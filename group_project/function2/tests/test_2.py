from pathlib import Path

from function2 import *

switchdict = {",": "+", "#": "-"}
reverse_switchdict = {v: k for k, v in switchdict.items()}
# Task 2 reuses the input file that lives in the function1 folder.
input_string = (Path(__file__).parents[2] / "function1" / "input_string.txt").read_text(encoding="utf-8")[:-1]


def replace_chars(inp):

    for k, v in reverse_switchdict.items():
        inp = inp.replace(k, v)

    return inp


class TestFunctionTwo(object):

    def test_2(self):
        assert replace_chars(input_string) == function2(input_string)
