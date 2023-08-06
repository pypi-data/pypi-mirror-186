import json
from os import getenv, getcwd
from os.path import isfile, join

import boto3
import click
import inquirer
from mypy_boto3_cloudformation import CloudFormationClient

from amplify_cf.utils import get_stack_outputs


class Context(object):
    def __init__(self):
        self.region = "us-east-1"
        self.env = None
        self._stack = None
        self._variables = {}

    @property
    def amplify_cf_file(self):
        return join(getcwd(), ".amplify-cf")

    @property
    def stack(self):
        if not self._stack:
            self._stack = self.resolve_stack()

        return self._stack

    @property
    def variables(self):
        if not self._variables:
            self._variables = self.stack_variables()

        return self._variables

    def resolve_env(self, env):
        env = env or getenv("AWS_VAULT", getenv("AWS_PROFILE"))
        if "-" in (env or ""):
            env = env.split("-")[1]

        return env

    def resolve_region(self, region):
        region = region or getenv("AWS_DEFAULT_REGION", "us-east-1")

        return region

    def resolve_stack(self):
        config = {}
        if isfile(self.amplify_cf_file):
            config = json.loads(open(self.amplify_cf_file, "r").read())

            stack = config.get("stack").format(env=self.env, region=self.region)
        else:
            cf: CloudFormationClient = boto3.client("cloudformation", region_name=self.region)
            paginator = cf.get_paginator("list_stacks")

            amplify_file = join("amplify", ".config", "project-config.json")

            amplify = json.loads(open(amplify_file, "r").read())
            stack_prefix = "-".join(["amplify", amplify.get("projectName").lower(), self.env])

            matches = []
            for page in paginator.paginate(
                StackStatusFilter=["CREATE_COMPLETE", "UPDATE_COMPLETE"], PaginationConfig={"MaxItems": 500}
            ):
                for stack in page["StackSummaries"]:
                    if stack_prefix not in stack.get("StackName"):
                        continue
                    if stack.get("StackName").startswith(stack_prefix) and stack.get("ParentId") is None:
                        matches.append(stack.get("StackName"))

            if len(matches) > 1:
                questions = [
                    inquirer.List(
                        "stack",
                        message="Which stack would you like to use for env setup?",
                        choices=matches,
                    ),
                ]
                stack = inquirer.prompt(questions).get("stack")
            else:
                stack = matches[0]

        return stack

    def stack_variables(self):
        return get_stack_outputs(stack_name=self.resolve_stack(), region=self.region)


def region_option(f):
    def callback(ctx, param, value):
        state = ctx.ensure_object(Context)
        state.region = ctx.obj.resolve_region(value)
        return value

    return click.option("-r", "--region", expose_value=False, help="AWS Region", callback=callback)(f)


def env_option(f):
    def callback(ctx, param, value):
        state = ctx.ensure_object(Context)
        state.env = ctx.obj.resolve_env(value)
        return value

    return click.option("-e", "--env", expose_value=False, help="Environment", callback=callback)(f)


def common_options(f):
    f = region_option(f)
    f = env_option(f)
    return f
