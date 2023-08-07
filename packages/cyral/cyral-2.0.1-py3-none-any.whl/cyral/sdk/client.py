"""Module client defines a Cyral API client with support for authentication.
Currently only public client based OAuth2 PKCE code flow is supported.
"""
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import os
import socketserver
import sys
from threading import Lock, Thread
from time import sleep
from typing import Dict, Optional, Tuple, Type
import webbrowser

from oauthlib import oauth2
from oauthlib.oauth2.rfc6749.clients.base import AUTH_HEADER
from oauthlib.oauth2.rfc6749.errors import (
    FatalClientError,
    MismatchingStateError,
    MissingCodeError,
    OAuth2Error,
    TokenExpiredError,
)
import requests

SDK_CLIENT_ID = "cyral-sdk-client"
DEFAULT_LOCAL_PORT = 8005


class StoredCredentials:
    """StoredCredentials reads, writes, and stores long term user credentials
    stored in a file. It allows the creds_file to be None in which case the
    credentials are not read or written from/to file but (if set) just held
    in this object. This removes the need for the caller to specially handle
    the case where stored credentials are not to be used.
    """

    def __init__(self, creds_file: Optional[str] = None) -> None:
        self.creds_file = creds_file
        self.creds = None
        if not self.creds_file:
            return
        try:
            with open(self.creds_file, mode="r", encoding="utf-8") as creds_fd:
                self.creds = json.loads(creds_fd.read())
        except FileNotFoundError:
            # file does not exist yet.
            return

    def _get_cred(self, cred_name: str) -> Optional[str]:
        return self.creds.get(cred_name, None) if self.creds else None

    def _set_cred(self, cred_name: str, cred: Optional[str]) -> None:
        if cred:
            if not self.creds:
                self.creds = {}
            self.creds[cred_name] = cred
        elif self.creds:
            try:
                del self.creds[cred_name]
            except KeyError:
                pass
        self._write()

    def get_refresh_token(self) -> Optional[str]:
        """refresh_token returns the stored refresh token if any."""
        return self._get_cred("refreshToken")

    def set_refresh_token(self, token: Optional[str]) -> None:
        """set the value for the saved refresh token."""
        self._set_cred("refreshToken", token)

    def get_offline_token(self) -> Optional[str]:
        """offline_token returns the stored offline token if any."""
        return self._get_cred("offlineToken")

    def set_offline_token(self, token: Optional[str]) -> None:
        """set the value for the saved offline token."""
        self._set_cred("offlineToken", token)

    def _write(self) -> None:
        """write the credentials to the creds file."""
        if not self.creds_file:
            return
        creds_path = os.path.dirname(self.creds_file)
        # create directory if needed.
        try:
            os.mkdir(creds_path)
        except OSError:
            pass  # ignore error creating directory.

        try:
            creds_blob = json.dumps(self.creds, sort_keys=True, indent=4)

            def opener(path, flags):
                return os.open(path, flags, 0o600)

            with open(
                self.creds_file, mode="w", encoding="utf-8", opener=opener
            ) as creds_file:
                print(creds_blob, file=creds_file)
        except OSError:
            print(
                f"Warning: error saving credentials to {self.creds_file}",
                file=sys.stderr,
            )


class TokenRequestError(OAuth2Error):
    """Exception raised when authentication fails."""

    error = "error obtaining OAuth2 token"


class Client:
    # pylint: disable=too-few-public-methods
    # pylint: disable=too-many-instance-attributes
    """
    Client enables interaction with the Cyral control plane using APIs.
    """

    def __init__(  # pylint: disable=too-many-arguments
        self,
        cp_address: str,
        client_id: str = SDK_CLIENT_ID,
        stored_creds: Optional[StoredCredentials] = None,
        local_port: int = DEFAULT_LOCAL_PORT,
        offline_access: bool = False,
        idp: Optional[str] = None,
    ) -> None:
        self.cp_address = cp_address
        self.oauth2_redirect_port = local_port
        self.oauth2_redirect_url = f"http://localhost:{local_port}"
        self.oauth2_token_endpoint = (
            f"https://{cp_address}/auth/realms/default/"
            + "protocol/openid-connect/token"
        )
        authz_endpoint = (
            f"https://{cp_address}/auth/realms/default/"
            + "protocol/openid-connect/auth"
        )
        if idp:
            authz_endpoint = authz_endpoint + f"?kc_idp_hint={idp}"
        self.oauth2_authorize_endpoint = authz_endpoint
        if not stored_creds:
            stored_creds = StoredCredentials()
        self.stored_creds = stored_creds
        self.offline_access = offline_access
        if offline_access:
            refresh_token = self.stored_creds.get_offline_token()
        else:
            refresh_token = self.stored_creds.get_refresh_token()
        self.oauth2_client = oauth2.WebApplicationClient(
            client_id,
            redirect_url=self.oauth2_redirect_url,
            refresh_token=refresh_token,
            code_challenge_method="S256",
        )
        self._auth_lock = Lock()

    def get_auth_header(self) -> Dict[str, str]:
        """Return an authorization header for making API call to Cyral
        Control Plane.
        """
        with self._auth_lock:
            return self._get_auth_header()

    def _get_auth_header(self) -> Dict[str, str]:
        def _auth_header() -> Dict[str, str]:
            uri = f"https://{self.cp_address}"
            _, headers, _ = self.oauth2_client.add_token(
                uri, token_placement=AUTH_HEADER
            )
            return headers

        if self.oauth2_client.access_token:
            try:
                return _auth_header()
            except TokenExpiredError:
                # need to regenerate the access token, fall through.
                pass

        # generate a fresh access token using the refresh token if we have one.
        refresh_token = self.oauth2_client.refresh_token
        if refresh_token:
            try:
                self._refresh_access_token(refresh_token)
            except (FatalClientError, OAuth2Error):
                # refresh token expired, fall through to full auth.
                pass
            else:
                return _auth_header()

        # we have neither a valid access token, nor a refresh token. So, we
        # need to do things from scratch.
        self._authenticate_user()
        return _auth_header()

    def _refresh_access_token(self, refresh_token: str) -> None:
        url, headers, body = self.oauth2_client.prepare_refresh_token_request(
            self.oauth2_token_endpoint,
            refresh_token=refresh_token,
            client_id=SDK_CLIENT_ID,
            redirect_uri=self.oauth2_redirect_url,
        )
        resp = requests.post(
            url, data=body.encode("utf-8"), headers=headers, timeout=5
        )
        self.oauth2_client.parse_request_body_response(resp.content)

    def _oauth_redirect_handler(
        self, oauth2_client: oauth2.WebApplicationClient
    ) -> Type[BaseHTTPRequestHandler]:
        """_oauth_redirect_handler returns a subclass of HTTPRequestHandler
        that handles the OAuth2 redirect from the authorize endpoint.
        """

        class _OAuthRedirectHandler(BaseHTTPRequestHandler):
            def __init__(
                self,
                request: bytes,
                client_address: tuple[str, int],
                server: socketserver.BaseServer,
            ) -> None:
                super().__init__(request, client_address, server)
                self.close_connection = True

            def log_request(self, code="-", size="-") -> None:
                # override the log_request method from the base class
                # so we do not log successful requests.
                pass

            def do_GET(self) -> None:  # pylint: disable=invalid-name
                """Handle an OAuth2 redirect request."""
                success_response = """
                    <html>
                    <head>
                    <title>Authentication success</title>
                    </head>
                    <body>
                    <h2>Authentication succeeded</h2>
                    <p>
                    Please close this window for additional security.
                    </body>
                    </head>
                """
                path = self.path
                uri = f"https://localhost{path}"
                try:
                    _ = oauth2_client.parse_request_uri_response(
                        uri, oauth2_client.state
                    )
                except (MismatchingStateError, MissingCodeError) as ex:
                    self.send_error(HTTPStatus.BAD_REQUEST, explain=str(ex))
                else:
                    self.send_response(HTTPStatus.OK)
                    self.send_header("Content-Type", "text/html")
                    self.end_headers()
                    self.wfile.write(success_response.encode("utf-8"))

        return _OAuthRedirectHandler

    def _start_webserver(self) -> Tuple[Thread, HTTPServer]:
        bind_addr = ("127.0.0.1", self.oauth2_redirect_port)
        httpd = HTTPServer(
            bind_addr, self._oauth_redirect_handler(self.oauth2_client)
        )
        httpd.timeout = 180  # wait at most 3 minutes for auth to complete.
        ws_thread = Thread(target=httpd.handle_request)
        ws_thread.start()
        return (ws_thread, httpd)

    def _authenticate_user(self) -> None:
        code_verifier = self.oauth2_client.create_code_verifier(64)
        code_challenge = self.oauth2_client.create_code_challenge(
            code_verifier, code_challenge_method="S256"
        )
        requested_scopes = ["offline_access"] if self.offline_access else None
        auth_url, _, _ = self.oauth2_client.prepare_authorization_request(
            self.oauth2_authorize_endpoint,
            code_challenge=code_challenge,
            code_challenge_method="S256",
            scope=requested_scopes,
        )
        (ws_thread, httpd) = self._start_webserver()
        # sleep a while to let it get set up. This is kludgy but I can't think
        # of anything better.
        sleep(0.2)
        print(
            "Please complete authentication in the browser.", file=sys.stderr
        )
        print(
            "If the browser does not launch automatically, "
            + f"visit the following URL in the browser:\n\n{auth_url}",
            file=sys.stderr,
        )
        try:
            webbrowser.open(auth_url)
        except webbrowser.Error:
            pass  # ignore error if browser cannot be launched.
        ws_thread.join()
        httpd.server_close()
        # We now should have an authorization code set in oauth2_client.
        # Use it to obtain a token.
        url, headers, body = self.oauth2_client.prepare_token_request(
            self.oauth2_token_endpoint,
            code_verifier=self.oauth2_client.code_verifier,
        )
        resp = requests.post(
            url, data=body.encode("utf-8"), headers=headers, timeout=5
        )
        self.oauth2_client.parse_request_body_response(resp.content)
        # save refresh token to saved credentials
        saved_token = self.oauth2_client.refresh_token
        if self.offline_access:
            self.stored_creds.set_offline_token(saved_token)
        else:
            self.stored_creds.set_refresh_token(saved_token)
