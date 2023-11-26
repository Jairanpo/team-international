## Code challenge made with the following requirements:

___

The DataCapture object accepts numbers and returns an object for querying
statistics about the inputs. Specifically, the returned object supports querying
how many numbers in the collection are less than a value, greater than a value,
or within a range. Here’s the program skeleton in Python to explain the
structure:

```python
capture = DataCapture()
capture.add(3)
capture.add(9)
capture.add(3)
capture.add(4)
capture.add(6)
stats = capture.build_stats()
stats.less(4)  # should return 2 (only two values 3, 3 are less than 4)
stats.between(3, 6)  # should return 4 (3, 3, 4 and 6 are between 3 and 6)
stats.greater(4) # should return 2 (6 and 9 are the only two values greater than 4)
```

## Challenge conditions:

1. You cannot import a library that solves it instantly.
2. The methods add(), less(), greater(), and between() should have constant time
   O(1).
3. The method build_stats() can be at most linear O(n).
4. Apply the best practices you know.

## How to use?
___ 
This test was made using python 3.7.6, and there are some string formatting
that will fail if not used with a python version that supports them.

Place your console inside the project directory and directly execute 
the python repl and start building your logic by importing the 
data_capture.py file.

Run python:
```shell
python
```

Then import the module data_capture.py:
```python 
from data_capture import DataCapture
```

Finally, build your data:
```python
from data_capture import DataCapture

capture = DataCapture()
capture = DataCapture()
capture.add(3)
capture.add(9)
capture.add(3)
capture.add(4)
capture.add(6)
stats = capture.build_stats()
stats.less(4)  # should return 2 (only two values 3, 3 are less than 4)
stats.between(3, 6)  # should return 4 (3, 3, 4 and 6 are between 3 and 6)
stats.greater(4) # should return 2 (6 and 9 are the only two values greater than 4)
```

## How to run tests?

Same as before, place your console inside the project directory and from there 
you can run one of the following commands: 
```shell
python -m unittest discover
```
or using the verbose flag:
```shell
python -m unittest discover --verbose
```
