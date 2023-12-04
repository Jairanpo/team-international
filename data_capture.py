# -*- coding: utf-8 -*-
from functools import wraps

def validate_input_amount(amount):
    """
    Decorator to validate the number of arguments passed to a function.

    Args:
        amount (int): The expected number of arguments.

    Raises:
        Exception: If the number of arguments is not equal to 'amount'.

    Returns:
        function: The decorated function.
    """
    def wrapper(fn):
        @wraps(fn)
        def inner(*args):
            if len(args) != amount + 1:
                raise Exception(f"< {fn.__name__} > requires {amount} arguments.")
            return fn(*args)
        return inner
    return wrapper

class DataCapture(object):
    """
    Class for capturing and processing data.

    Attributes:
        _dict_values (dict): A dictionary to store captured data.
        _largest_index (int): The largest index of captured data.
    """

    def __init__(self):
        self._dict_values = {}
        self._largest_index = 0

    @validate_input_amount(1)
    def add(self, value):
        """
        Add a value to the data capture.

        Args:
            value (int): The value to be added.

        Returns:
            None
        """
        key = str(value)
        if value > self._largest_index:
            self._largest_index = value

        if self._dict_values.get(key):
            self._dict_values[key].append(value)
        else:
            self._dict_values[key] = [value]

    def build_stats(self):
        """
        Build statistics based on the captured data.

        Returns:
            Stats: A Stats object containing statistics.
        """
        _stats = {}
        sorted_values = []
        for i in range(self._largest_index + 1):
            key = str(i)
            if self._dict_values.get(key) is not None:
                _stats.update({key: len(sorted_values)})
                sorted_values.extend(self._dict_values.get(key))
        return Stats(sorted_values, _stats)

class Stats(object):
    """
    Class for computing statistics on captured data.

    Attributes:
        values (list): A list of captured values.
        _stats (dict): A dictionary containing statistics.
    """

    def __init__(self, values, stats):
        self.values = values
        self._stats = stats

    @validate_input_amount(1)
    def less(self, value):
        """
        Get values less than a specified value.

        Args:
            value (int): The threshold value.

        Returns:
            list: A list of values less than 'value'.
        """
        _end = self._stats[str(value)]
        return self.values[:_end]

    @validate_input_amount(2)
    def between(self, start, end):
        """
        Get values within a specified range.

        Args:
            start (int): The start of the range (inclusive).
            end (int): The end of the range (inclusive).

        Returns:
            list: A list of values within the specified range.
        """
        _start = self._stats[str(start)]
        _end = self._stats[str(end)] + 1
        return self.values[_start:_end]

    @validate_input_amount(1)
    def greater(self, value):
        """
        Get values greater than a specified value.

        Args:
            value (int): The threshold value.

        Returns:
            list: A list of values greater than 'value'.
        """
        _start = self._stats[str(value)] + 1
        return self.values[_start:]

