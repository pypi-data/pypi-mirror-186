import click

import loci.utils as lcu
from loci.setup import login_and_get_api_key


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
def test():
    """Test connectivity to Loci server and CLI configuration"""
    if not lcu.is_loci_setup():
        lcu.print_error("Loci CLI has not been configured. Use the [bold]config[/bold] command.")
        return

    lcu.print_info("Testing Loci CLI configuration.")

    r = lcu.loci_api_req("/api/users/me")
    if r is not None:
        lcu.print_success("Loci configuration is good, you are logged in as [bold]%s[/bold]." % r["full_name"])
