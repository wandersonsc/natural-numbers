import pytest


def sum_natural_numbers(n):

    if n <= 1:
        return n
    return n + sum_natural_numbers(n - 1)


def test_sum_natural_numbers():
    """ Test the natural number fuction """

    n = 10
    assert sum_natural_numbers(n) == 55
