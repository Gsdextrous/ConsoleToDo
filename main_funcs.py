from main_objects import *      # ToDo, Status
from database import events
from auxilliaries import multiline_input, get_random_sequence


def add_todo():
    obj = ToDo()

    print("name?")
    user_data = input()
    obj.name = None if user_data == "" else user_data

    print("custom ID (without '@') ?")
    user_data = input()
    obj.id = generate_unique_id() if user_data == "" else f'@{user_data}'

    print("add some info?")
    user_data = multiline_input()
    obj.info = '' if user_data == "" else user_data

    print("achievement points?")
    user_data = input()
    try:
        obj.points_left = 0 if user_data == "" else int(user_data)
    except TypeError:
        obj.points_left = 0

    print("ordinary/urgent/done")
    user_data = input()
    stat_list = [ORDINARY, URGENT, DONE]
    try:
        obj.status = ORDINARY if user_data == "" else stat_list[int(user_data) - 1]
    except TypeError or IndexError:
        obj.status = ORDINARY

    print("active till?")
    user_data = input()
    time_string = None if user_data == "" else user_data
    obj.set_deadline(time_string)

    events.append(obj)


def get_events_by_name(todo_name):  # TODO make user type unique names
    res = []
    for event in events:
        if event.name == todo_name:
            if event.status == DELETED:
                continue
            res.append(event)
    return res


def get_event_by_id(todo_id):
    for event in events:
        if event.id == todo_id:
            if event.status == DELETED:
                continue
            return event


def get_all_ids():
    return [event.id for event in events if (event.status != DELETED) and (event.id is not None)]


def generate_unique_id():
    pool = set(get_all_ids())
    while True:     # FIXME
        gen = f'@{get_random_sequence(6)}'
        if gen in pool:
            continue
        return gen


def identify_todos(name_or_id):
    try:
        if name_or_id[0] == '@':
            return {'targets': [get_event_by_id(name_or_id)], 'det': 'id'}
        else:
            return {'targets': get_events_by_name(name_or_id), 'det': 'name'}
    except IndexError:
        return {'targets': get_events_by_name(name_or_id), 'det': 'name'}


def complete_todo(name_or_id):
    targets = identify_todos(name_or_id)['targets']
    for item in targets:
        item.status = DONE


def delete_todo_by_det(name_or_id):
    targets = identify_todos(name_or_id)['targets']
    for item in targets:
        item.status = DELETED


def show_all_todos():
    targets = [event for event in events if event.status != DELETED]

    targets.sort(key=lambda x: (
        x.status.rank,
        x.get_time_key(),
        -x.points_left,
    ))

    for item in targets:
        item.print_in_line()


def update_event_progress(name_or_id):
    targets = identify_todos(name_or_id)['targets']
    print('progress points completed?')
    delta = int(input())
    for item in targets:
        item.update_progress(delta)


def update_event_status(name_or_id):
    targets = identify_todos(name_or_id)['targets']
    print("change to ordinary/urgent/done ?")
    user_data = input()
    stats_list = [ORDINARY, URGENT, DONE]
    for item in targets:
        try:
            item.status = stats_list[int(user_data) - 1]
        except TypeError or IndexError:
            pass


def update_event_info(name_or_id):
    targets = identify_todos(name_or_id)['targets']
    print("add/rewrite ?")
    mode = int(input()) - 1
    print("text ?")
    text = multiline_input()

    if mode:
        for item in targets:
            item.info = text
    else:
        for item in targets:
            item.info += text


def show_todo(name_or_id):
    if name_or_id == '':
        show_all_todos()
        return
    targets = identify_todos(name_or_id)['targets']
    for item in targets:
        print('common info:\n' + item.get_common_values())
        print('details:\n' + item.info)


def update_event_id(name_or_id):
    targets = identify_todos(name_or_id)['targets']
    if len(targets) != 1:
        print("Can't determine exact ToDo")
    print('new ID (without "@")?')
    user_data = input()
    for item in targets:
        item.id = f'@{user_data}'


def delete_all_todos():
    for item in events:
        item.status = DELETED


def destroy_all_todos():
    print('Are you sure to destruct all ToDo objects? Y/N ?')
    if input().lower() in {'yes', 'y'}:
        events.clear()


def revive_all_todos():
    for item in events:
        if item.status == DELETED:
            item.status = ORDINARY


# temporary commands

def renew():
    aux.printf('Nothing to renew yet', 'highlight')


