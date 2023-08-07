import click
import urllib
import requests
import os
from requests.exceptions import RequestException

import loci.utils as lcu
from loci.project import get_project_by_name_or_id
from loci.resources import SRC_README_MD


def login_and_get_api_key(server: str, email: str, password: str):
    lcu.print_info("Logging in with your credentials and obtaining an API Key."
                   " Any previous API keys will be invalidated.")

    # Auth via password over OAuth2.
    url = urllib.parse.urljoin(server, "/api/login")
    data = {"grant_type": "password", "username": email, "password": password}

    with lcu.working():
        r = requests.post(url, timeout=5, data=data)
    if r.ok:
        access_token = r.json()["access_token"]
        headers = {"Authorization": "Bearer " + access_token}
        url = urllib.parse.urljoin(server, "/api/users/me/apikey")
        with lcu.working():
            r = requests.post(url, timeout=5, json={}, headers=headers)

        if r.ok:
            key = r.json()["cleartext_key"]
            lcu.print_info("Saving Loci configuration.")
            lcu.write_loci_config_value("loci_server", server)
            lcu.write_loci_config_value("api_key", key)
            lcu.print_success("Loci configuration saved. Test it with the [bold]test[/bold] command.")
        else:
            lcu.print_error("The API key creation has failed."
                            " You can do this manually.", fatal=False)
            url = urllib.parse.urljoin(server, "/docs#/api_keys/create_my_apikey_api_users_me_apikey_post")
            lcu.print_error("See the docs at [bold]%s[/bold]." % url)
    else:
        lcu.print_error("The login process to obtain an API key has failed. You can do this manually.",
                        fatal=False)
        url = urllib.parse.urljoin(server, "/docs#/api_keys/create_my_apikey_api_users_me_apikey_post")
        lcu.print_error("See the docs at [bold]%s[/bold]." % url)


@click.group()
def setup():
    """Server and localhost setup commands"""
    pass


@setup.command()
@click.option("-s", "--server",
              prompt="Loci Server URL",
              help="Loci Server URL, in the form https://loci-api.example.com",
              required=True,
              type=str,
              default="http://localhost:5000",
              show_default=True)
@click.option("-e", "--email",
              prompt="User Email",
              help="Email of first user, who will be an administrator.",
              required=True,
              type=str)
@click.option("-n", "--name",
              prompt="User Name",
              help="Full name of first user.",
              required=True,
              type=str)
@click.option("-p", "--password",
              prompt="User Password",
              confirmation_prompt="Confirm Password",
              help="Password of first user.",
              required=True,
              hide_input=True)
def server(server, email, name, password):
    """Setup a new Loci Notes Server"""
    lcu.print_info("Setting up the Loci Server at [bold]%s[/bold] with [bold]%s[/bold] as an administrator." %
                   (server, email))

    data = {"email": email, "full_name": name, "password": password}

    url = urllib.parse.urljoin(server, "/api/setup")
    try:
        with lcu.working():
            r = requests.post(url, timeout=5, json=data)

        if r.ok:
            lcu.print_success("The Loci server has been setup successfully.")
            login_and_get_api_key(server, email, password)

        elif r.status_code == 400:
            lcu.print_error("The server at [bold]%s[/bold] has returned an error." % server, fatal=False)
            lcu.print_error("    Detail: " + r.json()["detail"])
        else:
            lcu.print_error("Unable to setup the server. Please review the server logs for more information.")
    except RequestException:
        lcu.print_error("The Loci server did not respond. Is the URL correct and the server at [bold]%s[/bold] running?"
                        % server)


@setup.command()
@click.option("-n", "--name",
              help="Project name or ID",
              default=None,
              type=str)
def localhost(name):
    """Setup this localhost for using the current directory"""
    lcu.print_info("Setting up and validating your local machine for Loci Notes usage.")

    lcu.print_info("Checking for a project in your current directory...")
    project_id, project_name = lcu.get_project_id_from_config_in_dir(os.getcwd(), check_parents=False)

    if project_id is None or project_name is None:
        # No project exists in the current directory, make a new one.
        if name is None or name == "":
            # No name or search param was entered on the command line, ask for it directly.
            lcu.print_info("No project found, enter the name or ID of the project to use in this directory.")
            name = click.prompt("Project name or ID")

        project = get_project_by_name_or_id(name)
        if project is None:
            lcu.print_error("Project search failed, enter a valid project, or create a new one.")
            return

        directory = os.getcwd()
        lcu.set_project_config_in_dir(project, directory)
        lcu.print_info("Set [bold]%s[/bold] to use [bold]%s[/bold]." % (directory, project["name"]))

        project_name = project["name"]
        project_id = project["id"]

    lcu.print_success(f"Using [bold]{project_name}[/bold] as the Loci Notes project.")

    if not os.path.isdir("_src"):
        if os.path.isfile("_src"):
            lcu.print_error("A [bold]_src[/bold] was found, but it appears to be a file, not a directory. "
                            "Rename or remove this file.")
            return
        lcu.print_info("The source code directory was not found, creating [bold]_src[/bold] automatically.")
        os.mkdir("_src")

    lcu.print_success("The [bold]_src[/bold] directory was found. Use this to store all source code related "
                      f"to [bold]{project_name}[/bold].")

    src_readme_path = os.path.join(os.getcwd(), "_src", "README.md")
    if not os.path.isfile(src_readme_path):
        lcu.print_info("Adding an informational README file to [bold]_src[/bold]...")
        with open(src_readme_path, "w") as fd:
            fd.write(SRC_README_MD)

    lcu.print_success(f"Your localhost is setup to use Loci Notes with [bold]{project_name}[/bold].")
