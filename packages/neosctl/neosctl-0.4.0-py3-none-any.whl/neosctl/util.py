import configparser
import json
import pathlib
import typing

import httpx
import pydantic
import typer
from pygments import formatters
from pygments import highlight
from pygments import lexers

from neosctl import constant
from neosctl import schema


def dumps_formatted_json(payload: typing.Dict):
    return json.dumps(payload, indent=2, sort_keys=True)


def prettify_json(payload: typing.Dict) -> str:
    return highlight(dumps_formatted_json(payload), lexers.JsonLexer(), formatters.TerminalFormatter())


def is_success_response(response: httpx.Response):
    if 200 <= response.status_code < 300:
        return True
    return False


def send_output(msg: str, exit_code: int = 0):
    typer.echo(msg)

    raise typer.Exit(exit_code)


def process_response(response: httpx.Response, render_callable=prettify_json):
    exit_code = 0
    data = response.json()
    if response.status_code >= 400:
        exit_code = 1
        message = prettify_json(data)
    else:
        message = render_callable(data)

    send_output(
        msg=message,
        exit_code=exit_code,
    )


def read_config_dotfile() -> configparser.ConfigParser:
    c = configparser.ConfigParser()
    c.read(constant.PROFILE_FILEPATH)
    return c


def get_schema_profile(profile_name, allow_missing: bool = False, **kwargs):
    if allow_missing:
        return schema.OptionalProfile(**kwargs)

    try:
        return schema.Profile(**kwargs)
    except pydantic.ValidationError as e:
        required_fields = [err["loc"][0] for err in e.errors() if err["msg"] == "field required"]
        send_output(
            msg=(
                "Profile dotfile doesn't include fields:\n  {}\n"
                "Use neosctl -p {} profile init"
            ).format("\n  ".join(required_fields), profile_name),
            exit_code=1,
        )


def get_user_profile_section(c: configparser.ConfigParser, profile_name: str, allow_missing: bool = False):
    try:
        return c[profile_name]
    except KeyError:
        if not allow_missing:
            send_output(
                msg="Profile {} not found.".format(profile_name),
                exit_code=1,
            )


def get_user_profile(c: configparser.ConfigParser, profile_name: str, allow_missing: bool = False) -> schema.Profile:
    profile_config = get_user_profile_section(c, profile_name, allow_missing=allow_missing)
    if profile_config:
        return get_schema_profile(profile_name, allow_missing=allow_missing, **profile_config)


def bearer(ctx: typer.Context) -> typing.Optional[typing.Dict]:
    if not (ctx.obj.profile and ctx.obj.profile.access_token != ""):
        return None

    return {"Authorization": "Bearer {}".format(ctx.obj.profile.access_token)}


def check_profile_exists(ctx: typer.Context):
    if not ctx.obj.profile:
        send_output(
            msg="Profile not found! Run neosctl -p {} profile init".format(ctx.obj.profile_name),
            exit_code=1,
        )

    return True


def upsert_config(
    ctx: typer.Context,
    profile: schema.Profile,
) -> configparser.ConfigParser:
    ctx.obj.config[ctx.obj.profile_name] = profile.dict()

    with constant.PROFILE_FILEPATH.open("w") as profile_file:
        ctx.obj.config.write(profile_file)

    return ctx.obj.config


def remove_config(
    ctx: typer.Context,
) -> configparser.ConfigParser:
    if not ctx.obj.config.remove_section(ctx.obj.profile_name):
        send_output(
            msg="Can not remove {} profile, profile not found.".format(ctx.obj.profile_name),
            exit_code=1,
        )

    with constant.PROFILE_FILEPATH.open("w") as profile_file:
        ctx.obj.config.write(profile_file)

    return ctx.obj.config


def get_file_location(filepath: str) -> pathlib.Path:
    fp = pathlib.Path(filepath)
    if not fp.exists():
        send_output(
            msg="Can not find file: {}".format(fp),
            exit_code=1,
        )
    return fp


def load_json_file(fp: pathlib.Path, content_type: str) -> typing.Union[typing.Dict, typing.List]:
    with fp.open() as f:
        try:
            data = json.load(f)
        except json.decoder.JSONDecodeError:
            send_output(
                msg="Invalid {} file, must be json format.".format(content_type),
                exit_code=1,
            )
    return data


def _request(ctx: typer.Context, method: str, url: str, **kwargs):
    return httpx.request(method=method, url=url, headers=bearer(ctx), verify=not ctx.obj.profile.ignore_tls, **kwargs)


def get(ctx: typer.Context, url: str, **kwargs):
    return _request(ctx, "GET", url, **kwargs)


def post(ctx: typer.Context, url: str, **kwargs):
    return _request(ctx, "POST", url, **kwargs)


def put(ctx: typer.Context, url: str, **kwargs):
    return _request(ctx, "PUT", url, **kwargs)


def patch(ctx: typer.Context, url: str, **kwargs):
    return _request(ctx, "PATCH", url, **kwargs)


def delete(ctx: typer.Context, url: str, **kwargs):
    return _request(ctx, "DELETE", url, **kwargs)
