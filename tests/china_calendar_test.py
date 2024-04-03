# -*- coding: utf-8 -*-
"""
@File    : china_calendar_test.py
@Date    : 2024-04-03
"""
import unittest
import china_calendar


class ChinaCalendarTest(unittest.TestCase):
    def test_is_holiday(self):
        # 清明节
        assert china_calendar.is_holiday('2024-04-04') == True

    def test_is_workday(self):
        # 清明节
        assert china_calendar.is_workday('2024-04-04') == False
