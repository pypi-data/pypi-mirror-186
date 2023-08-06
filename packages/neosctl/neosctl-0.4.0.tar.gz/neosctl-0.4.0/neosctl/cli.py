import configparser
import os

import typer

from neosctl import auth
from neosctl import constant
from neosctl import consume
from neosctl import iam
from neosctl import metadata
from neosctl import product
from neosctl import profile
from neosctl import registry
from neosctl import schema
from neosctl import spark
from neosctl import storage
from neosctl.util import get_user_profile
from neosctl.util import read_config_dotfile


def _generate_common_schema(
    gateway_api_url: str,
    registry_api_url: str,
    iam_api_url: str,
    storage_api_url: str,
    profile_name: str,
    config: configparser.ConfigParser,
    profile: schema.Profile = None,
):
    common_schema = schema.Common(
        gateway_api_url=gateway_api_url,
        registry_api_url=registry_api_url,
        iam_api_url=iam_api_url,
        storage_api_url=storage_api_url,
        profile_name=profile_name,
        config=config,
        profile=profile,
    )
    common_schema.gateway_api_url = common_schema.get_gateway_api_url()
    common_schema.registry_api_url = common_schema.get_registry_api_url()
    common_schema.iam_api_url = common_schema.get_iam_api_url()
    common_schema.storage_api_url = common_schema.get_storage_api_url()

    return common_schema


def callback(
    ctx: typer.Context,
    gateway_api_url: str = typer.Option("", "--gateway-api-url", "--gurl", help="Gateway API URL"),
    registry_api_url: str = typer.Option("", "--registry-api-url", "--rurl", help="Registry API URL"),
    iam_api_url: str = typer.Option("", "--iam-api-url", "--iurl", help="IAM API URL"),
    storage_api_url: str = typer.Option("", "--storage-api-url", "--surl", help="Storage API URL"),
    profile: str = typer.Option(
        os.getenv("NEOSCTL_PROFILE", constant.DEFAULT_PROFILE),
        "--profile", "-p",
        help="Profile name",
    ),
):
    config = read_config_dotfile()
    user_profile = get_user_profile(config, profile, allow_missing=True)

    common_schema = _generate_common_schema(
        gateway_api_url=gateway_api_url,
        registry_api_url=registry_api_url,
        iam_api_url=iam_api_url,
        storage_api_url=storage_api_url,
        profile_name=profile,
        config=config,
        profile=user_profile,
    )

    ctx.obj = common_schema


def common(
    ctx: typer.Context,
):
    user_profile = get_user_profile(ctx.obj.config, ctx.obj.profile_name)
    ctx.obj.profile = user_profile


app = typer.Typer(name="neosctl", callback=callback)
app.add_typer(profile.app, name="profile", help="Manage profiles.")
app.add_typer(auth.app, name="auth", callback=common, help="Manage authentication status.")
app.add_typer(consume.app, name="consume", callback=common, help="Consume published data products.")
app.add_typer(iam.app, name="iam", callback=common, help="Manage access policies.")
app.add_typer(storage.app, name="storage", callback=common, help="Interact with Storage (as a service).")
app.add_typer(metadata.app, name="metadata", callback=common, help="Manage and browse metadata.")
app.add_typer(product.app, name="product", callback=common, help="Manage data products.")
app.add_typer(registry.app, name="registry", callback=common, help="Manage cores and search data products.")
app.add_typer(spark.app, name="spark", callback=common, help="Manage data product spark/secrets.")
