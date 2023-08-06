import typing

import httpx
import typer

from neosctl import util
from neosctl.auth import ensure_login
from neosctl.util import process_response


app = typer.Typer()


def storage_url(ctx: typer.Context, postfix: str) -> str:
    return "{}/{}".format(ctx.obj.storage_api_url.rstrip("/"), postfix)


def _load_statement(statement: typing.Optional[str], statement_filepath: typing.Optional[str]):
    if statement is None and statement_filepath is None:
        util.send_output(
            msg="At least one of --statement/--statement-filepath is required.",
            exit_code=1,
        )

    if statement_filepath:
        fp = util.get_file_location(statement_filepath)

        statement = fp.read_text()

    return statement


def _load_params(params_filepath: typing.Optional[str]):
    params = None
    if params_filepath:
        fp = util.get_file_location(params_filepath)

        params = util.load_json_file(fp, "params")

    return params


def _handle(
    ctx: typer.Context,
    postfix: str,
    statement: typing.Optional[str] = None,
    statement_filepath: typing.Optional[str] = None,
    params_filepath: typing.Optional[str] = None,
):
    @ensure_login
    def _request(ctx: typer.Context, params: typing.List[typing.Any]) -> httpx.Response:
        return util.post(
            ctx,
            url=storage_url(ctx, postfix),
            json={
                "statement": statement,
                "params": params,
            },
        )

    statement = _load_statement(statement, statement_filepath)
    params = _load_params(params_filepath)

    r = _request(ctx, params)
    process_response(r)


@app.command()
def execute(
    ctx: typer.Context,
    statement: typing.Optional[str] = typer.Option(None, "--statement", "-s", help="pSQL statement"),
    statement_filepath: typing.Optional[str] = typer.Option(
        None,
        "--statement-filepath",
        "-sf",
        help="Filepath for statement sql file.",
    ),
    params_filepath: typing.Optional[str] = typer.Option(
        None,
        "--params-filepath",
        "-pf",
        help="Filepath for statement params json file.",
    ),
):
    """Execute a statement.
    """
    _handle(ctx, "execute", statement, statement_filepath, params_filepath)


@app.command()
def executemany(
    ctx: typer.Context,
    statement: typing.Optional[str] = typer.Option(None, "--statement", "-s", help="pSQL statement"),
    statement_filepath: typing.Optional[str] = typer.Option(
        None,
        "--statement-filepath",
        "-sf",
        help="Filepath for statement sql file.",
    ),
    params_filepath: typing.Optional[str] = typer.Option(
        None,
        "--params-filepath",
        "-pf",
        help="Filepath for statement params json file.",
    ),
):
    """Execute a statement with multiple input params.
    """
    _handle(ctx, "executemany", statement, statement_filepath, params_filepath)


@app.command()
def fetch(
    ctx: typer.Context,
    statement: str = typer.Option(None, "--statement", "-s", help="pSQL statement"),
    statement_filepath: str = typer.Option(
        None,
        "--statement-filepath",
        "-sf",
        help="Filepath for statement sql file.",
    ),
    params_filepath: str = typer.Option(
        None,
        "--params-filepath",
        "-pf",
        help="Filepath for statement params json file.",
    ),
):
    """Fetch results of a statement.
    """
    _handle(ctx, "fetch", statement, statement_filepath, params_filepath)


@app.command()
def fetchrow(
    ctx: typer.Context,
    statement: str = typer.Option(None, "--statement", "-s", help="pSQL statement"),
    statement_filepath: str = typer.Option(
        None,
        "--statement-filepath",
        "-sf",
        help="Filepath for statement sql file.",
    ),
    params_filepath: str = typer.Option(
        None,
        "--params-filepath",
        "-pf",
        help="Filepath for statement params json file.",
    ),
):
    """Fetch first result of a statement.
    """
    _handle(ctx, "fetchrow", statement, statement_filepath, params_filepath)
