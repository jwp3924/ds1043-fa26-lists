"""lists

Exercises for exploring lists
"""

from pathlib import Path


def clamp(a: list[int], low: int = 0, high: int = 10) -> None:
    """Modify the values of a to be `low` when they fall below `low` or `high` when the fall above `high`"""
    for i in range(len(a)):
        if a[i] < low:
            a[i] = 'low'
        elif a[i] > high:
            a[i] = 'high'
    return None

numlist = [-5,2,7,-3,12,19]
print(numlist)
clamp(numlist)
print(numlist)

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

letterlist = ['a','b','c','d','e']
print(letterlist)
reverse(letterlist)
print(letterlist)

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
def hop_in(name: str, pouch: list[str] = []) -> None:
    if len(pouch) > 0:
        siblings = f' with their siblings: {", ".join(pouch)}'
    else:
        siblings = ''
    print(f"{name} hops into their mother's pouch{siblings}")
    pouch.append(name)


# You can point this function a folder on your computer and it will list
# all the files in it and any subfolders. Experiment with how `items` is
# built (Stack vs Queue) and see how the ordering changes.
def list_files(folder: str) -> list[str]:
    """Create a list of all files under `root`"""
    root = Path(folder)
    filenames: list[str] = []
    items: list[Path] = []
    while len(items) > 0:
        # item =  from `items` here
        if item.is_dir():  # if the item is a folder...
            # add the contents of item.iterdir() to items
        else:
            # add item.name to filenames
    return filenames


# Implement this function using a list as a stack to find matching parentheses
# if a match is not found, raise a ValueError with a helpful message (like the
# index of the unmatched parenthesis)
def match_parentheses(line: str) -> list[str]:
    """Given a string containing an expression, return a list of subexpressions delineated by parenthesis"""
    return [line]

