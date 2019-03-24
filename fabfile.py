# -*- coding: utf-8 -*-

from boto3 import client as aws
from fabric.api import cd
from fabric.api import env
from fabric.api import execute
from fabric.api import parallel
from fabric.api import run
from fabric.api import runs_once
from fabric.api import sudo
from fabric.api import task
from fabric.contrib import files as remote_files
from fabric.colors import blue
from fabric.colors import red
from git import Repo


repository = Repo('.')
GIT_BRANCH = '%s' % repository.head.ref
GIT_DIR = '/home/ubuntu/IA-backend-test'
WORK_DIR = '/home/ubuntu/IA-backend-test'
AWS_ACCESS_KEY = "AKIAIMIX7A3JY5EQ4GHA"
AWS_SECRET_KEY = "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"
AWS_REGION = "us-east-2"
env.user = 'ubuntu'
env.key_filename = 'ec2-ia-test.pem'


@task
def where():

    aws__hosts()
    print(env.hosts)


@task
@parallel
def deploy():
    aws__hosts()
    print(blue("Updating instance...", bold = True))
    execute(pull)
    execute(dependencies)
    execute(supervisorctl)
    print(blue("Deployed integrations", bold = True))


@task
@runs_once
def aws__hosts():

    print(red("Obtaining instances ...", bold = True))
    env.hosts = _aws_filter_by_tags()
    print(red("Obtained instances", bold = True))


def _aws_filter_by_tags():

    print(red("Filtering instances in the config regions..."))
    DNS = []
    connection = _aws_create_connection()
    instances = connection.describe_instances()
    for reservation in instances["Reservations"]:
        for instance in reservation["Instances"]:
            if instance['State']['Name'] == 'running':
                DNS.append(str(instance["PublicIpAddress"]))
    print(red("Filtered instances by tags"))
    return DNS


def _aws_create_connection():

    print(red("Connecting to AWS in %s ..." % AWS_REGION))
    connection = aws(
        'ec2',
        aws_access_key_id = AWS_ACCESS_KEY,
        aws_secret_access_key = AWS_SECRET_KEY,
        region_name = AWS_REGION
    )
    print(red("Connection with AWS in %s established" % AWS_REGION))
    return connection


@task
@parallel
def pull():
    with cd(GIT_DIR):
        print(blue("Pulling changes..."))
        run("git checkout %s && git pull origin %s" % (GIT_BRANCH, GIT_BRANCH))
        print(blue("Pulled changes"))


@task
@parallel
def dependencies():
    with cd(GIT_DIR):
        if remote_files.exists("requirements.txt"):
            if not remote_files.exists("venv/"):
                print(blue("Creating venv ..."))
                run("python3 -m venv venv")
                print(blue("Created venv"))
            print(blue("Installing dependencies..."))
            run("source venv/bin/activate && pip install -r requirements.txt")
            print(blue("Installed dependencies"))


@task
@parallel
def supervisorctl():

    print(blue("Restarting supervisor..."))
    sudo("supervisorctl restart app")
    print(blue("Restarted supervisor"))
    sudo("supervisorctl status")

