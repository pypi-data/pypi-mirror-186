import click

from loci.config import config, test, setup
from loci.user import user
from loci.project import project
from loci.project import list as project_list
from loci.artifact import artifact
from loci.artifact import status as artifact_status
from loci.artifact import list as artifact_list
from loci.note import note
from loci.note import new as note_new
from loci.note import list as note_list
import loci.utils as lcu


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    lcu.print_version()
    ctx.exit()


@click.group()
@click.option("-v", "--version", is_flag=True, callback=print_version, expose_value=False, is_eager=True)
def loci_cli():
    pass


loci_cli.add_command(config)
loci_cli.add_command(setup)
loci_cli.add_command(test)
loci_cli.add_command(user)
loci_cli.add_command(project)
loci_cli.add_command(artifact)
loci_cli.add_command(note)


@click.command()
@click.pass_context
@click.option("-a", "--artifact",
              prompt="Artifact",
              help="Artifact descriptor or ID",
              required=True,
              type=str)
@click.option("-s", "--status",
              prompt=False,
              help="Artifact status update",
              type=click.Choice(["DONE", "FLAG", "TODO"], case_sensitive=False))
def status(ctx, artifact, status):
    """Alias for `artifact status`"""
    ctx.forward(artifact_status, artifact=artifact, status=status)


loci_cli.add_command(status)


@click.command()
@click.pass_context
@click.option("-a", "--artifact",
              prompt="Artifact",
              help="Artifact descriptor",
              required=True,
              type=str)
@click.option("-t", "--note-type",
              prompt=False,
              help="Note type",
              required=True,
              default="comment",
              show_default=True,
              type=click.Choice(["comment", "log", "snapshot_txt"], case_sensitive=False))
@click.option("-T", "--tool",
              prompt=False,
              help="Tool submitting note",
              required=True,
              default="loci-cli",
              show_default=True,
              type=str)
@click.option("-c", "--contents",
              prompt="Contents",
              help="Note contents",
              required=True,
              type=str)
def new(ctx, artifact, note_type, tool, contents):
    """Alias for `note new`"""
    ctx.forward(note_new, artifact=artifact, note_type=note_type, tool=tool, contents=contents)


loci_cli.add_command(new)


@click.command()
@click.pass_context
@click.option("-a", "--artifact",
              prompt="Artifact",
              help="Artifact descriptor or ID",
              required=True,
              type=str)
def notes(ctx, artifact):
    """Alias for `note list`"""
    ctx.forward(note_list, artifact=artifact)


loci_cli.add_command(notes)


@click.command()
@click.pass_context
@click.option("-f", "--filter",
              prompt=False,
              help="Filter by artifact status",
              type=click.Choice(["DONE", "FLAG", "TODO"], case_sensitive=False))
@click.option("-q", "--query",
              prompt=False,
              help="Filter by artifact content",
              type=str)
def artifacts(ctx, filter, query):
    """Alias for `artifact list`"""
    ctx.forward(artifact_list, filter=filter, query=query)


loci_cli.add_command(artifacts)


@click.command()
@click.pass_context
def projects(ctx):
    """Alias for `project list`"""
    ctx.forward(project_list)


loci_cli.add_command(projects)


if __name__ == "__main__":
    loci_cli()
