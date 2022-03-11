import pytest
import datetime
from src.function3 import *

input_list_1 = [6, 8, 6]
input_list_2 = [12, 45, 40]
start_of_the_course = [18, 0, 0]


def cal_diff(input_list_1: list, input_list_2: list, start_of_the_course: list):

    inputdate_1 = datetime.datetime(
        datetime.datetime.now().year,
        datetime.datetime.now().month,
        datetime.datetime.now().day,
        input_list_1[0],
        input_list_1[1],
        input_list_1[2],
    )

    inputdate_2 = datetime.datetime(
        datetime.datetime.now().year,
        datetime.datetime.now().month,
        datetime.datetime.now().day,
        input_list_2[0],
        input_list_2[1],
        input_list_2[2],
    )

    startofcoursedate = datetime.datetime(
        datetime.datetime.now().year,
        datetime.datetime.now().month,
        datetime.datetime.now().day,
        start_of_the_course[0],
        start_of_the_course[1],
        start_of_the_course[2],
    )

    return (
        (startofcoursedate - inputdate_1).seconds,
        (startofcoursedate - inputdate_2).seconds,
    )


class TestFunctionThree(object):
    def test_1(self):
        assert cal_diff(input_list_1, input_list_2, start_of_the_course) == function3(
            input_list_1, input_list_2, start_of_the_course
        )
