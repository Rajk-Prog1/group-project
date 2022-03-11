import pytest
from src.function2 import *

switchdict = {",": "+", "#": "-"}
reverse_switchdict = {v: k for k, v in switchdict.items()}
input_string = open('input_string.txt').read()[:-1]

def replace_chars(inp):

    for k, v in reverse_switchdict.items():
        inp = inp.replace(k, v)

    return inp

class TestFunctionTwo(object):

    def test_1(self):
        assert replace_chars(input_string) == function2(input_string)