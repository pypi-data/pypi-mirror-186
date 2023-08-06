import typing

import httpx
import typer

from neosctl import schema
from neosctl import util
from neosctl.auth import ensure_login
from neosctl.util import process_response


app = typer.Typer()


def iam_url(iam_api_url: str, postfix: str = "") -> str:
    return "{}/{}".format(iam_api_url.rstrip("/"), postfix)


@app.command()
def list(
    ctx: typer.Context,
    page: int = typer.Option(1, help="Page number."),
    page_size: int = typer.Option(10, help="Page size number."),
    resource: typing.Optional[str] = typer.Option(None, help="Resource nrn."),
):
    """List existing policies.
    """
    @ensure_login
    def _request(ctx: typer.Context):
        params = {"page": page, "page_size": page_size}
        if resource:
            params["resource"] = resource

        return util.get(
            ctx,
            iam_url(ctx.obj.get_iam_api_url(), "policy/users"),
            params=params,
        )

    r = _request(ctx)
    process_response(r)


@app.command(name="create")
def create_from_json(
    ctx: typer.Context,
    filepath: str = typer.Argument(..., help="Filepath of the user policy json payload"),
):
    """Create an IAM policy.
    """
    @ensure_login
    def _request(ctx: typer.Context, user_policy: schema.UserPolicy) -> httpx.Response:
        return util.post(
            ctx,
            "{iam_url}".format(iam_url=iam_url(ctx.obj.get_iam_api_url(), "policy/user")),
            json=user_policy.dict(),
        )

    fp = util.get_file_location(filepath)
    user_policy_payload = util.load_json_file(fp, "schema")

    user_policy = schema.UserPolicy(**user_policy_payload)

    r = _request(ctx, user_policy)
    process_response(r)


@app.command(name="update")
def update_from_json(
    ctx: typer.Context,
    principal: str = typer.Argument(..., help="Principal uuid"),
    filepath: str = typer.Argument(..., help="Filepath of the user policy json payload"),
):
    """Update an existing IAM policy.
    """
    @ensure_login
    def _request(ctx: typer.Context, user_policy: schema.UserPolicy) -> httpx.Response:
        return util.put(
            ctx,
            "{iam_url}".format(iam_url=iam_url(ctx.obj.get_iam_api_url(), "policy/user")),
            params={"user_nrn": principal},
            json=user_policy.dict(),
        )

    fp = util.get_file_location(filepath)
    user_policy_payload = util.load_json_file(fp, "schema")

    user_policy = schema.UserPolicy(**user_policy_payload)

    r = _request(ctx, user_policy)
    process_response(r)


@app.command()
def delete(ctx: typer.Context, user_nrn: str):
    """Delete an existing IAM policy.
    """
    @ensure_login
    def _request(ctx: typer.Context) -> httpx.Response:
        return util.delete(
            ctx,
            "{iam_url}".format(iam_url=iam_url(ctx.obj.get_iam_api_url(), "policy/user")),
            params={"user_nrn": user_nrn},
        )

    r = _request(ctx)
    process_response(r)


@app.command()
def get(ctx: typer.Context, user_nrn: str):
    """Get an existing IAM policy.
    """
    @ensure_login
    def _request(ctx: typer.Context) -> httpx.Response:
        return util.get(
            ctx,
            "{iam_url}".format(iam_url=iam_url(ctx.obj.get_iam_api_url(), "policy/user")),
            params={"user_nrn": user_nrn},
        )

    r = _request(ctx)
    process_response(r)
