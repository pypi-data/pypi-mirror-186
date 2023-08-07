"""Configure AWS profile to access S3 via Cyral sidecar"""

import os
import subprocess  # nosec: B404
import sys
from pathlib import Path
from typing import Any

import pkg_resources
import yaml
from awscli.customizations.configure.writer import ConfigFileWriter
from botocore.session import get_session

S3_PROXY_PLUGIN = "awscli-plugin-s3-proxy"


def _get_config_file_path(file: str) -> str:
    # we use the botocore and awscli existing code to get this done.
    session = get_session()
    config_path = session.get_config_variable(file)
    config_path = os.path.expanduser(config_path)
    return config_path


def _write_config_file(values: Any, config_file_name: str) -> None:
    writer = ConfigFileWriter()
    # this will create or update the profile as needed.
    writer.update_config(values, config_file_name)


def update_aws_creds(
    access_token: str,
    user_email: str,
    aws_profile_name: str,
    silent: bool,
) -> None:
    """Update AWS credentials based on the Cyral access token."""
    values = {
        "aws_access_key_id": f"{user_email}:{access_token}",
        "aws_secret_access_key": "none",
        "__section__": aws_profile_name,
    }

    creds_path = _get_config_file_path("credentials_file")
    _write_config_file(values, creds_path)

    if not silent:
        print(f"Updated S3 token for AWS profile '{aws_profile_name}'")
        if aws_profile_name != "default":
            print(
                "\nTo use this profile, specify the profile name using "
                "--profile, as shown:\n\n"
                f"aws s3 ls --profile {aws_profile_name}\n"
            )


class S3ProxyPluginNotInstalled(Exception):
    """S3ProxyPluginNotInstalled exception is raised if the user does
    not have the S3 proxy plugin installed."""


def configure_s3_proxy_settings(
    aws_profile_name: str,
    sidecar_endpoint: str,
    ca_bundle: str,
) -> None:
    """Configure S3 proxy settings in the AWS profile."""
    if not _s3_plugin_is_installed():
        raise S3ProxyPluginNotInstalled(
            "Please first install S3 proxy plugin using the command:\n\n"
            + f"pip3 install {S3_PROXY_PLUGIN}"
        )
    try:
        _update_s3_proxy_plugins()
        _update_ca_bundle(aws_profile_name, ca_bundle)
        update_s3_proxy_endpoint(aws_profile_name, sidecar_endpoint)
    except Exception as ex:
        raise Exception("error configuring S3 proxy settings") from ex


def _save_ca_bundle(ca_bundle: str, direname: str) -> str:
    ca_bundle_default_path = Path(direname) / "cyral_ca_bundle.pem"
    with open(ca_bundle_default_path, "w", encoding="utf-8") as file:
        file.write(ca_bundle)
    return str(ca_bundle_default_path)


def _update_ca_bundle(aws_profile_name: str, ca_bundle: str) -> None:
    config_path = _get_config_file_path("config_file")
    ca_bundle_direname = os.path.dirname(config_path)
    cyral_ca_bundle_file = _save_ca_bundle(ca_bundle, ca_bundle_direname)
    values = {
        "ca_bundle": cyral_ca_bundle_file,
        "__section__": "profile " + aws_profile_name,
    }
    _write_config_file(values, config_path)


def _update_s3_proxy_plugins() -> None:
    installed_plugin_name = S3_PROXY_PLUGIN.replace("-", "_")
    values = {
        "s3-proxy": installed_plugin_name,
        "__section__": "plugins",
    }
    if _get_cli_version() == "v2":
        values.update(
            {"cli_legacy_plugin_path": _get_cli_legacy_plugin_path()},
        )
    config_path = _get_config_file_path("config_file")
    _write_config_file(values, config_path)


def update_s3_proxy_endpoint(aws_profile_name: str, endpoint: str) -> None:
    """update the S3 proxy endpoint"""
    endpoint = endpoint.replace("http://", "").replace("https://", "")
    values = {
        "s3": {
            "proxy": f"http://{endpoint}",
        },
        "__section__": "profile " + aws_profile_name,
    }
    config_path = _get_config_file_path("config_file")
    _write_config_file(values, config_path)


def s3_proxy_is_configured(aws_profile_name: str) -> bool:
    """Check if S3 proxy is setup in the specified AWS profile."""
    session = get_session()
    config = session.full_config
    # a correctly configured config looks like the following:
    # {
    #     "plugins":{
    #         "s3-proxy":"awscli_plugin_s3_proxy"
    #     },
    #     "profiles":{
    #         "cyral":{
    #             "ca_bundle":"/home/user/.aws/cyral_ca_bundle.pem",
    #             "s3":{
    #                 "proxy":"http://sidecar.endpoint:453"
    #             }
    #         }
    #     }
    # }
    return (
        # check if the config has a plugins field
        config.get("plugins")
        # check if plugins has an entry for "s3-proxy"
        and config["plugins"].get("s3-proxy")
        # check if the config has a "profiles" field
        and config.get("profiles")
        # check if an entry for the given aws profile exists inside "profiles"
        and config["profiles"].get(aws_profile_name)
        # check if "ca_bundle" got a value for the given aws profile
        and config["profiles"][aws_profile_name].get("ca_bundle")
        # check if the value given to "ca_bundle" is a valid file
        and Path(config["profiles"][aws_profile_name]["ca_bundle"]).is_file()
        # check if "s3" got a value for the given aws profile
        and config["profiles"][aws_profile_name].get("s3")
        # check if "proxy" got a non-None value inside that s3 object
        and config["profiles"][aws_profile_name]["s3"].get("proxy")
        # check if s3 proxy plugin is installed
        and _s3_plugin_is_installed()
    )


def _get_cli_legacy_plugin_path() -> str:
    # should be the dir of the installed S3_PROXY_PLUGIN
    try:
        plugin_info = subprocess.check_output(  # nosec: B603
            [sys.executable, "-m", "pip", "show", S3_PROXY_PLUGIN],
        ).decode("utf-8")
        return yaml.safe_load(plugin_info)["Location"]
    except subprocess.CalledProcessError as ex:
        raise Exception(
            "Failed to find a legacy plugin path for AWS cli.",
        ) from ex


def _s3_plugin_is_installed() -> bool:
    # pylint: disable=not-an-iterable
    pkgs = [pkg.key for pkg in pkg_resources.working_set]
    return S3_PROXY_PLUGIN in pkgs


def _get_cli_version() -> str:
    # returns the major version
    try:
        cli_output = subprocess.check_output(  # nosec: B603 B607
            ["aws", "--version"],
        ).decode("utf-8")
        if not cli_output.startswith("aws-cli"):
            raise AssertionError(f"unrecognized AWS CLI version: {cli_output}")
        # example output: aws-cli/2.1.15 Python/3.7.3 ...
        aws_version = cli_output.split("/")[1]
        major_version = "v" + aws_version[0]
        return major_version
    except (subprocess.CalledProcessError, AssertionError) as ex:
        raise Exception(
            "Failed to get AWS cli version. Make sure AWS CLI is installed!",
        ) from ex
