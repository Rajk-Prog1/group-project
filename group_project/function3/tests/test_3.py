import datetime

from function3 import *

input_list_1 = [3, 38, 6]
input_list_2 = [10, 15, 40]
start_of_the_course = [15, 30, 0]


def cal_diff(input_list_1: list, input_list_2: list, start_of_the_course: list):

    # Any fixed day works; only the time of day matters.
    day = datetime.date(2000, 1, 1)

    inputdate_1 = datetime.datetime.combine(day, datetime.time(*input_list_1))
    inputdate_2 = datetime.datetime.combine(day, datetime.time(*input_list_2))
    startofcoursedate = datetime.datetime.combine(
        day, datetime.time(*start_of_the_course)
    )

    return (
        int((startofcoursedate - inputdate_1).total_seconds()),
        int((startofcoursedate - inputdate_2).total_seconds()),
    )


class TestFunctionThree:
    def test_3(self):
        assert cal_diff(input_list_1, input_list_2, start_of_the_course) == function3(
            input_list_1, input_list_2, start_of_the_course
        )
