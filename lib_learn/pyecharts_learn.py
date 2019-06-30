#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/9 23:35
# @Author  : yangmingming
# @Site    :
# @File    : os_learn.py
# @Software: PyCharm

from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot as driver
from pyecharts.globals import ThemeType

bar = (
    Bar()
    .add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
    .add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
    .add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
    .set_global_opts(title_opts=opts.TitleOpts(title="某商场销售情况", subtitle="副标题"))
)


def bar_chart() -> Bar:
    c = (
        # Bar()
        Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
        .add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
        .add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
        .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(position="right"))
        .set_global_opts(title_opts=opts.TitleOpts(title="Bar-测试渲染图片"))
    )
    return c


if __name__ == '__main__':
    # bar.render()
    # make_snapshot(driver, bar_chart().render(), "bar.png")
    bar = bar_chart()
    bar.render()
