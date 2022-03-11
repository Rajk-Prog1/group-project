import pytest
import string
from src.function1 import *

def remove_chars(inp):

    return "".join([c for c in list(inp) if c not in list(string.ascii_lowercase)])


input_string = open('input_string.txt').read()[:-1]

class TestFunctionOne(object):

    def test_1(self):
        assert remove_chars(input_string) == function1(input_string)

