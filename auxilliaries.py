import colorama as cr
import keyboard as kb
import random as rnd
import time

cr.init()

colors_config_r = {
    'warning': cr.Fore.RED,
    'accepted': cr.Fore.GREEN,
    'fatal_error': cr.Fore.BLUE,
    'highlight': cr.Fore.CYAN,
    'atmospheric': cr.Fore.LIGHTYELLOW_EX,
    'fiasco': cr.Fore.MAGENTA,
}

kb.add_hotkey('ctrl+enter', lambda: kb.write('__________'))


# text decorations

def printf(text, output_format):
    print(f"{colors_config_r[output_format]}{text}{cr.Style.RESET_ALL}")


def reformat(text, fmt):
    return f"{colors_config_r[fmt]}{text}{cr.Style.RESET_ALL}"


def multiline_input():  # Ctr + Enter + Enter to end
    res = ""
    while True:
        line = input()
        if line == '__________':
            break
        res += f"{line}\n"

    return res


# string decorations
def unify_line_length(line, limit):
    try:
        if len(line) <= limit:
            return line + ' '*(limit - len(line) + 2)
        else:
            return line[:limit-1] + '...'
    except TypeError:
        return ' ' * (limit + 2)


def unify_num_length(num, limit):
    s_num = str(num)
    if len(s_num) <= limit:
        return s_num + ' ' * (limit - len(s_num) + 1)
    else:
        return '9'*limit + '+'


# operations with date and time

def convert_to_sec(time_string):
    t_struct = time.strptime(time_string, '%d.%m.%y')
    return time.mktime(t_struct)


def show_time_rem(d, mints=None):
    if mints is None:
        mints = False

    def extra_zero(x):
        return f'0{x}' if len(str(x)) == 1 else x

    factor = int(d.days >= 0)
    sign = '-' if d.days == -1 else ''

    days = d.days if factor else d.days + 1
    full_sec = d.seconds if factor else 86400 - d.seconds
    hours = extra_zero(full_sec // 3600)
    minutes = extra_zero((full_sec % 3600) // 60)

    if mints:
        time_string = unify_line_length(f"{sign}{days}d {hours}h {minutes}m", 12)
    else:
        time_string = unify_line_length(f"{sign}{days}d {hours}h", 9)

    return time_string if factor else reformat(time_string, 'warning')


# common operations

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


# random staff
def array_union(arr):
    ans = []
    for item in arr:
        try:
            for sub_item in item:
                ans.append(sub_item)
        except TypeError:
            ans.append(item)
    return ans


def get_random_sequence(length):
    global alphabet
    return ''.join([rnd.choice(alphabet) for _ in range(length)])


alphabet = array_union([[chr(ord('a') + x) for x in range(26)],
                        [chr(ord('A') + x) for x in range(26)],
                        ['x' for x in range(10)]])






