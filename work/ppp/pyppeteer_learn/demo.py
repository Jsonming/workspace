#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/3 17:15
# @Author  : yangmingming
# @Site    : 
# @File    : demo.py
# @Software: PyCharm
import asyncio
from pyppeteer import launch


async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('http://example.com')
    await page.screenshot({'path': 'example.png'})
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
