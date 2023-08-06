import os
import click
import rich
from rich.table import Table

import loci.utils as lcu
from loci.project import get_project_by_name_or_id


def get_artifact_by_name_or_id(project_id, name_or_id):
    lcu.print_info("Getting artifact information.")
    r = lcu.loci_api_req("/api/projects/%d/artifacts" % project_id, method="GET")
    if r is not None:
        search_by_id = False
        try:
            # Try to turn the input into an int
            input_id = int(name_or_id)
            search_by_id = True
        except ValueError:
            search_by_id = False

        if not search_by_id:
            possible_artifacts = []
            for artifact in r:
                if name_or_id in artifact["descriptor"]:
                    possible_artifacts.append(artifact)

            if len(possible_artifacts) > 1:
                lcu.print_error("The descriptor [bold]%s[/bold] matches several artifacts. "
                                "Please give a more specific identifier." % name_or_id)
                return None
            elif len(possible_artifacts) == 0:
                lcu.print_error("The descriptor [bold]%s[/bold] did not match any artifacts. " % name_or_id)
                return None
            input_id = possible_artifacts[0]["id"]

        for artifact in r:
            # Find the correct artifact
            if input_id == artifact["id"]:
                return artifact

        lcu.print_error("Artifact not found.")
    else:
        lcu.print_error("Failed to retrieve artifact information.")
        lcu.print_error("    Details: [bold]%s[/bold]" % r.json()["detail"])
        return None


def get_project_info():
    project_id, project_name = lcu.get_project_id_from_config_in_dir(os.getcwd())

    if project_id is None:
        lcu.print_warning("There is no project associated with this directory, use [bold]loci project set[/bold] "
                          "to automatically set project working folders.")
        project_str = click.prompt("Project name or ID", type=str)
        project = get_project_by_name_or_id(project_str)

        if project is None:
            # We should already have an error printed for the user from get_project_by_name_or_id().
            return None, None

        project_id = int(project["id"])
        project_name = project["name"]
    return project_id, project_name


def get_status_style(status):
    if status.upper() == "TODO":
        return "[bold yellow]TODO[/bold yellow]"
    if status.upper() == "DONE":
        return "[bold green]DONE[/bold green]"
    if status.upper() == "FLAG":
        return "[bold red]FLAG[/bold red]"


@click.group()
def artifact():
    """artifact management commands"""
    pass


@artifact.command()
@click.option("-f", "--filter",
              prompt=False,
              help="Filter by artifact status",
              type=click.Choice(["DONE", "FLAG", "TODO"], case_sensitive=False))
@click.option("-q", "--query",
              prompt=False,
              help="Filter by artifact content",
              type=str,
              default=None)
def list(filter, query):
    """Show all project artifacts"""
    project_id, project_name = get_project_info()
    lcu.print_info("Project: [bold]%s[/bold]." % project_name)

    if query:
        r = lcu.loci_api_req("/api/projects/%d/artifacts" % project_id, params={"q": query})
    else:
        r = lcu.loci_api_req("/api/projects/%d/artifacts" % project_id)

    if r is not None:
        r.sort(key=lambda x: x["id"])

        table = Table(show_header=True, header_style="bold")
        table.add_column("ID", style="dim", justify="right")
        table.add_column("Status", style="", justify="left")
        table.add_column("Descriptor", style="", justify="left")
        table.box = rich.box.SIMPLE_HEAD

        for artifact in r:
            if filter:
                if artifact["status"].upper() == filter.upper():
                    table.add_row(str(artifact["id"]),
                                  get_status_style(artifact["status"]),
                                  artifact["descriptor"],)
            else:
                table.add_row(str(artifact["id"]),
                              get_status_style(artifact["status"]),
                              artifact["descriptor"],)
        lcu.console.print(table)


@artifact.command()
@click.option("-a", "--artifact",
              prompt="artifact",
              help="Artifact descriptor or ID",
              required=True,
              type=str)
@click.option("-s", "--status",
              prompt=False,
              help="Artifact status update",
              type=click.Choice(["DONE", "FLAG", "TODO"], case_sensitive=False))
def status(artifact, status):
    """Show or change the status of a artifact"""
    project_id, project_name = get_project_info()
    lcu.print_info("Project: [bold]%s[/bold]." % project_name)

    artifact = get_artifact_by_name_or_id(project_id, artifact)
    if artifact is None:
        return

    lcu.print_info("[%d] '[bold]%s[/bold]' is %s." %
                   (artifact["id"], artifact["descriptor"], get_status_style(artifact["status"])))

    try:
        # See if the user wants to update the status
        if not status:
            new_status = click.prompt(
                    "Set status",
                    default=artifact["status"].upper(),
                    type=click.Choice(["DONE", "FLAG", "TODO"], case_sensitive=False))
        else:
            new_status = status

        if not new_status.upper() == artifact["status"].upper():
            artifact_updates = {}
            artifact_updates["status"] = new_status.upper()

            r = lcu.loci_api_req("/api/artifacts/%d" % artifact["id"], method="PUT", data=artifact_updates)
            if r is not None:
                lcu.print_success("[%d] '[bold]%s[/bold]' is %s." %
                                  (artifact["id"], artifact["descriptor"], get_status_style(new_status.upper())))
                return
            else:
                lcu.print_error("Status update was unsuccessful.")
                return
    except click.Abort:
        return
