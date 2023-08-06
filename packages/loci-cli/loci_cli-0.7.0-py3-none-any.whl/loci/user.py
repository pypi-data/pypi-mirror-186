import click
import rich
from rich.table import Table

import loci.utils as lcu


def get_user_by_name_or_id(name_or_id):
    lcu.print_info("Getting user information.")
    r = lcu.loci_api_req("/api/users", method="GET")
    if r is not None:
        search_by_id = False
        try:
            # Try to turn the input into an int
            input_id = int(name_or_id)
            search_by_id = True
        except ValueError:
            search_by_id = False

        if not search_by_id:
            possible_users = []
            for user in r:
                if name_or_id in user["full_name"]:
                    possible_users.append(user)
                elif name_or_id in user["email"]:
                    possible_users.append(user)

            if len(possible_users) > 1:
                lcu.print_error("The name [bold]%s[/bold] matches several users. "
                                "Please give a more specific identifier." % name_or_id)
                return None
            elif len(possible_users) == 0:
                lcu.print_error("The name [bold]%s[/bold] did not match any users. " % name_or_id)
                return None
            input_id = possible_users[0]["id"]

        for user in r:
            # Find the correct user
            if input_id == user["id"]:
                return user
        lcu.print_error("User could not be found.")
        return None
    else:
        lcu.print_error("Failed to retrieve user information.")
        return None


@click.group()
def user():
    """User management commands"""
    pass


@user.command()
def list():
    """Show all users"""
    r = lcu.loci_api_req("/api/users")
    if r is not None:
        r.sort(key=lambda x: x["id"])

        table = Table(show_header=True, header_style="bold")
        table.add_column("ID", style="dim", justify="right")
        table.add_column("Name", style="", justify="left")
        table.add_column("Active", style="", justify="right")
        table.box = rich.box.SIMPLE_HEAD

        for user in r:
            table.add_row(str(user["id"]),
                          user["full_name"],
                          "[green bold]\u2713[/green bold]" if user["is_active"] else " ")

        lcu.console.print(table)


@user.command()
@click.option("-e", "--email",
              prompt="User Email",
              help="Email of new user.",
              required=True,
              type=str)
@click.option("-n", "--name",
              prompt="User Name",
              help="Full name of new user.",
              required=True,
              type=str)
@click.option("-p", "--password",
              prompt="User Password",
              confirmation_prompt="Confirm Password",
              help="Password of new user.",
              required=True,
              hide_input=True)
def new(email, name, password):
    """Create a new user"""
    lcu.print_info("Creating new user.")
    r = lcu.loci_api_req("/api/users", method="POST",
                         data={"email": email, "full_name": name, "password": password})
    if r is not None:
        lcu.print_success("New user [bold]%s[/bold] created successfully." % name)


@user.command()
@click.option("-n", "--name",
              prompt="Name or ID",
              help="User name, email, or ID to update",
              required=True,
              type=str)
def update(name):
    """Update a user"""
    user = get_user_by_name_or_id(name)
    if user is None:
        return

    try:
        user_updates = {}
        prompt_input = click.prompt("User Email", default=user["email"], type=str)
        user_updates["email"] = prompt_input

        prompt_input = click.prompt("User Name", default=user["full_name"], type=str)
        user_updates["full_name"] = prompt_input

        prompt_input = click.prompt("Update Password?",
                                    type=click.Choice(["y", "n"], case_sensitive=False), default="n")

        if prompt_input == "y":
            prompt_input = click.prompt("User Password",
                                        type=str,
                                        hide_input=True,
                                        confirmation_prompt="Confirm Password")
            user_updates["password"] = prompt_input

        r = lcu.loci_api_req("/api/users/" + str(user["id"]), method="PUT", data=user_updates)
        if r is not None:
            lcu.print_success("[bold]%s[/bold] updated successfully." % r["full_name"])
            return
        else:
            lcu.print_error("User update was unsuccessful.")
            return
    except click.Abort:
        lcu.print_error("User update cancelled.")
        return


@user.command()
@click.option("-n", "--name",
              prompt="Name or ID",
              help="User name, email, or ID to update",
              required=True,
              type=str)
def delete(name):
    """Delete a user"""
    user = get_user_by_name_or_id(name)
    if user is None:
        return

    r = lcu.loci_api_req("/api/users/" + str(user["id"]), method="DELETE")
    if r is not None:
        lcu.print_success("[bold]%s[/bold] deleted successfully." % user["full_name"])
        return
    else:
        lcu.print_error("User deletion was unsuccessful.")
        return
