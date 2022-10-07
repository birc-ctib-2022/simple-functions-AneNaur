"""Exercises with simple functions"""


def prod(a, b, c):
    """
    Compute the product of three numbers.

    >>> prod(1, 2, 3)
    'TEST ME!'
    """
    return a*b*c
    ...

a=10
def prod2(b):
    """
    Get a global a and write to a local c before computing prod(a, b, c)

    >>> prod2(42)
    'TEST ME'
    """
    c=5
    return a*b*c
    ...


def longest(x, y):
    """
    Returning the longest of two lists.

    >>> longest([1, 2, 3], [4, 5])
    'TEST ME'
    """
    if len(x)>len(y):
        return x
    if len(x)<len(y):
        return y
    else:
        return "the two lists are the same length"
    #return x if len(x)>=len(y) else y

    ...


def dist(p1, p2):
    """
    Compute the distance between p1 and p2.

    >>> dist((1,2), (3,4))
    'TEST ME'
    """
    x1, y1 = p1
    x2, y2 = p2
    return sqrt((x1-x2)**2+(y1-y2)**2)
    ...
