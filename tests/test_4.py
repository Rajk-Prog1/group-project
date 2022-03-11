import pytest
from src.function4 import *


inp1 = 345
inp2 = 45735


def bcommon_div(inp1, inp2):

    max_oszto = 1

    for i in range(2, inp1 // 2 + 1):
        if inp1 % i == 0 and inp2 % i == 0:
            max_oszto = i

    return max_oszto


class TestFunctionFour(object):
    def test_1(self):
        assert bcommon_div(inp1, inp2) == function4(inp1, inp2)
