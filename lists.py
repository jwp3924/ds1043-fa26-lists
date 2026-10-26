"""lists

Exercises for exploring lists
"""
import os
import stat
from pathlib import Path

def clamp(a: list[int], low: int = 0, high: int = 10) -> None:
    """Modify the values of a to be `low` when they fall below `low` or `high` when the fall above `high`"""
    for i in range(len(a)):
        if a[i] < low:
            a[i] = 'low'
        elif a[i] > high:
            a[i] = 'high'
    return None

# Try writing your own reverse function by actually moving values around rather than
# using reversed, list.reverse, a[::-1], etc
def reverse(a: list) -> None:
    """Reverses the list a in place"""
    reversed_list = []
    for i in range(len(a)):
        reversed_list.append(a[len(a)-(1+i)])
    for j in range(len(a)):
        a[j] = reversed_list[j]
    return None

# Read the following function and write out your prediction of what it will do
# in the following situations:
# - create a list named `susan`. Call `hop_in` multiple times, passing `susan`
#   as the `pouch` argument
#   The first call will print '{name} hops into their mother's pouch'.
#   Subsequent calls will print '{name} hops into their mother's pouch with their siblings: {previous names}'
# - simply call `hop_in` multiple times without specifying a `pouch`
#   The call will print '{name} hops into their mother's pouch' each time.
#
# Now run this in the console. Was your prediction correct?
#   My prediction was wrong. The list of siblings remains from call to call.
def hop_in(name: str, pouch: list[str] = []) -> None:
    if len(pouch) > 0:
        siblings = f' with their siblings: {", ".join(pouch)}'
    else:
        siblings = ''
    print(f"{name} hops into their mother's pouch{siblings}")
    pouch.append(name)

hop_in('James')
hop_in('Adam')
hop_in('Jenny')

# You can point this function a folder on your computer and it will list
# all the files in it and any subfolders. Experiment with how `items` is
# built (Stack vs Queue) and see how the ordering changes.
def list_files(folder_path: str) -> list[str]:
    """Create a list of all files under `root`. Must be given an absolute path as an argument."""
    filenames: list[str] = []
    items = []
    paths = []
    for object in os.listdir(folder_path):
        paths.append(folder_path + '\\' + object)
        items.append(object)
    while len(items) > 0:
        # item =  from `items` here
        item = items.pop(len(items)-1)
        path = paths.pop(len(paths)-1)
        if os.path.isdir(path):  # if the item is a folder...
            # add the contents of item.iterdir() to items
            for thing in os.listdir(path):
                paths.append(path + '\\' + thing)
                items.append(thing)
        else:
            # add item.name to filenames
            filenames.append(item)
    return filenames

# Implement this function using a list as a stack to find matching parentheses
# if a match is not found, raise a ValueError with a helpful message (like the
# index of the unmatched parenthesis)
def match_parentheses(line: str) -> list[str]:
    """Given a string containing an expression, return a list of subexpressions delineated by parenthesis"""
    in_subexpression = False
    subexpression = ''
    subexpressions = []
    for character in line:
        if in_subexpression == False:
            if character == '(':
                in_subexpression = True
            elif character == ')':
                raise ValueError
    return [line]

