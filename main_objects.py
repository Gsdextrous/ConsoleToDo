import auxilliaries as aux
import datetime as dat
import time
import math


class Status:
    def __init__(self, name, rank, fmt=None, id=None):
        self.name = name
        self.rank = rank
        self.fmt = fmt
        self.id = id

    def show(self):
        if self.fmt is None:
            return self.name
        else:
            try:
                return aux.reformat(aux.unify_line_length(self.name, 15), self.fmt)
            except KeyError or ValueError:
                return self.name


DONE = Status('Completed', 3, 'accepted', id='000')
ORDINARY = Status('Ordinary task', 2, 'highlight', id='001')
URGENT = Status('Urgent task', 1, 'warning', id='010')
DELETED = Status('---', 4, id='011')
FAILURE = Status('Failed', 5, 'fiasco', id='101')   # will appear in further updates
OVERDUE = Status('Overdue task', 6, 'fiasco', id='110')   # will appear in further updates

stat_list = [DONE, ORDINARY, URGENT, DELETED]


class ToDo:
    def __init__(self, name=None, info=None, points_left=None, deadline=None, status=ORDINARY, id=None):
        self.name = name
        self.info = info
        self.points_left = points_left
        self.deadline = deadline
        self.status = status
        self.id = id

    def set_deadline(self, date):
        try:
            self.deadline = aux.convert_to_sec(date)
        except TypeError:       # when reaching NoneType
            self.deadline = math.inf
        pass

    def get_time_key(self):
        return -self.deadline * aux.sign(self.deadline - time.time())

    def get_time_rem(self):
        if self.status == DONE:
            return aux.unify_line_length("--/--", 9)
        elif self.deadline == math.inf:
            return aux.reformat(aux.unify_line_length('+inf', 9), 'highlight')
        delta = dat.datetime.fromtimestamp(self.deadline) - dat.datetime.now()
        return aux.show_time_rem(delta)

    def update_progress(self, delta_points):
        self.points_left -= delta_points
        if self.points_left <= 0:
            self.status = DONE
            self.points_left = 0
        elif self.status == DONE:
            self.status = ORDINARY

    def print_in_line(self):
        print(f"{self.status.show()} | {aux.unify_line_length(self.name, 14)} | "
              f"time left: {self.get_time_rem()} | "
              f"{aux.reformat(aux.unify_num_length(self.points_left, 2), 'highlight')} pts left"
              f" | {aux.reformat('ID', 'highlight')} {self.id}")

    def get_common_values(self):
        s = f"{self.status.show()} | {self.name} | " \
            f"active till {self.deadline} | " \
            f"{aux.reformat(str(self.points_left), 'highlight')} pts left" \
            f" | {aux.reformat('ID', 'highlight')} {self.id}"

        return s




