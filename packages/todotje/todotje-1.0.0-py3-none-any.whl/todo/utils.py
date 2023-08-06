import sqlite3
from datetime import datetime
import sys

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
TASK_FILE = "task_db.db"

def add_entry(con, entry_dict):
    cur = con.cursor()
    query = "INSERT INTO {dir_name} ({columns}) VALUES ({vps})".format(
        dir_name = dir_name,
        columns=", ".join(entry_dict.keys()),
        vps=", ".join(["?"]*len(entry_dict)))
    cur.execute(query, list(entry_dict.values()))
    con.commit()


def process_entry(con, task_name, task_completed=False, prio=5):
    cur = con.cursor()
    dt_string = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    num_tasks = cur.execute(f'SELECT COUNT(*) FROM {dir_name}').fetchone()[0]
    task_id = num_tasks + 1
    entry_dict = {"task_name": task_name, "date": dt_string,
                  "completed": task_completed, "task_id": task_id,
                  "prio": prio}
    add_entry(con, entry_dict)


def fetch_incomplete(con):
    cur = con.cursor()
    res = cur.execute(f'SELECT * FROM {dir_name} where completed=0')
    cols = fetch_columns(con)
    return [entry_to_dict(con, t, cols) for t in res.fetchall()]


def fetch_all(con):
    cur = con.cursor()
    res = cur.execute(f'SELECT * FROM {dir_name}')
    cols = fetch_columns(con)
    return [entry_to_dict(con, t, cols) for t in res.fetchall()]


def fetch_columns(con):
    cur = con.cursor()
    cur.execute(f'SELECT * FROM {dir_name}')
    columns = [d[0] for d in cur.description]
    return columns


def entry_to_dict(con, entry, cols=None):
    if cols is None:
        cols = fetch_columns(con)
    return {col: val for col, val in zip(cols, entry)}


def connect(func):
    """ A decorator to automatically connect to the database """
    def wrapper(*args):
        with sqlite3.connect(TASK_FILE) as con:
            result = func(con, *args)
        con.close()
        return result
    return wrapper


@connect
def name_to_id(con, task_name):
    cur = con.cursor()
    query = f'SELECT task_id from {dir_name} WHERE task_name = "{task_name}"'
    try:
        res = cur.execute(query)
        return res.fetchone()[0]
    except:
        sys.exit("invalid task name") 

@connect
def id_to_name(con, task_id):
    cur = con.cursor()
    query = f'SELECT task_name from {dir_name} WHERE task_id = {task_id}'
    res = cur.execute(query)
    ans = res.fetchone()[0]
    print(ans)
    return ans


@connect
def complete_by_id(con, task_id):
    try:
        cur = con.cursor()
        cur.execute(f'UPDATE {dir_name} SET completed = 1 WHERE task_id = {task_id}')
        return True
    except:
        return False


@connect
def complete(con, task_id):
    if not task_id.isdigit():
        task_id = name_to_id(task_id)
    if complete_by_id(task_id):
        print(f'Completed {id_to_name(task_id)}.')
    else:
        print(f'Error completing {task_id}.')


@connect
def complete_all(con):
    for task in fetch_incomplete(con):
        complete_by_id(task["task_id"])


@connect
def edit(con):
    """ A function for editing tasks """
    task_in = input("Which task would you like to edit? ")
    task_id = check_valid(task_in)
    if task_id is None:
        sys.exit("Please enter a valid task name or id.")

    property_list = ["name", "prio", "completed", "task_id"]
    pdict = {ix: property for ix, property in enumerate(property_list, 1)}
    property_id = get_property_id(pdict, len(property_list))
    new_property = input(f'Enter new {pdict[property_id]}: ')

    if pdict[property_id] == "name":
        query = (f'UPDATE {dir_name} SET task_name'
                 f'= "{new_property}" WHERE task_id = {task_id}')
    else:
        query = (f'UPDATE {dir_name} SET {pdict[property_id]}'
                 f' = {new_property} WHERE task_id = {task_id}')
    cur = con.cursor()
    cur.execute(query)

def get_property_id(pdict, n):
    p_strings = [f'{ix}: {property}' for ix, property in pdict.items()]
    p_str = "[" + "]  [".join(p_strings) + "]"
    user_input = input("Which property?\n" + p_str + "\n")
    while True:
        try:
            property_id = int(user_input)
            if property_id >= 1 and property_id <= n:
                return property_id
        except:
            print("Enter a number")
        property_id = input("Enter a valid number")

@connect
def check_valid(con, task_in):
    task_list = fetch_incomplete(con)
    if task_in.isdigit():
        for task in task_list:
            if task["task_id"] == int(task_in):
                return int(task_in)
        return None
    for task in task_list:
        if task["task_name"] == task_in:
            return task["task_id"]
    return None


@connect
def delete_all(con):
    cur = con.cursor()
    cur.execute(f'DELETE FROM {dir_name}')


@connect
def main(con):
    task_name = input("Task name (priority): ")
    if task_name.split()[-1].isdigit():
        prio = int(task_name.split()[-1])
        task_name = "".join(task_name.split()[:-1])
    else:
        prio = 5
    process_entry(con, task_name=task_name, prio=prio)


@connect
def add_task(con, task_name):
    process_entry(con, task_name=task_name, prio=5)


def format_time(seconds):
    days = seconds // (60*60*24)
    hours = seconds // (60*60)
    minutes = seconds // 60
 
    if days >= 1:
        return f'{days:2d} days ago'
    if days == 1:
        return f'{days:2d} day  ago'
    if hours > 1:
        return f'{hours:2d} hours ago'
    if hours == 1:
        return f'{hours:2d} hour  ago'
    if minutes > 1:
        return f'{minutes:2d} minutes ago'
    if minutes == 1:
        return f'{minutes:2d} minute  ago'
    
    return f'{seconds:2d} seconds ago'
    

def print_task(task):
    """ makes the task human-readable """
    now = datetime.now()
    start_time = datetime.strptime(task["date"], DATETIME_FORMAT)
    time_since = now - start_time
    time_formatted = format_time(time_since.seconds)
    res = (f'{task["task_name"][:20]:20s}'
           f'{time_formatted:17s} ||'
           f' priority: {str(task["prio"]):5s} id:{task["task_id"]}')
    if task["completed"] == 1:
        res += " Completed"
    print(res)

###

@connect
def reset_ids(con):
    """ Re-numbers the tasks starting from 1 """
    incomplete_tasks = fetch_incomplete(con)
    sorted_incomplete = sorted(incomplete_tasks, key=lambda x: x["task_id"])
    cur = con.cursor()
    for index, task in enumerate(sorted_incomplete):
        query = (
                f'UPDATE {dir_name} SET task_id = {index + 1}'
                f' WHERE task_id = {task["task_id"]}'
        )
        cur.execute(query)
    reset_completed = f'UPDATE {dir_name} set task_id = 0 WHERE completed=1'
    cur.execute(reset_completed)


@connect
def oldest_incomplete_tasks(con):
    """ prints the oldest n tasks"""
    reset_ids()
    incomplete_tasks = fetch_incomplete(con)
    sorted_incomplete_tasks = sorted(incomplete_tasks, key=lambda x: x["date"])
    for task in sorted_incomplete_tasks:
        print_task(task)


@connect
def sort_by_prio(con, asc=True):
    """ prints the tasks in order of priority """
    incomplete_tasks = fetch_incomplete(con)
    tasks_by_prio = sorted(incomplete_tasks,
                           key=lambda x: x["prio"] or 5,
                           reverse=asc)
    for task in tasks_by_prio:
        print_task(task)


@connect
def all_tasks(con):
    all_tasks = fetch_all(con)
    for task in all_tasks:
        print_task(task)

### admin

def clean_dir_name(dir_name):
    return "".join(c for c in dir_name if c.isalnum())


@connect
def initialise(con, directory):
    try:
        cur = con.cursor()
        query = f'CREATE TABLE {directory}(task_name, prio, date, completed, task_id)'
        cur.execute(query)
        print(f'Initialised todo list for {directory}.')
    except:
        print("already initialised (or invalid directory name)...")
        # could do directory name cleaning ... 

def search_for_dir(cwd_split):
    valid_dirs = get_table_names()
    for dir_name in cwd_split[::-1]:
        if dir_name in valid_dirs:
            return dir_name
    sys.exit("Not inside an initialised directory.")

def check_valid_directory(table_name):
    return table_name in get_table_names()


@connect
def fetch_task_columns(con, tn):
    cur = con.cursor()
    cur.execute(f'SELECT * FROM {tn}')
    columns = [d[0] for d in cur.description]
    return columns


@connect
def get_table_names(con):
    cur = con.cursor()
    query = "SELECT name FROM sqlite_master WHERE type='table'"
    table_names = cur.execute(query).fetchall()
    return [t[0] for t in table_names]



@connect
def global_all_tasks(con):
    cur = con.cursor()
    table_names = get_table_names()
    for tn in table_names:
        print("\n", tn)
        query = f"SELECT * from {tn}"
        dir_name = tn
        res = cur.execute(query)
        cols = fetch_task_columns(tn)
        task_list = [entry_to_dict(con, t, cols) for t in res.fetchall()]
        for task in task_list:
            print_task(task)

