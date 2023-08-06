import json
import re
from os import getcwd
from os.path import join, isfile

import click
from dotenv import dotenv_values

from amplify_cf.ext import common_options
from amplify_cf.utils import resolve_vars, resolve_value


@click.group(invoke_without_command=True)
@common_options
@click.pass_context
def config(ctx):
    if not ctx.invoked_subcommand:
        ctx.invoke(update_exports)
        ctx.invoke(update_amplify)


@config.command(name="sync-exports")
@common_options
@click.argument("stack", required=False)
@click.pass_obj
def update_exports(obj, stack):
    exports = join(getcwd(), "src", f"aws-exports.{obj.env}.js")

    mapping = {}
    if isfile(obj.amplify_cf_file):
        mapping = json.load(open(obj.amplify_cf_file, "r")).get("mapping", {})

    if not isfile(exports):
        click.secho(f"Unable to locate exports file: {exports}", fg="yellow")
        return

    click.secho(f"Updating: {exports}", fg="blue")
    with open(exports, "r+") as f:
        content = f.read()
        f.seek(0)

        for name, value in resolve_vars(mapping, obj.stack_variables()).items():
            content = re.sub(rf'{name}: "[^\"]*"', f'{name}: "{value}"', content)

        f.write(content)


@config.command(name="sync-amplify")
@common_options
@click.argument("stack", required=False)
@click.pass_context
def update_amplify(ctx, stack: str):
    amplify_meta = join(getcwd(), "amplify", "backend", "amplify-meta.json")
    if not isfile(amplify_meta):
        click.secho(f"Unable to locate file: {amplify_meta}", fg="yellow")
        return

    with open(amplify_meta, "r+") as f:
        config = json.load(fp=f)

        for section in ["auth", "api", "function", "storage", "custom"]:
            for service in config.get(section).keys():
                local = config.get(section).get(service)
                if "output" not in local:
                    continue

                key = "root." + section + service
                for k in local["output"].keys():
                    if k in ctx.obj.variables[key]:
                        local["output"][k] = ctx.obj.variables[key][k]

        f.seek(0)
        json.dump(config, f, indent=2)


@config.command(name="sync-local")
@common_options
@click.argument("stack", required=False)
@click.pass_context
def update_env_local(ctx, stack: str):
    env_local = join(getcwd(), ".env.local")
    if not isfile(env_local):
        click.secho(f"Unable to locate file: {env_local}", fg="yellow")
        return

    config = dotenv_values(".env.local")
    mapping = {}
    if isfile(ctx.obj.amplify_cf_file):
        settings = json.load(open(ctx.obj.amplify_cf_file, "r"))
        mapping = settings.get("mapping", {})
        replace = settings.get("replace", {})

    variables = resolve_vars(mapping, ctx.obj.stack_variables())
    for key, value in config.items():
        value = value.strip()
        if key in variables:
            config[key] = variables[key]

        for regex, replace_with in replace.items():
            if re.search(regex, value, re.MULTILINE):
                config[key] = re.sub(regex, resolve_value(replace_with, ctx), value)

    with open(env_local, "w+") as f:
        for key, value in config.items():
            f.write(f"{key}={value}\n")
