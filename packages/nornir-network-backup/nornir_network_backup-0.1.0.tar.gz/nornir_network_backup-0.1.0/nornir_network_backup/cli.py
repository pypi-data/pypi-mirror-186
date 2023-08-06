import os

import click

from nornir_network_backup.nornir.backup import (
    nr_backup_single_host,
    nr_backup_many,
)


@click.group
def base():
    """Base entry for click"""


@click.command()
@click.argument("host")
@click.option(
    "-u",
    "--user",
    prompt=True,
    default=lambda: os.environ.get("USER", ""),
    type=str,
    required=True,
    help="Username",
)
@click.password_option(
    "-p",
    "--password",
    confirmation_prompt=False,
    type=str,
    required=True,
    help="Password",
)
@click.option(
    "--oneos",
    "driver",
    flag_value="oneaccess_oneos",
    help="Driver for OneAccess OneOS devices",
)
@click.option(
    "--ios-xe",
    "driver",
    flag_value="cisco_ios",
    help="Driver for Cisco IOS-XE devices",
)
@click.option(
    "--ios-xr",
    "driver",
    flag_value="cisco_xr",
    help="Driver for Cisco IOS-XR devices",
)
@click.option(
    "--saos",
    "driver",
    flag_value="ciena_saos",
    help="Driver for Ciena SAOS devices",
)
@click.option(
    "--regenerate-hosts",
    "regenerate_hosts",
    default=False,
    is_flag=True,
    help="Force the hosts.yaml file to be re-generated (requires NMAPDiscoveryInventory inventory plugin)",
)
@click.option(
    "--facts/--no-facts",
    "facts",
    default=True,
    help="Disable gathering extra facts",
)
@click.option(
    "-c",
    "--config-file",
    default="config.yaml",
    type=str,
    required=False,
    help="Specifiy the location of main nornir config file, default = config.yaml",
)
@click.option("-v", "--verbose", count=True)
def backup_single_host(
    host, user, password, driver, regenerate_hosts, facts, verbose, config_file
):
    """Backup a single host, especially useful if the device is not yet known in the inventory devices.yaml file
    because you can manually assigne the device driver.

    This command will always use the provided username + password, overriding any usernames or passwords defined in
    the configuration files.

    By default the hosts.yaml file is not re-generated if the NMAPDiscoveryInventory plugin is in use
    """
    click.echo(f"Start backup for a single host {host}")
    nr_backup_single_host(
        host,
        user,
        password,
        driver,
        regenerate_hostsfile=regenerate_hosts,
        gather_facts=facts,
        config_file=config_file,
    )


@click.command(name="backup")
@click.option(
    "-u",
    "--user",
    prompt=False,
    default=lambda: os.environ.get("USER", ""),
    type=str,
    required=False,
    help="Username",
)
@click.password_option(
    "-p",
    "--password",
    prompt=False,
    confirmation_prompt=False,
    type=str,
    required=False,
    help="Password",
)
@click.option(
    "--all",
    "all_hosts",
    default=False,
    is_flag=True,
    help="Take a backup of all hosts in the hosts.yaml inventory",
)
@click.option(
    "--host",
    "-h",
    "host_list",
    multiple=True,
    help="Take a backup of one host. This command can be repeated to include multiple hosts. The host has to exist in the inventory.",
)
@click.option(
    "--group",
    "-g",
    "group_list",
    multiple=True,
    help="Take a backup of all the hosts of one group. This command can be repeated to include multiple groups. The group has to exist in the inventory.",
)
@click.option(
    "--regenerate-hosts/--no-regenerate-hosts",
    "regenerate_hosts",
    default=None,
    help="Enable or disable re-generation of hosts.yaml file if the NMAPDiscoveryInventory inventory plugin is installed, this overrides the settings from the main config file",
)
@click.option(
    "--facts/--no-facts",
    "facts",
    default=None,
    help="Disable gathering extra facts, this overrides settings from the main config file",
)
@click.option(
    "-c",
    "--config-file",
    default="config.yaml",
    type=str,
    required=False,
    help="Specifiy the location of main nornir config file, default = config.yaml",
)
@click.option("-v", "--verbose", count=True)
def backup_many(
    all_hosts,
    host_list,
    group_list,
    user,
    password,
    regenerate_hosts,
    facts,
    verbose,
    config_file,
):
    """Backup many hosts. All hosts HAVE to exist in the hosts.yaml file and filters may be used on existing host or
    groups or you can provide a valid Nornir F() filter string.

    The username and password may be provided but they're not required, then can also be set in one of the configuration
    files or provided via environment variable.

    The hosts.yaml file will be regenerated automatically by default if the NMAPDiscoveryInventory inventory plugin is used.
    """

    if not (all_hosts or host_list or group_list):
        raise click.UsageError(
            "Please provide a host, group or nornir filter or explicitly add the --all parameter\n"
        )

    click.echo("Starting backup process")

    nr_backup_many(
        user,
        password,
        all_hosts=all_hosts,
        host_list=host_list,
        group_list=group_list,
        regenerate_hostsfile=regenerate_hosts,
        gather_facts=facts,
        config_file=config_file,
    )


base.add_command(backup_single_host)
base.add_command(backup_many)


if __name__ == "__main__":
    base()
