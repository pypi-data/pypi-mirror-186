import click
import rich
from rich.table import Table
import pendulum


import loci.utils as lcu
from loci.artifact import get_artifact_by_name_or_id, get_project_info


@click.group()
def note():
    """Note management commands"""
    pass


@note.command()
@click.option("-a", "--artifact",
              prompt="Artifact",
              help="Artifact descriptor or ID",
              required=True,
              type=str)
def list(artifact):
    """Show all notes for a project artifact"""
    project_id, project_name = get_project_info()
    if project_id is None or project_name is None:
        return

    lcu.print_info("Project: [bold]%s[/bold]." % project_name)

    artifact_obj = get_artifact_by_name_or_id(project_id, artifact)
    if artifact_obj is None:
        return

    lcu.print_info("[%d] '[bold]%s[/bold]'" % (artifact_obj["id"], artifact_obj["descriptor"]))

    r = lcu.loci_api_req("/api/artifacts/%d/notes" % artifact_obj["id"])
    if r is not None:
        r.sort(key=lambda x: x["creation_time"], reverse=False)

        table = Table(show_header=True, header_style="bold", leading=10)
        table.add_column("ID", style="dim", justify="right")
        table.add_column("Author", style="", justify="left")
        table.add_column("Created", style="", justify="left")
        table.add_column("Tool", style="", justify="left")
        table.add_column("Type", style="", justify="left")
        table.add_column("Contents", style="", justify="left")
        table.box = rich.box.SIMPLE_HEAD

        for note in r:
            natural_time = pendulum.parse(note["creation_time"]).diff_for_humans()
            table.add_row(str(note["id"]),
                          note["user"]["full_name"],
                          natural_time,
                          note["submission_tool"],
                          note["note_type"],
                          note["contents"])

        lcu.console.print(table)


@note.command()
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
              type=click.Choice(["comment", "log", "snapshot_txt", "link"], case_sensitive=False))
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
def new(artifact, note_type, contents, tool):
    """Add a new note to the project"""
    project_id, project_name = get_project_info()
    if project_id is None or project_name is None:
        return

    lcu.print_info("Project: [bold]%s[/bold]." % project_name)

    new_note = {}
    new_note["artifact_descriptor"] = artifact
    new_note["submission_tool"] = tool
    new_note["note_type"] = note_type.upper()
    new_note["contents"] = contents

    r = lcu.loci_api_req("/api/projects/%d/notes" % project_id, method="POST", data=new_note)
    if r is not None:
        lcu.print_success("Note created successfully.")


def get_note_by_id(ctx, param, note_id: int):
    if not note_id or ctx.resilient_parsing:
        return

    ctx.ensure_object(dict)
    lcu.print_info("Getting note information.")
    r = lcu.loci_api_req("/api/notes/%d" % note_id, method="GET")
    if r is not None:
        ctx.obj["note_id"] = r["id"]
        ctx.obj["note_contents"] = r["contents"]
        return r
    else:
        lcu.print_error("Failed to retrieve note information.", fatal=False)
        lcu.print_error("    Details: [bold]%s[/bold]" % r.json()["detail"])
        ctx.exit()


@note.command()
@click.pass_context
@click.option("-n", "--note",
              prompt="Note ID",
              help="Note ID",
              required=True,
              type=int,
              callback=get_note_by_id,
              is_eager=True)
@click.option("-c", "--contents",
              prompt="Note Contents",
              help="Note Contents",
              required=True,
              type=str,
              cls=lcu.default_from_context("note_contents"))
def edit(ctx, note, contents):
    project_id, project_name = get_project_info()
    if project_id is None or project_name is None:
        return

    note_update = {}
    note_update["contents"] = contents

    lcu.print_info("Updating note information...")
    r = lcu.loci_api_req("/api/notes/%d" % note["id"], method="PUT", data=note_update)
    if r is not None:
        lcu.print_success("Note updated.")
        return
