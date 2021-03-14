# import unittest
import os

def func(x):
    os.system('/bin/grep' + x)
    return 1


def test_answer():
    assert func(' --help') == 1
