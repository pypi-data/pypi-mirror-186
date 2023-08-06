import json
import os
import pathlib
import typing

import httpx
import typer

from neosctl import util
from neosctl.auth import ensure_login
from neosctl.schema import DataProductCreate
from neosctl.util import process_response


app = typer.Typer()


def product_url(ctx: typer.Context) -> str:
    return "{}/product".format(ctx.obj.get_gateway_api_url().rstrip("/"))


special_delimiters = {
    r"\t": "\t",
}


@app.command(name="template")
def template(
    ctx: typer.Context,
    name: str = typer.Argument(os.getenv("NEOSCTL_PRODUCT", ...), help="Data Product name"),
    filepath: str = typer.Option(..., "--filepath", "-f", help="Filepath of the csv template"),
    output_dir: str = typer.Option(..., "--output-dir", "-o", help="Output directory for the json template"),
    delimiter: str = typer.Option(",", "--delimiter", "-d", help="csv delimiter"),
    quotechar: typing.Optional[str] = typer.Option(None, "--quote-char", "-q", help="csv quote char"),
):
    """Generate a data product schema template from a csv.

    Given a csv with a header row, generate a template field schema.
    """
    @ensure_login
    def _request(ctx: typer.Context, f: typing.IO) -> httpx.Response:
        params = {k: v for k, v in [("delimiter", delimiter), ("quotechar", quotechar)] if v is not None}

        return util.post(
            ctx,
            "{dp_url}/template".format(dp_url=product_url(ctx)),
            params=params,
            files={"csv_file": f},
        )

    fp = util.get_file_location(filepath)

    with fp.open("rb") as f:
        r = _request(ctx, f)

    if r.status_code >= 400:
        process_response(r)

    fp = pathlib.Path(output_dir) / "{}.json".format(name)
    with fp.open("w") as f:
        json.dump(r.json(), f, indent=4)


@app.command(name="create")
def create_from_json(
    ctx: typer.Context,
    name: str = typer.Argument(os.getenv("NEOSCTL_PRODUCT", ...), help="Data Product name"),
    engine: str = typer.Option(..., "--engine", "-e", help="Storage engine"),
    filepath: str = typer.Option(..., "--filepath", "-f", help="Filepath of the table schema json payload"),
):
    """Create a data product.
    """
    @ensure_login
    def _request(ctx: typer.Context, dpc: DataProductCreate) -> httpx.Response:
        return util.post(
            ctx,
            "{dp_url}/{name}".format(dp_url=product_url(ctx), name=name),
            json=dpc.dict(exclude_none=True),
        )

    fp = util.get_file_location(filepath)
    fields = util.load_json_file(fp, "schema")

    dpc = DataProductCreate(engine=engine, fields=fields)

    r = _request(ctx, dpc)
    process_response(r)


@app.command()
def list(ctx: typer.Context):
    """List data products.
    """
    @ensure_login
    def _request(ctx: typer.Context):
        return util.get(ctx, product_url(ctx))

    r = _request(ctx)
    process_response(r)


@app.command()
def delete_data(
    ctx: typer.Context,
    name: str = typer.Argument(os.getenv("NEOSCTL_PRODUCT", ...), help="Data Product name"),
):
    """Delete data from a data product.
    """
    @ensure_login
    def _request(ctx: typer.Context) -> httpx.Response:
        return util.delete(
            ctx,
            "{dp_url}/{name}/data".format(dp_url=product_url(ctx), name=name),
        )

    r = _request(ctx)
    process_response(r)


@app.command()
def delete(
    ctx: typer.Context,
    name: str = typer.Argument(os.getenv("NEOSCTL_PRODUCT", ...), help="Data Product name"),
    force: bool = typer.Option(
        False,
        "--force",
        help="Force remove even if attached spark application is still running.",
    ),
):
    """Delete a data product.
    """
    @ensure_login
    def _request(ctx: typer.Context) -> httpx.Response:
        return util.delete(
            ctx,
            "{dp_url}/{name}".format(dp_url=product_url(ctx), name=name),
            params={"force": force},
        )

    r = _request(ctx)
    process_response(r)


@app.command()
def publish(
    ctx: typer.Context,
    name: str = typer.Argument(os.getenv("NEOSCTL_PRODUCT", ...), help="Data Product name"),
):
    """Publish a data product.
    """
    @ensure_login
    def _request(ctx: typer.Context) -> httpx.Response:
        return util.post(
            ctx,
            "{dp_url}/{name}/publish".format(dp_url=product_url(ctx), name=name),
        )

    r = _request(ctx)
    process_response(r)


@app.command()
def unpublish(
    ctx: typer.Context,
    name: str = typer.Argument(os.getenv("NEOSCTL_PRODUCT", ...), help="Data Product name"),
):
    """Unpublish a product.
    """
    @ensure_login
    def _request(ctx: typer.Context) -> httpx.Response:
        return util.delete(
            ctx,
            "{dp_url}/{name}/publish".format(dp_url=product_url(ctx), name=name),
        )

    r = _request(ctx)
    process_response(r)


@app.command(name="get")
def get_product(
    ctx: typer.Context,
    product_name: str = typer.Argument(os.getenv("NEOSCTL_PRODUCT", ...), help="Data Product name"),
):
    """Get data product schema.
    """
    @ensure_login
    def _request(ctx: typer.Context) -> httpx.Response:
        return util.get(
            ctx,
            "{dp_url}/{name}".format(dp_url=product_url(ctx), name=product_name),
        )

    r = _request(ctx)
    process_response(r)


@app.command()
def preview(
    ctx: typer.Context,
    product_name: str = typer.Argument(os.getenv("NEOSCTL_PRODUCT", ...), help="Data Product name"),
):
    """Preview data product data.

    Get the first 25 rows of a data product's data.
    """
    @ensure_login
    def _request(ctx: typer.Context) -> httpx.Response:
        return util.get(
            ctx,
            "{product_url}/{name}/data".format(
                product_url=product_url(ctx),
                name=product_name,
            ),
        )

    r = _request(ctx)
    process_response(r)
