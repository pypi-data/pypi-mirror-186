#!/usr/bin/env python3

# This functionality should be merged into
# https://github.com/galaxyproject/training-material/blob/main/bin/check_instance.py

"""
This is a command line tool for checking whether a Galaxy workflow can be run on
a particular Galaxy instance. It does this by checking whether the tools used in
the workflow are available on the specified Galaxy instance. If a tool is not
available, the program can optionally install it from the tool shed.

Usage: check_workflow_tools.py [-h] [-i] workflow_path galaxy_url api_key

Optional arguments:
  -p PATH, --path PATH  path or URL to the workflow file
  -r REPO, --repo REPO  path to a local copy of the usegalaxy-tools repository
  -u URL, --url URL     Galaxy server URL
  -k KEY, --key KEY     an admin API key for the Galaxy server. Required to install the workflow and tools.
  -i, --install         install the workflow and any missing tools.
  -h, --help            show this help message and exit

"""

import os
import sys
import json
import yaml
import requests
import argparse

import bioblend.galaxy
from planemo.runnable import for_path
from planemo.galaxy.workflows import install_shed_repos


def check_workflow_tools(tools, workflow_path, galaxy_url, api_key, install_tools):
    """
    Check whether the tools used in a Galaxy workflow are available on a
    particular Galaxy instance. Optionally install missing tools from the
    tool shed.

    Parameters:
        tools (list): A list of tools to check.
        workflow_path (str): The path to the workflow file. Can be a local file path or a URL.
        galaxy_url (str): The URL of the Galaxy instance to check.
        api_key (str): An API key for accessing the Galaxy instance.
        install_tools (bool): A boolean indicating whether to install missing tools.

    Returns:
        int: An exit code of 0 if all tools are available, or 2 if any tools are missing or have the wrong version.
    """

    if workflow_path.startswith('http'):
        response = requests.get(workflow_path)
        if response.status_code != 200:
            print(f"Unable to fetch the workflow from {workflow_path}")
            print(f"{response.status_code} - {response.reason}")
            return
        workflow = response.text
    else:
        with open(workflow_path) as f:
            workflow = json.load(f)

    # print(json.dumps(workflow, indent=4))
    not_found = {}
    wrong_version = {}
    gi = bioblend.galaxy.GalaxyInstance(galaxy_url, api_key)
    nSteps = len(workflow['steps'])
    for nStep in range(nSteps):
        step = workflow['steps'][str(nStep)]
        if step['tool_id']:
            tool_id = step['tool_id']
            if 'tool_shed_repository' in step:
                revision = step['tool_shed_repository']['changeset_revision']
            else:
                # print(f"{tool_id} does not have a tool_shed_repository")
                # print(json.dumps(step, indent=4))
                revision = 'unknown'
            try:
                tool = gi.tools.show_tool(tool_id)
                # print(json.dumps(tool, indent=4))
                if tool['id'] != tool_id:
                    wrong_version[tool_id] = revision #tool['id']
            except:
                not_found[tool_id] = revision

    exit_code = 0
    if len(not_found) == 0 and len(wrong_version) == 0:
        print('All tools are available for this workflow')
    else:
        exit_code = 2
        process_not_found(not_found)
        process_wrong_version(wrong_version)

    if install_tools:
        if api_key is None:
            print("Unable to install tools without an admin API key.")
        else:
            result = gi.workflows.import_workflow_from_local_path(workflow_path, publish=True)
            print(json.dumps(result, indent=4))
            runnable = for_path(workflow_path)
            print("Installing tools")
            install_shed_repos(runnable, gi, False)

    return exit_code


def process_not_found(tools):
    """
    Process a list of missing tools and print out instructions for adding them
    to the appropriate lock files.

    Parameters:
        tools (dict): A dictionary of missing tools, where the keys are tool IDs and the values are tool revisions.
    """

    if len(tools) == 0:
        return

    print("# Please add the following entries to the appropriate .lock file(s) and update the matching .yml files.")
    for id, revision in tools.items():
        (shed, ignored, owner, group, name, version) = id.split('/')
        key = f"{owner}/{name}"
        if key in tools:
            if not revision in tools[key]['revisions']:
                print(f"We need to update {key} to revision {revision}")
            else:
                print(f"ERROR?: usegalaxy-tools/cloud already contains {key} revision {revision}!!!")
        else:
            section = {
                'name': name,
                'owner': owner,
                'revisions': [revision],
                'tool_panel_section_id': 'section_id',
                'tool_panel_section_label': 'section_label'
            }
            print(yaml.dump([section]))


def process_wrong_version(tools):
    """

    :param tools:
    :return:
    """
    if len(tools) == 0:
        return
    print("Wrong versions installed")
    for id, revision in tools.items():
        (shed, ignored, owner, group, name, version) = id.split('/')
        key = f"{owner}/{name}"
        if key in tools:
            tool = tools[key]
            if not revision in tool['spec']['revisions']:
                tool['spec']['revisions'].append(revision)
                # TODO if --update was specified on the command line then update the file.
                print(f"# Update the following block in  {tool['path']}")
                print(yaml.dump([tools[key]['spec']]))
            else:
                # If {key}@{revision} is not installed on the instance but is present
                # in usegalaxy-tools then something is amiss...
                print(f"usegalaxy-tools/cloud already contains {key} revision {revision} ")
        else:
            print("The wrong version is installed on Galaxy but there is no entry in usegalaxy-tools!")
            section = {
                'name': name,
                'owner': owner,
                'revisions': [revision],
                'tool_panel_section_id': 'section_id',
                'tool_panel_section_label': 'section_label'
            }
            print(yaml.dump([section]))


def load_lock_file(filepath, tools):
    """

    :param filepath:
    :param tools:
    :return:
    """
    # print(f"Loading {filepath}")
    with open(filepath) as f:
        tool_info = yaml.safe_load(f)

    for tool in tool_info['tools']:
        name = tool['name']
        owner = tool['owner']
        key = f"{owner}/{name}"
        if key in tools:
            # raise Exception(f"{tool} has already been defined in")
            print(f"WARNING: {key} is already defined in {tools[key]['path']}")
        else:
            tools[key] = {
                'path': filepath,
                'spec': tool
            }
        # revisions = tool['revisions']
        # if name not in tools:
        #     tools[name] = []
        # tools[name].extend(revisions)


def scan_usegalaxy_tools(directory_path):
    tools = {}
    files = os.scandir(directory_path)
    for item in files:
        if item.is_file and item.name.endswith('.lock'):
            load_lock_file(item.path, tools)
    return tools


def test_tool_not_found(id, url, key):
    print(f"Searching for {id}")
    gi = bioblend.galaxy.GalaxyInstance(url, key)
    print(json.dumps(gi.tools.show_tool(id), indent=4))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Check if all tools used in a workflow are present on a given Galaxy instance.',
        epilog='Copyright 2022 The Galaxy Project'
    )
    parser.add_argument('-p', '--path', required=True, help='path to the workflow file')
    parser.add_argument('-r', '--repo', required=True, help='path to a local copy of the usegalaxy-tools repository')
    parser.add_argument('-u', '--url', required=True, help='Galaxy server URL')
    parser.add_argument('-k', '--key', help='an admin API key for the Galaxy server.  Required to install the workflow and tools.')
    parser.add_argument('-i', '--install', default=False, action='store_true', help='install the workflow and any missing tools.')

    argv = parser.parse_args()
    exit_code = 0
    tools = scan_usegalaxy_tools(argv.repo)
    exit_code = check_workflow_tools(tools, argv.path, argv.url, argv.key, argv.install)
    sys.exit(exit_code)
