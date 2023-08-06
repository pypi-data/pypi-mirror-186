import click

from .ext import Context
from .config import config
from .env import env
from .schema import schema


@click.group()
@click.pass_context
def cmd(ctx):
    ctx.obj = Context()


cmd.add_command(config)
cmd.add_command(schema)
cmd.add_command(env)
