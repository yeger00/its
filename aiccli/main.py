import click


class Issue(object):
    def __init__(self, id, title, labels = []):
        self.id = id
        self.title = title
        self.labels = labels


@click.group()
def cli():
    pass


@cli.command()
def init():
    click.echo('init')
    click.echo('mkdir .aiccli')


@cli.group()
@click.option('--id', type=int, required=False)
@click.pass_context
def issue(ctx, id):
    ctx.obj = Issue(id)
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
