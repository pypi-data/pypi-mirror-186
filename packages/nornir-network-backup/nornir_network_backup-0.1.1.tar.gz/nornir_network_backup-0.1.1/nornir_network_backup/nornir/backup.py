import datetime
import json
import logging
from pathlib import Path

import ruamel.yaml
from nornir import InitNornir
from nornir.core.filter import F
from nornir.core.inventory import Host
from nornir.core.plugins.inventory import (
    InventoryPluginRegister,
    TransformFunctionRegister,
)
from nornir.core.task import MultiResult, Result, Task
from nornir_netmiko import netmiko_send_command
from nornir_utils.plugins.tasks.files import write_file

# from nornir_utils.plugins.inventory.transform_functions import load_credentials

# from nornir_network_backup.nornir.plugins.processors import BackupReporter
from nornir_network_backup.nornir.config import init_user_defined_config
from nornir_network_backup.nornir.plugins.inventory import (
    NMAPDiscoveryInventory,
)
from nornir_network_backup.nornir.plugins.inventory.transform_functions import (
    load_credentials,
)
from nornir_network_backup.nornir.utils import (
    fact_to_yml,
    generate_comment,
    generate_filename,
    remove_file,
)

# logging.basicConfig(filename="netmiko_global.log", level=logging.DEBUG)
# logger = logging.getLogger("netmiko")

logger = logging.getLogger("nornir_network_backup")


def task_get_facts(task: Task, user_config: dict, **kwargs) -> Result:
    commands = get_fact_commands(task.host)

    facts = {
        "all_commands": [],
        "failed_commands": [],
        "success_commands": [],
        "failed": False,
    }

    for cmd in commands:
        cmd_nice = cmd.replace(" ", "_").replace("|", "_")
        facts["all_commands"].append(cmd)

        output = task.run(
            name=f"fact_netmiko_send_command_{cmd_nice}",
            task=netmiko_send_command,
            command_string=cmd,
            use_textfsm=user_config["textfsm"]["enabled"],
            # severity_level=logging.DEBUG,
        )

        if output.failed:
            facts["failed_commands"].append(cmd)

        else:
            facts["success_commands"].append(cmd)

            content, extension = fact_to_yml(output.result)

            fact_file = generate_filename(
                filetype="fact",
                hostname=task.host,
                user_config=user_config,
                command=cmd,
                extension=extension,
            )

            if not output.result:
                remove_file(fact_file)
                continue

            task.run(
                task=write_file,
                filename=fact_file,
                content=f"{content}",
            )

    # save the result to the inventory Host object
    # facts = {"all_commands": [], "failed_commands": [], "success_commands": []}
    facts["total_commands"] = len(facts["all_commands"])
    facts["total_failed_commands"] = len(facts["failed_commands"])
    facts["total_success_commands"] = len(facts["success_commands"])
    facts["failed"] = True if facts["failed_commands"] else False

    task.host.data.setdefault("_backup_results", {}).setdefault("facts", facts)

    return Result(host=task.host, result=facts)
    # return Result(host=task.host, result=facts, failed=failed)


def _extract_fact_from_result(result, wanted_summary_facts):
    """checks all the results to see if we should extract something for the summary facts"""
    if type(result) is list:
        for entry in result:
            for rc in _extract_fact_from_result(entry, wanted_summary_facts):
                yield rc

    if type(result) is dict:
        for key in wanted_summary_facts.keys():
            if key in result:
                value = result[key]
                if not value:
                    continue
                if type(value) is list:
                    value = "|".join(value)
                yield [key.upper(), value]


def get_summary_facts(
    results: MultiResult, host: Host, wanted_summary_facts: dict
) -> dict:
    """Get summary facts from all the previous 'show' results of all the tasks
    with name "fact_netmiko_send_command"

    We'll check the fact output results first, afterwards we'll check the host
    data fields (fact info has priority)

    "summary" facts are pre-defined keywords in the nornir configuration file and
    these will be added on top of the backup configuration file as comments. Only
    the facts that are found in the output fatcs commands will be displayed

    Example config backup file

        !
        ! ### START OF CONFIG ###
        !
        ! BOOT_VERSION: BOOT16-SEC-V3.4R3E40C
        ! DEVICE: LBB_140
        ! HOSTNAME: dops-lab-02
        ! MAC: 70:FC:8C:07:22:CC
        ! RELOAD_REASON: Power Fail detection
        ! SERIAL: T1703006230033175
        ! SOFTWARE: ONEOS16-MONO_FT-V5.2R2E7_HA8
        !
        Building configuration...

        Current configuration:

        !
        bind ssh Dialer 1
        bind ssh Loopback 1
        !

    """
    have_summary_facts = {}

    for r in results:
        if not r.name.startswith("fact_netmiko_send_command") or r.failed:
            continue

        for res in _extract_fact_from_result(r.result, wanted_summary_facts):
            # print(res)
            # print(type(res))
            if res:
                have_summary_facts[res[0]] = res[1]

        # print(r.result)
        # print(r.name)
        # print(type(r.result))
        # print(r.result)
        # print(f"failed: {r.failed}")

    # find missing wanted facts in the hosts.yaml file
    missing_wanted_facts = [
        key.lower()
        for key in wanted_summary_facts.keys()
        if key.upper() not in have_summary_facts.keys()
    ]
    # print(f"MISSING WANTED KEYS:{missing_wanted_facts}")

    for key in missing_wanted_facts:
        # print(f"KEY:{key}")
        if key in host.data:
            value = host.data[key]
            if not value:
                continue
            if type(value) is list:
                value = "|".join(value)
            have_summary_facts[key.upper()] = value

    # for key in host.data.keys():
    #     print(f"KEY:{key}")
    #     if key.upper() in missing_wanted_facts:
    #         have_summary_facts[key.upper()] = host.data[key]

    return have_summary_facts


def task_backup_config(
    task: Task,
    user_config: dict,
    **kwargs,
    # config_backup_folder,
) -> Result:

    # print(f"host parameters: {task.host.dict()}")

    task_starttime = datetime.datetime.now()

    config_file = None
    config_diff_file = None

    # import sys
    # sys.exit()

    result = {
        "get_running_config": False,
        "save_running_config": False,
        "failed": False,
    }

    if user_config["facts"]["enabled"]:
        fact_tasks_output = task.run(
            task=task_get_facts,
            user_config=user_config,
        )
        summary_facts = get_summary_facts(
            fact_tasks_output,
            host=task.host,
            wanted_summary_facts=user_config["facts"]["summary"],
        )
        # print(fact_tasks_output.result)
    else:
        summary_facts = dict()

    # print(summary_facts)

    cmd_running_config = task.host.extended_data().get("cmd_running_config")
    # print(f"show running config command = {cmd_running_config}")

    r = task.run(task=netmiko_send_command, command_string=cmd_running_config)

    if not r.failed:
        result["get_running_config"] = True

    if r.failed:
        result["failed"] = True

    backup_config_file = generate_filename(
        filetype="backup",
        hostname=task.host,
        user_config=user_config,
    )

    r = task.run(
        task=write_file,
        filename=backup_config_file,
        content=generate_comment(summary_facts)
        + "\n"
        + r.result
        + "\n"
        + generate_comment("### END OF CONFIG ###", header=[""]),
    )

    if not r.failed:
        result["save_running_config"] = True
        config_file = backup_config_file

        if user_config["backup_config"]["save_config_diff"]:
            diff_file = generate_filename(
                filetype="diff", hostname=task.host, user_config=user_config
            )
            if r.diff and diff_file:
                config_diff_file = diff_file
                task.run(
                    task=write_file,
                    filename=diff_file,
                    content=r.diff,
                )

    if r.failed:
        result["failed"] = True

    task_endtime = datetime.datetime.now()
    task_duration = task_endtime - task_starttime

    # save the result to the inventory Host object
    task.host.data.setdefault("_backup_results", {}).setdefault("config", {})
    task.host.data["_backup_results"]["config"] = result
    task.host.data["_backup_results"]["starttime"] = task_starttime
    task.host.data["_backup_results"]["endtime"] = task_endtime
    task.host.data["_backup_results"]["duration"] = task_duration.total_seconds()
    task.host.data["_backup_results"]["config"]["backup_file"] = (
        Path(config_file).name if config_file else ""
    )
    task.host.data["_backup_results"]["config"]["diff_file"] = (
        config_diff_file if config_diff_file else ""
    )

    print(
        f"{task.host}: {'FAILED' if result['failed'] else 'SUCCESS'} in {task_duration.total_seconds()} seconds"
    )
    logger.info(
        f"{task.host}: {'FAILED' if result['failed'] else 'SUCCESS'} in {task_duration.total_seconds()} seconds"
    )

    return Result(host=task.host, result=result)


def add_host_to_inventory(
    hostname: str, ip: str, username: str, password: str, platform: str
):
    """adds a host to the inventory programatically"""
    if not platform:
        raise Exception(
            "This host is not known in the database, you have to provide the platform as extra commandline parameter"
        )

    return Host(
        name=hostname,
        hostname=hostname,
        username=username,
        password=password,
        platform=platform,
    )


def get_fact_commands(host: Host) -> list:
    """return a list of all the facts commands found hierarchically in host and all groups
    The default recursive behavior in Nornir will stop at the first match
    """
    fact_commands = [cmd for cmd in host.extended_data().get("cmd_facts", [])]

    for grp in host.groups:
        fact_commands += [cmd for cmd in grp.extended_data().get("cmd_facts", [])]

    return list(set(fact_commands))


def _init_nornir(
    config_file: str,
    regenerate_hostsfile: bool,
    gather_facts: bool,
):
    """Initiates the nornir object without applying any filters

    backup_script = single | many
    """

    # register extra plugins
    InventoryPluginRegister.register("NMAPDiscoveryInventory", NMAPDiscoveryInventory)
    TransformFunctionRegister.register("load_credentials", load_credentials)

    nornir_config = None

    with open(config_file, "r") as f:
        yml = ruamel.yaml.YAML(typ="safe")
        nornir_config = yml.load(f)

        # always override the regenerate_hosts parameter

    if (
        regenerate_hostsfile is not None
        and nornir_config["inventory"]["plugin"] == "NMAPDiscoveryInventory"
    ):
        nornir_config["inventory"]["options"]["regenerate"] = regenerate_hostsfile

    if gather_facts is not None:
        nornir_config["user_defined"]["facts"]["enabled"] = gather_facts

    nr = InitNornir(**nornir_config)

    return nr


def run_backup_process(nr, nr_unfiltered):

    backup_start_time = datetime.datetime.now()

    logger.info(f"--- START BACKUP PROCESS FOR {len(nr.inventory.hosts)} HOSTS ---")
    print(
        "-" * 50
        + f"\n--- START BACKUP PROCESS FOR {len(nr.inventory.hosts)} HOSTS ---\n"
        + "-" * 50
    )

    result = nr.run(
        task=task_backup_config,
        user_config=nr.config.user_defined,
    )

    backup_end_time = datetime.datetime.now()

    backup_duration = backup_end_time - backup_start_time

    # report info summary:
    #   total hosts
    #   failed hosts
    #   successful hosts
    #   start time
    #   end time
    #   total runtime

    # report info details:
    #   host, backup status (fail|success|skip), OS, HWTYPE, backup time, backup duration, fact files

    nbr_processed_hosts = len(result.items())
    nbr_failed_hosts = len(result.failed_hosts)
    nbr_success_hosts = nbr_processed_hosts - nbr_failed_hosts
    success_rate = (nbr_success_hosts / nbr_processed_hosts) * 100
    backup_start_date = backup_start_time.strftime("%Y-%m-%d")
    backup_start_time = backup_start_time.strftime("%H-%M-%S")

    for failed_host in result.failed_hosts:
        print(f"{failed_host}: FAILED")
        logger.error(f"FAILED HOST: {failed_host}")

    logger.info(
        f"--- {nbr_success_hosts} FINISHED IN {backup_duration.total_seconds()} SECONDS, {nbr_failed_hosts} FAILED ---"
    )
    print(
        "-" * 50
        + f"\n--- {nbr_success_hosts} FINISHED, {nbr_failed_hosts} FAILED IN {backup_duration.total_seconds()} SECONDS ---\n"
        + "-" * 50
    )

    backup_summary = {
        "backup_start_date": backup_start_date,
        "backup_start_time": backup_start_time,
        "overall_result": "success" if not result.failed else "failed",
        "nbr_unfiltered_hosts": len(nr_unfiltered.inventory.hosts),
        "nbr_filtered_hosts": len(nr.inventory.hosts),
        "nbr_processed_hosts": nbr_processed_hosts,
        "nbr_failed_hosts": nbr_failed_hosts,
        "nbr_success_hosts": nbr_success_hosts,
        "success_rate": success_rate,
        "failed_rate": 100 - success_rate,
        "duration_seconds": backup_duration.total_seconds(),
    }

    # write the backup summary
    with open("config-backups-summary.txt", "a") as f:
        f.write(json.dumps(backup_summary, indent=4))

    # write the host details
    for host, host_data in result.items():
        backup_results = host_data.host.data.get("_backup_results", {})
        facts_failed = backup_results.get("facts", {}).get("failed", True)
        config_failed = backup_results.get("config", {}).get("failed", True)
        report = {
            "result": "failed" if (facts_failed or config_failed) else "success",
            "backup_start_date": backup_start_date,
            "backup_start_time": backup_start_time,
            "backup_duration": backup_duration.total_seconds(),
            "task_start_time": str(backup_results.get("starttime", "")),
            "task_stop_time": str(backup_results.get("endtime", "")),
            "task_duration": backup_results.get("duration", -1),
            "host": host,
            "hwtype": host_data.host.data.get("hwtype", ""),
            "vendor": host_data.host.data.get("vendor", ""),
            "software": host_data.host.data.get("software", ""),
            "platform": host_data.host.platform,
            "os_slug": host_data.host.data.get("os_slug", ""),
            "config_file": backup_results.get("config", {}).get("backup_file", ""),
            "changed": True
            if backup_results.get("config", {}).get("diff_file", "")
            else False,
            "facts_commands": ",".join(
                backup_results.get("facts", {}).get("all_commands", [])
            ),
            "facts_failed_commands": ",".join(
                backup_results.get("facts", {}).get("failed_commands", [])
            ),
            "facts_count": backup_results.get("facts", {}).get("total_commands", 0),
            "facts_result": "failed"
            if backup_results.get("facts", {}).get("failed", True)
            else "success",
            "facts_count_failed": backup_results.get("facts", {}).get(
                "total_failed_commands", 0
            ),
        }

        with open("config-backups-details.txt", "a") as f:
            f.write(json.dumps(report) + "\n")


def _apply_inventory_transformation(
    nr, username: str = None, password: str = None, platform: str = None
):

    transform_function = TransformFunctionRegister.get_plugin("load_credentials")
    for h in nr.inventory.hosts.values():
        transform_function(
            h,
            **(
                {
                    "username": username,
                    "password": password,
                    "platform": platform,
                }
                or {}
            ),
        )


def nr_backup_single_host(
    hostname: str,
    username: str,
    password: str,
    platform: str,
    regenerate_hostsfile: bool,
    gather_facts: bool,
    config_file: str = None,
):

    nr = _init_nornir(
        config_file=config_file,
        regenerate_hostsfile=regenerate_hostsfile,
        gather_facts=gather_facts,
    )

    # InventoryPluginRegister.register(
    #     "NMAPDiscoveryInventory", NMAPDiscoveryInventory
    # )

    # InventoryPluginRegister.register(
    #     "BackupReporter", BackupReporter
    # )

    # nornir will be initialized from dict because for single-host-backup we will not regenerate
    # the hosts.yaml file each time

    # with open(config_file, "r") as f:
    #     yml = ruamel.yaml.YAML(typ="safe")
    #     nornir_config = yml.load(f)

    # if nornir_config["inventory"]["plugin"] == "NMAPDiscoveryInventory":
    #     nornir_config["inventory"]["options"][
    #         "regenerate"
    #     ] = regenerate_hostsfile

    # nornir_config["user_defined"]["facts"]["enabled"] = gather_facts

    # nr = InitNornir(**nornir_config)
    init_user_defined_config(nr)

    # print(f"gather facts: {nornir_config['user_defined']['facts']['enabled']}")

    # print(f"TOTAL HOSTS FOUND: {len(nr.inventory.hosts)}")

    # search the host(s) based on inventory name or hostname(=IP address)
    nr_filtered = nr.filter(F(name__eq=hostname) | F(hostname__eq=hostname))

    # nr_filtered = nr.filter(
    #     F(name__eq="dops-lab-02")
    #     | F(name__eq="lab_00009-sas51-100")
    #     | F(name__eq="nos-tasr-01")
    #     | F(name__eq="orangeshop01-4glbb-158")
    #     | F(name__eq="plushome01-50oos-01")
    #     | F(name__eq="orangeswops-02738344-plug401-2725")
    # )

    # nr_filtered = nr_filtered.with_processors([BackupReporter()])

    # print(f"HOSTS FOUND after filtering: {nr_filtered.inventory.hosts}")

    # override the inventory details with the CLI parameters, for security reasons and overriding the existing inventory
    if nr_filtered.inventory.hosts:
        # make sure the hostname contains the key of the host and not the ip address
        hostname = list(nr_filtered.inventory.hosts.keys())[0]
        print(
            f"-- host {hostname} was found in the inventory, we will use it but take the username, password, platform from CLI"
        )
        # if username:
        #     nr.inventory.hosts[hostname].username = username
        # if password:
        #     nr.inventory.hosts[hostname].password = password
        # if platform:
        #     nr.inventory.hosts[hostname].platform = platform
    # otherwise create a new host and add the platform as group
    else:
        logger.info(
            f"-- host {hostname} was not found in the inventory, we will create an entry"
        )
        nr.inventory.hosts[hostname] = add_host_to_inventory(
            hostname, hostname, username, password, platform
        )
        nr.inventory.hosts[hostname].defaults = nr.inventory.defaults
        grp = nr.inventory.groups.get(platform)
        if grp:
            nr.inventory.hosts[hostname].groups.add(grp)
        nr_filtered = nr.filter(name=hostname)

    # add username + password to each host
    _apply_inventory_transformation(
        nr_filtered, username=username, password=password, platform=platform
    )

    run_backup_process(nr_filtered, nr)

    # print(f"TOTAL HOSTS: {nr_filtered.inventory.hosts}")

    # print(nr.inventory.hosts[hostname].dict())

    # print(nr.inventory.hosts[hostname].defaults)
    # print(nr.inventory.hosts[hostname].data)
    # print(nr.inventory.hosts[hostname].extended_data())
    # print(nr.inventory.hosts[hostname].extended_groups())
    # print(nr.inventory.hosts[hostname].groups)
    # print(nr.inventory.hosts[hostname].get("cmd_facts"))
    # print(get_fact_commands(nr.inventory.hosts[hostname]))
    # import sys

    # sys.exit()

    # if the backup config file exists then rename it to <config file>.failed

    # with open("config_backup.txt", "w") as f:
    #     for host, host_data in result.items():
    #         f.write(f"{host}: {host_data.result}\n")


def nr_backup_many(
    username: str,
    password: str,
    all_hosts: bool,
    host_list: list,
    group_list: list,
    regenerate_hostsfile: bool,
    gather_facts: bool,
    config_file: str = None,
):
    """Starts the backup process for many hosts based on nornir filtering:

    if all_hosts is True => use all hosts, regardless if host_list or group_list is defined
    """

    nr = _init_nornir(
        config_file=config_file,
        regenerate_hostsfile=regenerate_hostsfile,
        gather_facts=gather_facts,
    )

    init_user_defined_config(nr)

    _filter = []

    for host in host_list:
        _filter.append(f"F(name__eq='{host}') | F(hostname__eq='{host}')")

    for group in group_list:
        _filter.append(f"F(groups__contains='{group}')")

    if _filter:
        nr_filtered = nr.filter(eval("|".join(_filter)))
    else:
        nr_filtered = nr

    # add username + password to each host
    _apply_inventory_transformation(nr_filtered, username=username, password=password)

    print(f"starting backup for hosts: {nr_filtered.inventory.hosts}")
    run_backup_process(nr_filtered, nr)
