import os
import click
import rich
from rich.table import Table

import loci.utils as lcu
from loci.user import get_user_by_name_or_id


def get_project_by_name_or_id(name_or_id):
    lcu.print_info("Getting project information...")
    r = lcu.loci_api_req("/api/projects", method="GET")
    if r is not None:
        search_by_id = False
        try:
            # Try to turn the input into an int
            input_id = int(name_or_id)
            search_by_id = True
        except ValueError:
            search_by_id = False

        if not search_by_id:
            possible_projects = []
            for project in r:
                if name_or_id in project["name"]:
                    possible_projects.append(project)

            if len(possible_projects) > 1:
                lcu.print_error("The name [bold]%s[/bold] matches several projects. "
                                "Be more specific." % name_or_id)
                return None
            elif len(possible_projects) == 0:
                lcu.print_error("The name [bold]%s[/bold] did not match any projects. " % name_or_id)
                return None
            else:
                return possible_projects[0]

        else:
            for project in r:
                # Find the correct project
                if input_id == project["id"]:
                    return project
            lcu.print_error(f"Failed to retrieve project ID {input_id}.")
            return None
    else:
        lcu.print_error("Failed to retrieve project information.")
        return None


@click.group()
def project():
    """Project management commands"""
    pass


@project.command()
def list():
    """Show all projects"""
    r = lcu.loci_api_req("/api/projects")
    if r is not None:
        r.sort(key=lambda x: x["creation_time"])

        table = Table(show_header=True, header_style="bold")
        table.add_column("ID", style="dim", justify="right")
        table.add_column("Name", style="", justify="left")
        table.add_column("Access", style="", justify="right")
        table.box = rich.box.SIMPLE_HEAD

        for project in r:
            table.add_row(str(project["id"]),
                          project["name"],
                          "[green bold]\u2713[/green bold]" if project["have_access"] else " ")

        lcu.console.print(table)


@project.command()
@click.option("-n", "--name",
              prompt="Name",
              help="New project name",
              required=True,
              type=str)
@click.option("-s", "--set-dir",
              prompt=False,
              help="Automatically set current dir to use new project",
              default=False,
              required=True,
              type=bool)
@click.pass_context
def new(ctx, name, set_dir):
    """Create a new project"""
    lcu.print_info("Creating new project.")
    r = lcu.loci_api_req("/api/projects", method="POST", data={"name": name})
    if r is not None:
        lcu.print_success("New project [bold]%s[/bold] created successfully." % name)

        if set_dir:
            ctx.invoke(set, name=name)


@project.command()
@click.option("-n", "--name",
              prompt="Name or ID",
              help="Project name or ID to update",
              required=True,
              type=str)
def update(name):
    """Update a project"""
    old_project = get_project_by_name_or_id(name)
    if old_project is None:
        return

    try:
        project_updates = {}
        new_name = click.prompt("Name", default=old_project["name"], type=str)
        project_updates["name"] = new_name

        r = lcu.loci_api_req("/api/projects/" + str(old_project["id"]), method="PUT", data=project_updates)
        if r is not None:
            lcu.print_success("[bold]%s[/bold] updated successfully." % r["name"])
            return
        else:
            lcu.print_error("Project update was unsuccessful.")
            return
    except click.Abort:
        lcu.print_error("Project update cancelled.")
        return


@project.command()
@click.option("-n", "--name",
              prompt="Name or ID",
              help="Project name or ID to delete",
              required=True,
              type=str)
def delete(name):
    """Delete a project"""
    old_project = get_project_by_name_or_id(name)
    if old_project is None:
        return

    r = lcu.loci_api_req("/api/projects/" + str(old_project["id"]), method="DELETE")
    if r is not None:
        lcu.print_success("[bold]%s[/bold] deleted successfully." % old_project["name"])
        return
    else:
        lcu.print_error("Project deletion was unsuccessful.")
        return


@project.command()
def get():
    """Get the current configured project for the current working directory"""
    project_id, project_name = lcu.get_project_id_from_config_in_dir(os.getcwd())

    if project_id is None or project_name is None:
        lcu.print_error("There is no project associated with this directory.")
        return
    lcu.print_success("Currently working in [bold]%s[/bold]." % (project_name))


@project.group()
def access():
    """Project access management commands"""
    pass


@access.command()
@click.option("-n", "--name",
              prompt="Name or ID",
              help="Project name or ID",
              required=True,
              type=str)
def show(name):
    """Show current user access to project"""
    project = get_project_by_name_or_id(name)
    if project is None:
        return

    r = lcu.loci_api_req(f"/api/projects/{project['id']}", method="GET")
    if r is None:
        return

    project = r

    table = Table(show_header=True, header_style="bold")
    table.add_column("ID", style="dim", justify="right")
    table.add_column("Name", style="", justify="left")
    table.add_column("Manager", style="", justify="right")
    table.box = rich.box.SIMPLE_HEAD

    for manager in project["managers"]:
        table.add_row(str(manager["id"]), manager["full_name"], "[green bold]\u2713[/green bold]")

    for user in project["users"]:
        table.add_row(str(user["id"]), user["full_name"], "")

    lcu.console.print(table)


@access.command()
@click.option("-n", "--name",
              prompt="Name or ID",
              help="Project name or ID",
              required=True,
              type=str)
@click.option("-u", "--user",
              prompt="User name or ID",
              help="User name or ID",
              required=True,
              type=str)
@click.option('--manager/--no-manager', default=False)
def add(name: str, user: str, manager: bool):
    """Grant a user project access"""
    project = get_project_by_name_or_id(name)
    if project is None:
        return

    user = get_user_by_name_or_id(user)
    if user is None:
        return

    body = {
        "user_id": user["id"],
        "is_manager": manager
    }

    r = lcu.loci_api_req(f"/api/projects/{project['id']}/access", method="POST", data=body)
    if r is not None:
        if manager:
            lcu.print_success(f"[bold]{user['full_name']}[/bold] was granted manager access "
                              "to [bold]{project['name']}[/bold].")
            return
        else:
            lcu.print_success(f"[bold]{user['full_name']}[/bold] was granted user access to "
                              "[bold]{project['name']}[/bold].")
            return
    else:
        lcu.print_error(f"[bold]{user['full_name']}[/bold] was not granted access.")
        return


@access.command()
@click.option("-n", "--name",
              prompt="Name or ID",
              help="Project name or ID",
              required=True,
              type=str)
@click.option("-u", "--user",
              prompt="User name or ID",
              help="User name or ID",
              required=True,
              type=str)
def rm(name: str, user: str):
    """Remove a user's project access"""
    project = get_project_by_name_or_id(name)
    if project is None:
        return

    user = get_user_by_name_or_id(user)
    if user is None:
        return

    # Get the project access list
    r = lcu.loci_api_req(f"/api/project/{project['id']}/access", method="GET")
    if r is not None:
        access_id = None
        for access in r:
            if access["user_id"] == user["id"]:
                access_id = access["id"]
                break
        if access_id:
            r = lcu.loci_api_req(f"/api/project_access/{access_id}", method="DELETE")
            if r is None:
                lcu.print_error(f"[bold]{user['full_name']}[/bold]'s access could not be removed.")
            else:
                lcu.print_success(f"Removed [bold]{user['full_name']}[/bold]'s access to "
                                  "[bold]{project['name']}[/bold].")
        else:
            lcu.print_error(f"[bold]{user['full_name']}[/bold] does not have access to "
                            "[bold]{project['name']}[/bold].")


project.add_command(access)
