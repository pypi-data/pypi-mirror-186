import typing

import click
import typer

from neosctl import schema
from neosctl import util
from neosctl.util import check_profile_exists
from neosctl.util import get_user_profile
from neosctl.util import is_success_response
from neosctl.util import process_response
from neosctl.util import read_config_dotfile
from neosctl.util import send_output
from neosctl.util import upsert_config


app = typer.Typer()


def auth_url(iam_api_url: str) -> str:
    return "{}".format(iam_api_url.rstrip("/"))


def _check_refresh_token_exists(ctx: typer.Context):
    if ctx.obj.profile.refresh_token == "":
        send_output(
            msg="You need to login. Run neosctl -p {} auth login".format(ctx.obj.profile_name),
            exit_code=1,
        )

    return True


def ensure_login(method):
    def check_access_token(*args, **kwargs):
        ctx = args[0]
        if not isinstance(ctx, click.core.Context):
            # Developer reminder
            raise RuntimeError("First argument should be typer.Context instance")  # pragma: no cover

        r = method(*args, **kwargs)

        check_profile_exists(ctx)

        # Try to refresh token
        # Confirm it is a token invalid 401, registry not configured mistriggers this flow.
        if r.status_code == 401:
            data = r.json()
            if "code" in data and data["code"].startswith("A0"):
                refresh_token(ctx)

                # Refresh the context
                c = read_config_dotfile()
                ctx.obj.config = c
                ctx.obj.profile = get_user_profile(c, ctx.obj.profile_name)

                r = method(*args, **kwargs)

        return r
    return check_access_token


def _update_profile(
    ctx: typer.Context,
    auth: schema.Auth = schema.Auth(),
):
    profile = schema.Profile(
        gateway_api_url=ctx.obj.gateway_api_url,
        registry_api_url=ctx.obj.registry_api_url,
        iam_api_url=ctx.obj.iam_api_url,
        storage_api_url=ctx.obj.storage_api_url,
        user=ctx.obj.profile.user,
        access_token=auth.access_token,
        refresh_token=auth.refresh_token,
        ignore_tls=ctx.obj.profile.ignore_tls,
    )

    return profile


@app.command()
def login(
    ctx: typer.Context,
    password: typing.Optional[str] = typer.Option(None, "--password", "-p"),
):
    """Login to neos.
    """
    check_profile_exists(ctx)

    if password is None:
        password = typer.prompt(
            "[{profile}] Enter password for user ({user})".format(
                profile=ctx.obj.profile_name,
                user=ctx.obj.profile.user,
            ),
            hide_input=True,
        )

    r = util.post(
        ctx,
        "{auth_url}/login".format(auth_url=auth_url(ctx.obj.get_iam_api_url())),
        json={"user": ctx.obj.profile.user, "password": password},
    )

    if not is_success_response(r):
        process_response(r)

    upsert_config(ctx, _update_profile(ctx, schema.Auth(**r.json())))

    send_output(
        msg="Login success",
        exit_code=0,
    )


@app.command()
def logout(ctx: typer.Context):
    """Logout from neos.
    """
    check_profile_exists(ctx)

    _check_refresh_token_exists(ctx)

    r = util.post(
        ctx,
        "{auth_url}/logout".format(auth_url=auth_url(ctx.obj.get_iam_api_url())),
        json={"refresh_token": ctx.obj.profile.refresh_token},
    )

    if not is_success_response(r):
        process_response(r)

    upsert_config(ctx, _update_profile(ctx, schema.Auth()))

    send_output(
        msg="Logout success",
        exit_code=0,
    )


def refresh_token(ctx: typer.Context):
    check_profile_exists(ctx)
    _check_refresh_token_exists(ctx)

    r = util.post(
        ctx,
        "{auth_url}/refresh".format(auth_url=auth_url(ctx.obj.get_iam_api_url())),
        json={"refresh_token": ctx.obj.profile.refresh_token},
    )

    if not is_success_response(r):
        process_response(r)

    upsert_config(ctx, _update_profile(ctx, schema.Auth(**r.json())))

    return r
