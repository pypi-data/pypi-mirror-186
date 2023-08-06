import json
import os

from ruamel.yaml.main import round_trip_dump as yaml_dump


def generate_filename(
    filetype: str,
    hostname: str,
    user_config: dict,
    extension: str = None,
    command: str = None,
):
    """convenience function that will generate the filename

    args:
        filetype: backup|diff|fact
    """
    config_backup_folder = user_config["backup_config"]["folder"]
    config_diff_folder = user_config["backup_config"]["config_diff_folder"]
    erase_existing_diff_file = user_config["backup_config"]["save_config_diff"]
    facts_folder = user_config["facts"]["folder"]

    if filetype == "backup":
        return f"{config_backup_folder}/{hostname}-config.txt"

    if filetype == "diff":
        outputdir = config_diff_folder or config_backup_folder
        diff_file = os.path.join(outputdir, f"{hostname}.diff")
        if erase_existing_diff_file:
            remove_file(diff_file)
        return diff_file

    if filetype == "fact":
        cmd_nice = command.replace(" ", "_").replace("|", "_")
        output_dir = facts_folder or config_backup_folder
        return f"{output_dir}/{hostname}-{cmd_nice}.{extension}"

    return None


def remove_file(fn: str):
    try:
        os.unlink(fn)
    except Exception:
        pass


def fact_to_yml(content):
    """converts a list or dict into YAML format
    If the content is a string then the content will not be converted to YAML.

    returns:
        content: the converted content
        extension: either YAML or TXT, depending if conversion succeeded
    """
    extension = "txt"
    if type(content) is dict or type(content) is list:
        content = yaml_dump(content)
        extension = "yaml"
    return content, extension


def fact_to_json(content):
    """converts a list or dict into JSON format
    If the content is a string then the content will not be converted to YAML.

    returns:
        content: the converted content
        extension: either JSON or TXT, depending if conversion succeeded
    """
    extension = "txt"
    if type(content) is dict or type(content) is list:
        content = json.dumps(content, indent=4)
        extension = "json"
    return content, extension


def generate_comment(
    data,
    comment_str="!",
    header=["", "### START OF CONFIG ###", ""],
    footer=[""],
) -> str:
    """generates a router configuration comment

    args:
        data: the text that should be changed into comment
        comment_str: the comment string to be used
        header: list of strings that should be prepended
        footer: list of strings that should be appended

    if data = string => prepend with comment_str
    if data = dict => sort alphabetically and make key: value strings with comment_str
    if data = list => prepend every entry with comment_str

    Examples:
        data = "this is  a test"
            => "! this is a test"

        data = ["this", "is", "a", "test"]
            => "! this"
               "! is"
               "! a"
               "! test"

        data = {"this": "is", "a": "test"}
            => "! a: test"
               "! this: is"

    return the entire block as a string
    """
    result = []
    if type(data) is str:
        result.append(data)
    elif type(data) is list:
        # lists within lists are skipped
        for item in data:
            if type(item) is str:
                result.append(item)
    elif type(data) is dict:
        for key in sorted(data.keys()):
            result.append(f"{key}: {data[key]}")

    # add header
    if header:
        result = header + result

    # add footer
    if footer:
        result = result + footer

    return "\n".join(map(lambda x: f"{comment_str} {x}", result))
