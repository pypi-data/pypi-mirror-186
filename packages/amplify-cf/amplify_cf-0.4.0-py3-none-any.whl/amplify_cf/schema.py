import json
import os
import subprocess
from os import getcwd
from os.path import join, isdir, isfile, dirname

import boto3
import click
import inquirer as inquirer
import yaml
from mypy_boto3_appsync.client import AppSyncClient

from amplify_cf.ext import common_options


@click.group()
def schema():
    pass


def get_project_name():
    graphql_config_file = join(getcwd(), ".graphqlconfig.yml")
    raw_api_name = None
    if isfile(graphql_config_file):
        with open(graphql_config_file, "r") as f:
            graphql_config = yaml.load(f, Loader=yaml.Loader)
            raw_api_name = list(graphql_config.get("projects").keys())[0]

    return raw_api_name


def ensure_content(path, content, created_files, condition):
    if not condition:
        return

    dir = dirname(path)
    if not isdir(dir):
        created_files.append(dir)
        os.makedirs(dir)

    created_files.append(path)
    with open(path, "w+") as f:
        json.dump(content, f)


@schema.command(name="fetch")
@click.argument("api", required=False)
@common_options
@click.pass_obj
def fetch_schema(obj, api=None):
    try:
        appsync: AppSyncClient = boto3.client("appsync", region_name=obj.region)
    except:
        click.secho("Failed to obtain AWS credentials", fg="red")
        return 1

    if not api:
        apis = dict(map(lambda x: (x["name"], x["apiId"]), appsync.list_graphql_apis().get("graphqlApis", [])))
        questions = [
            inquirer.List(
                "api",
                message="Which API you would like to export?",
                choices=apis.keys(),
            ),
        ]
        answers = inquirer.prompt(questions)
        api_name = answers.get("api")
        api_id = apis.get(api_name)
    else:
        api_id = api

    raw_api_name = get_project_name()

    click.secho(f"Fetching schema for API: {api_id}", fg="green")
    schema = appsync.get_introspection_schema(apiId=api_id, format="SDL", includeDirectives=True)

    work_dir = getcwd()
    target_dir = join(work_dir, "amplify", "backend", "api", raw_api_name, "build")
    if not isdir(target_dir):
        os.makedirs(target_dir, exist_ok=True)

    target_file = join(target_dir, "schema.graphql")
    with open(target_file, "wb+") as f:
        f.write(schema.get("schema").read())

    click.secho(f"Saved schema to: {target_file}", fg="green")


@schema.command(name="update")
@click.argument("api", required=False)
@common_options
@click.pass_context
def update_models(ctx, api):
    result = ctx.invoke(fetch_schema, api=api)

    if result not in [0, None]:
        return result

    amplify_path = "./node_modules/.bin/amplify"
    if not isfile(amplify_path):
        click.secho("Missing local amplify installation. Trying with global", fg="yellow")
        amplify_path = "amplify"

    raw_api_name = get_project_name()

    created = []
    meta_file = "./amplify/backend/amplify-meta.json"
    ensure_content(
        meta_file,
        {"api": {raw_api_name: {"service": "AppSync", "providerPlugin": "awscloudformation", "output": {}}}},
        created,
        raw_api_name and not isfile(meta_file),
    )

    project_config_file = join(getcwd(), "amplify", ".config", "project-config.json")
    project_path = None
    if isfile(project_config_file):
        with open(project_config_file, "r+") as f:
            project_config = json.load(f)
            f.seek(0)
            project_path = project_config.get("projectPath", None)
            project_config["projectPath"] = getcwd()
            json.dump(project_config, f, indent=2)
    else:
        ensure_content(
            project_config_file,
            {
                "projectName": raw_api_name,
                "version": "3.1",
                "frontend": "javascript",
                "javascript": {
                    "framework": "none",
                    "config": {
                        "SourceDir": "src",
                        "DistributionDir": "dist",
                        "BuildCommand": "npm run-script build",
                        "StartCommand": "npm run-script start",
                    },
                },
                "providers": ["awscloudformation"],
            },
            created,
            True,
        )

    ensure_content("./schema.json", {}, created, not isfile("./schema.json"))

    local_env = "./amplify/.config/local-env-info.json"
    ensure_content(
        local_env, {"defaultEditor": "none", "envName": "base", "projectPath": "./"}, created, not isfile(local_env)
    )

    subprocess.call([amplify_path, "codegen"], env=os.environ)

    for f in reversed(created):
        if isfile(f):
            os.unlink(f)
        else:
            os.rmdir(f)

    if isfile(project_config_file) and project_path is not None:
        with open(project_config_file, "r+") as f:
            project_config = json.load(f)
            project_config["projectPath"] = project_path
            f.seek(0)
            json.dump(project_config, f, indent=2)
