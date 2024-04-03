# china-calendar

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/china-calendar)](https://pypi.org/project/china-calendar)
[![PyPI](https://img.shields.io/pypi/v/china-calendar.svg)](https://pypi.org/project/china-calendar)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/china-calendar?label=pypi%20downloads)](https://pypi.org/project/china-calendar)
[![PyPI - License](https://img.shields.io/pypi/l/china-calendar)](https://github.com/mouday/china-calendar/blob/master/LICENSE)
[![GitHub release](https://img.shields.io/github/v/release/mouday/china-calendar)](https://github.com/mouday/china-calendar/releases)
[![GitHub Stars](https://img.shields.io/github/stars/mouday/china-calendar?color=%231890FF&style=flat-square)](https://github.com/mouday/china-calendar)

a calendar about china

判断某一天是否为工作日或者是法定节假日，仅适用于中国

安装

```bash
pip install china-calendar
```

使用示例：

```python
import china_calendar

# 清明节
assert china_calendar.is_holiday('2024-04-04') == True

assert china_calendar.is_workday('2024-04-04') == False
```

类似的库：

- [https://github.com/LKI/chinese-calendar](https://github.com/LKI/chinese-calendar)
