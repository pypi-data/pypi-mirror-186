import httpx
import typer

from neosctl import util
from neosctl.auth import ensure_login
from neosctl.util import process_response


app = typer.Typer()


def consume_url(gateway_api_url: str) -> str:
    return "{}/consume".format(gateway_api_url.rstrip("/"))


@app.command()
def query(
    ctx: typer.Context,
    statement: str,
):
    """Query a published data product.
    """
    @ensure_login
    def _request(ctx: typer.Context) -> httpx.Response:
        return util.post(
            ctx,
            url=consume_url(ctx.obj.gateway_api_url),
            json={
                "statement": statement,
            },
        )

    r = _request(ctx)
    process_response(r)
