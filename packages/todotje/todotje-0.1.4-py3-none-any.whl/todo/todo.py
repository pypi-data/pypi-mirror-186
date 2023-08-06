#!/usr/bin/env python3

import argparse
import sys
import os
import utils

def get_dir():
    cwd = os.getcwd()
    cwd_list = cwd.split("/")[1:]
    cwd_clean = [utils.clean_dir_name(x) for x in cwd_list]
    return cwd_clean

parser = argparse.ArgumentParser(description="Test")
parser.add_argument('task_name', nargs='?')
g = parser.add_mutually_exclusive_group()
g.add_argument('-c', '--complete',
                    action="store_true")
g.add_argument('-s', '--sort', action="store_true")
g.add_argument('-e', '--edit', action="store_true")
g.add_argument('-a', '--all', action="store_true")
g.add_argument('-ca', '--clearall', action="store_true")
g.add_argument('-d', '--delete', action="store_true")
g.add_argument('-i', '--init', action="store_true")
g.add_argument('-sa', '--showall', action="store_true")
g.add_argument('-r', '--reset', action="store_true")
parser.add_argument("-x",'--debug', action="store_true")

args = parser.parse_args()

cwd_clean = get_dir()

if args.showall:
    utils.global_all_tasks()
    sys.exit(0)

if args.init:
    utils.initialise(cwd_clean[-1])
    sys.exit(0)

cur_dir = utils.search_for_dir(cwd_clean)
utils.dir_name = cur_dir    

if not len(sys.argv) > 1:
    utils.oldest_incomplete_tasks()
elif args.complete:
    utils.complete(args.task_name)
elif args.sort:
    utils.sort_by_prio()
elif args.edit:
    utils.edit()
elif args.all:
    utils.all_tasks()
elif args.clearall:
    ans = input("Do you want to complete all tasks? y/[n]")
    if ans == "y":
        utils.complete_all()
elif args.delete:
    ans = input("Do you really want to delete all tasks? y/[n]")
    if ans == "y":
        utils.delete_all()
elif args.reset:
    utils.reset_ids()
else:
    utils.add_task(args.task_name)
    print(f'Added task {args.task_name}')
if args.debug:
    print(args)
