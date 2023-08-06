import time


def add(t=1, x=0, y=0):
    """Add node."""
    time.sleep(t)
    return x + y


def minus(t=1, x=0, y=0):
    """Minus node."""
    time.sleep(t)
    return x - y


def power(t=1, x=0, y=0):
    """Power node."""
    from math import pow

    time.sleep(t)
    return pow(x, y)


def greater(t=1, x=0, y=0):
    """Greater than node"""
    time.sleep(t)
    return x > y


def less(t=1, x=0, y=0):
    """Less than node"""
    time.sleep(t)
    return x < y


def sqrt(t=1, x=1):
    """sqrt node"""
    from math import sqrt

    time.sleep(t)
    return sqrt(x)


def test_range(start=0, stop=5, step=1):
    """Range node"""
    return list(range(start, stop, step))


class Person:
    name = "Bob"
    age = 5

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def run(self):
        return self

    def __repr__(self) -> str:
        s = "Person(name={}, age={})".format(self.name, self.age)
        return s


def person(name, age):
    return Person(name, age)
