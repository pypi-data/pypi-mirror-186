#!/usr/bin/env python3

import argparse
import sys
import os
from todo import utils

def get_dir():
    cwd = os.getcwd()
    cwd_list = cwd.split("/")[1:]
    cwd_clean = [utils.clean_dir_name(x) for x in cwd_list]
    return cwd_clean

def cli():
    cwd_clean = get_dir()

    parser = argparse.ArgumentParser(description="todo")
    parser.add_argument('task_name', nargs='?')

    options = (
            {"name": "complete", "tag": "-c", "action": utils.complete,
                "input_property" : "task_name"},
            {"name": "sort", "tag": "-s", "action": utils.sort_by_prio},
            {"name": "edit", "tag": "-e", "action": utils.edit},
            {"name": "showall", "tag": "-sa", "action": utils.global_all_tasks},
            {"name": "init", "tag": "-i", "action": utils.initialise},
            {"name": "all", "tag": "-a", "action": utils.all_tasks},
            {"name": "reset", "tag": "-r", "action": utils.reset_ids},
            {"name": "completeall", "tag": "-ca", "action":utils.complete_all},
            {"name": "delete", "tag": "-d", "action":utils.delete_all},
    )

    g = parser.add_mutually_exclusive_group()
    for option in options:
        g.add_argument(option["tag"], "--" + option["name"], action="store_true")

    args = parser.parse_args()

    if args.init:
        utils.initialise(cwd_clean[-1])
        sys.exit(0)

    cur_dir = utils.search_for_dir(cwd_clean)
    utils.dir_name = cur_dir    

    for option in options:
        if getattr(args, option["name"]):
            arg = option.get("input_property", ())
            if arg:
                arg = (getattr(args, arg),)
            option["action"](*arg)
            sys.exit(0)

    if not len(sys.argv) > 1:
        utils.oldest_incomplete_tasks()
    else:
        utils.add_task(args.task_name)
        print(f'Added task {args.task_name}')
