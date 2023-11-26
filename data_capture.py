# -*- coding: utf-8 -*-
# Standard library:
from functools import wraps
# -- -- -- -- -- -- -- -- -- -- -- -- -- --
# Third party:
# -- -- -- -- -- -- -- -- -- -- -- -- -- --
# project:
# =============================================================================


def validate_int_only_arguments(fn):
    @wraps(fn)
    def wrapper(*args):
        list_of_values = args[1:]
        if not all(isinstance(number, int) for number in list_of_values):
            raise Exception(
                f'< {fn.__name__} > only accepts integer arguments.'
            )

        return fn(*args)

    return wrapper


def validate_input_amount(amount):
    def wrapper(fn):
        @wraps(fn)
        def inner(*args):
            if len(args) != amount + 1:
                raise Exception(
                    f'< {fn.__name__} > require {amount} arguments.'
                )

            return fn(*args)

        return inner

    return wrapper


class DataCapture(object):

    def __init__(self):
        self._list_of_values = []

    @property
    def values(self):
        return self._list_of_values

    @validate_input_amount(1)
    @validate_int_only_arguments
    def add(self, value):
        self._list_of_values.append(value)

    def build_stats(self):
        if len(self._list_of_values) < 1:
            raise Exception('You haven\'t add values')

        self._list_of_values.sort()

        _stats = {}
        for i, n in enumerate(self._list_of_values):
            if str(n) not in _stats:
                _stats.update({
                    str(n): i
                })
            else:
                continue

        return Stats(self._list_of_values, _stats)


class Stats(object):
    def __init__(self, values, stats):
        self.values = values
        self._stats = stats

    @validate_input_amount(1)
    @validate_int_only_arguments
    def less(self, value):
        _end = self._stats[str(value)]
        return self.values[:_end]

    @validate_input_amount(2)
    @validate_int_only_arguments
    def between(self, start, end):
        _start = self._stats[str(start)]
        _end = self._stats[str(end)] + 1

        return self.values[_start: _end]

    @validate_input_amount(1)
    @validate_int_only_arguments
    def greater(self, value):
        _start = self._stats[str(value)] + 1
        return self.values[_start:]
