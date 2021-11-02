import auxilliaries as aux
from database import events, save_progress_and_quit
from main_objects import stat_list
import main_funcs as f_pool


command_names = {
    '.exit': lambda x: save_progress_and_quit(['events.pickle'], [events], True),
    '.save': lambda x: save_progress_and_quit(['events.pickle'], [events], False),
    '.add': lambda x: f_pool.add_todo(),
    '.update_info': lambda x: f_pool.update_event_info(x),
    '.update_status': lambda x: f_pool.update_event_status(x),
    '.update_progress': lambda x: f_pool.update_event_progress(x),
    '.update_id': lambda x: f_pool.update_event_id(x),
    '.show_all': lambda x: f_pool.show_all_todos(),
    '.show': lambda x: f_pool.show_todo(x),
    '.done': lambda x: f_pool.complete_todo(x),
    '.delete': lambda x: f_pool.delete_todo_by_det(x),
    '.delete_all': lambda x: f_pool.delete_all_todos(),
    '.destruct_all': lambda x: f_pool.destroy_all_todos(),
    '.revive_all': lambda x: f_pool.revive_all_todos(),
    '.renew': lambda x: f_pool.renew_deadlines()

}


def refresh_stat():
    for item in events:
        for stat in stat_list:
            if item.status.id == stat.id:
                item.status = stat


def command_handler(input_line):
    user_data = input_line.split('.')
    try:
        arg, command = user_data[0], f'.{user_data[1]}'
    except IndexError:
        print('no such command exists')
        aux.printf('if you want to leave the program, type ".exit"', 'highlight')
        return
    try:
        command_names[command](arg)     # function execution
    except KeyError:
        print('no such command exists')
        aux.printf('if you want to leave the program, type ".exit"', 'highlight')


print('Welcome again in GS-ToDo v 1.3.6')
refresh_stat()

while True:
    try:

        new_line = input()
        if new_line == 'Dude':
            break
    except EOFError or ValueError:
        break
    command_handler(new_line)










