# -*- coding: utf-8 -*-
"""
@File    : calendar_util.py
@Date    : 2024-04-03
"""
import json
import re

import requests
from parsel import Selector


def get_calendar(year_and_month):
    """
    https://wannianrili.bmcx.com/

    @return:

    {
      "2024-04-01": {
        "class_name": "",
        "comment": "愚人节"
        }
    }
    """

    # https://wannianrili.bmcx.com/ajax/?q=2024-04&v=22121303
    url = 'https://wannianrili.bmcx.com/ajax/'

    params = {
        'q': year_and_month,
        'v': '22121303'
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0"
    }

    res = requests.get(url, params=params, headers=headers)
    sel = Selector(text=res.text)
    rows = sel.css('.wnrl_riqi')

    data = {}
    for row in rows:
        class_name = row.css('a::attr(class)').extract_first('').strip()
        day = row.css('a::attr(onclick)').extract_first('').strip()
        comment = row.css('.wnrl_td_bzl::text').extract_first('').strip()

        ret = re.search('\d{4}-\d{2}-\d{2}', day)
        day = ret.group(0)

        data[day] = {
            'class_name': class_name,
            'comment': comment
        }

    return data


def get_day_item(day):
    """

    @param day:
    @return:
    {
        "class_name": "",
        "comment": "愚人节"
    }
    """
    calendar = get_calendar('-'.join(day.split('-')[:2]))
    # print(json.dumps(calendar, indent=2, ensure_ascii=False))
    return calendar.get(day)


def is_workday(day):
    # 工作日
    workday_class_list = ['', 'wnrl_riqi_ban']

    day_item = get_day_item(day)

    if day_item:
        if day_item.get('class_name') in workday_class_list:
            return True
        else:
            return False


def is_holiday(day):
    # 节假日
    holiday_class_list = ['wnrl_riqi_xiu', 'wnrl_riqi_mo']
    day_item = get_day_item(day)

    if day_item:
        if day_item.get('class_name') in holiday_class_list:
            return True
        else:
            return False

