import pytest
from src.function5 import *

input_string = "asdlkajnfpibwf891763t4ohbdiweuzrg91823gzbdockjwdehbf9kllhjbaefizgiweuzdbiwuezgrweuzgfh98437wzgrh"
input_int = 3


def select_chars(input_string, input_int):

    return "".join(
        [
            input_string[k * input_int - 1]
            for k in range(1, int(len(input_string) / input_int) + 1)
        ]
    )


class TestFunctionFive(object):
    def test_1(self):
        assert select_chars(input_string, input_int) == function5(
            input_string, input_int
        )
