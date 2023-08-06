import click
import urllib
import requests
from requests.exceptions import RequestException

import loci.utils as lcu


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


@click.command()
@click.option("-s", "--server",
              prompt="Loci Server URL",
              help="Loci Server URL, in the form https://loci-api.example.com",
              required=True,
              type=str,
              default=lambda: lcu.get_loci_config_value("loci_server"))
@click.option("-e", "--email",
              prompt="User Email",
              help="Your user email.",
              required=True,
              type=str)
@click.option("-p", "--password",
              prompt="User Password",
              help="Your user password.",
              required=True,
              hide_input=True)
def config(server, email, password):
    """Configure this CLI tool"""
    lcu.print_info("Saving Loci configuration.")
    lcu.write_loci_config_value("loci_server", server)
    login_and_get_api_key(server, email, password)


@click.command()
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
def setup(server, email, name, password):
    """Setup a new Loci Server"""
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


@click.command()
def test():
    """Test connectivity to Loci server and CLI configuration"""
    if not lcu.is_loci_setup():
        lcu.print_error("Loci CLI has not been configured. Use the [bold]config[/bold] command.")
        return

    lcu.print_info("Testing Loci CLI configuration.")

    r = lcu.loci_api_req("/api/users/me")
    if r is not None:
        lcu.print_success("Loci configuration is good, you are logged in as [bold]%s[/bold]." % r["full_name"])
