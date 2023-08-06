import httpx
import typer

from neosctl import util
from neosctl.auth import ensure_login
from neosctl.schema import RegisterCore
from neosctl.schema import RemoveCore
from neosctl.util import process_response


app = typer.Typer()


def core_url(registry_api_url: str) -> str:
    return "{}/core".format(registry_api_url.rstrip("/"))


def data_product_url(registry_api_url: str, postfix: str = "") -> str:
    return "{}/data_product{}".format(registry_api_url.rstrip("/"), postfix)


@app.command(name="register-core")
def register_core(
    ctx: typer.Context,
    partition: str = typer.Argument(..., help="Core partition"),
    name: str = typer.Argument(..., help="Core name"),
):
    """Register a core.

    Register a core to recieve an identifier and access key for use in deployment.
    """
    @ensure_login
    def _request(ctx: typer.Context, name: str, rc: RegisterCore) -> httpx.Response:
        return util.post(
            ctx,
            core_url(ctx.obj.get_registry_api_url()),
            json=rc.dict(exclude_none=True),
        )

    rc = RegisterCore(partition=partition, name=name)

    r = _request(ctx, name, rc)
    process_response(r)


@app.command(name="list-cores")
def list_cores(
    ctx: typer.Context,
):
    """List existing registered cores.
    """
    @ensure_login
    def _request(ctx: typer.Context) -> httpx.Response:
        return util.get(
            ctx,
            core_url(ctx.obj.get_registry_api_url()),
        )

    r = _request(ctx)
    process_response(r)


@app.command(name="remove-core")
def remove_core(
    ctx: typer.Context,
    urn: str = typer.Argument(..., help="Core urn"),
):
    """Remove a registered core.
    """
    @ensure_login
    def _request(ctx: typer.Context, rc: RemoveCore) -> httpx.Response:
        return util.delete(
            ctx,
            url=core_url(ctx.obj.get_registry_api_url()),
            json=rc.dict(exclude_none=True),
        )

    rc = RemoveCore(urn=urn)

    r = _request(ctx, rc)
    process_response(r)


@app.command(name="search")
def search_products(
    ctx: typer.Context,
    search_term: str,
):
    """Search published data products across cores.
    """
    @ensure_login
    def _request(ctx: typer.Context, search_term: str) -> httpx.Response:
        return util.get(
            ctx,
            data_product_url(ctx.obj.get_registry_api_url(), "/search"),
            params={"search_term": search_term},
        )

    r = _request(ctx, search_term)
    process_response(r)


@app.command(name="get-product")
def get_product(
    ctx: typer.Context,
    urn: str,
):
    """Get data product details.
    """
    @ensure_login
    def _request(ctx: typer.Context, urn: str) -> httpx.Response:
        return util.get(
            ctx,
            data_product_url(ctx.obj.get_registry_api_url(), "/urn/{}".format(urn)),
        )

    r = _request(ctx, urn)
    process_response(r)
