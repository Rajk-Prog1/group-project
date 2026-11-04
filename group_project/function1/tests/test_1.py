import string
from pathlib import Path

from function1 import *


def remove_chars(inp):

    return "".join([c for c in list(inp) if c not in list(string.ascii_lowercase)])


input_string = (Path(__file__).parent.parent / "input_string.txt").read_text(
    encoding="utf-8"
)[:-1]


class TestFunctionOne:
    def test_1(self):
        assert remove_chars(input_string) == function1(input_string)
