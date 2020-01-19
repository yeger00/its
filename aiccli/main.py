#!/usr/bin/env python3

import click
import os
import yaml

class Issue(object):
    def __init__(self, id, title, labels = []):
        self.id = id
        self.title = title


class Aiccli(object):
    AICCLI_DIR_NAME = ".aiccli"
    ISSUES_FILE = "issues.yml"
    def __init__(self, path, create_db=False):
        if not self.is_aiccli(path):
            if not create_db:
                raise Exception("not a aiccli repo")
            else:
                self.dir_path = self.get_dir_path(path)
                os.mkdir(self.dir_path)
        else:
            if create_db:
                raise Exception("aiccli already exists")
            else:
                self.dir_path = self.get_dir_path(path)


    @classmethod
    def get_dir_path(cls, path):
        return os.path.join(path, cls.AICCLI_DIR_NAME)


    @classmethod
    def is_aiccli(cls, path):
        dir_path = cls.get_dir_path(path)
        return os.path.exists(dir_path)


    def issues(self):
        return YamlWrapper(os.path.join(self.dir_path, self.ISSUES_FILE))


class YamlWrapper(object):
    def __init__(self, path):
        self.path = path
        self.all_objects = {}
        if not os.path.exists(path):
            self.write_all()
        self.read_all()


    def get(self, id):
        print(self.all_objects)
        for i in self.all_objects:
            if i.id == id:
                return i


    def read_all(self):
        with open(self.path, "r") as f:
            self.all_objects = yaml.load(f)
    

    def write_all(self):
        with open(self.path, "w") as f:
            return yaml.dump(self.all_objects, f)


    def add(self, obj):
        all_objects.append(obj)
        write_all()


@click.group()
def cli():
    pass


@cli.command()
def init():
    Aiccli(os.getcwd(), True)
    click.echo('init')
    click.echo('mkdir .aiccli')


@cli.group()
@click.option('--id', type=int, required=False)
@click.pass_context
def issue(ctx, id):
    aiccli = Aiccli(os.getcwd(), False)
    issue = aiccli.issues().get(id)
    ctx.obj = (aiccli, issue)
    click.echo("issue: {id}".format(id=id))


@issue.command()
def new():
    click.echo("new")


@issue.command()
def list():
    click.echo("list")


@issue.group()
@click.pass_obj
def add(issue):
    pass


@add.command()
@click.argument('comment', type=str)
@click.pass_obj
def comment(issue, comment):
    click.echo("add to: {id}".format(id=issue.id))
    click.echo("comment: {comment}".format(comment=comment))


@add.command()
@click.argument('label', type=str)
@click.pass_obj
def label(issue, label):
    click.echo("add to: {id}".format(id=issue.id))
    click.echo("label: {label}".format(label=label))


if __name__ == '__main__':
    cli()
