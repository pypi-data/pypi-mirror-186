import click

from amplify_cf.config import config
from amplify_cf.ext import common_options
from amplify_cf.schema import update_models


@click.group()
def env():
    pass


@env.command()
@click.pass_context
@common_options
def switch(ctx):
    click.secho(f"Switching to new env: {ctx.obj.env} in {ctx.obj.region}", fg="blue")
    click.secho(f"Using stack: {ctx.obj.stack}")

    ctx.invoke(config)

    # API
    API = next(
        filter(
            lambda x: x.startswith("api") and "GraphQLAPIIdOutput" in ctx.obj.variables.get("root").get(x),
            ctx.obj.variables.get("root").keys(),
        ),
        None,
    )

    apiId = ctx.obj.variables.get("root").get(API).get("GraphQLAPIIdOutput")

    ctx.invoke(update_models, api=apiId)
