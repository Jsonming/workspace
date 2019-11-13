# -*- coding: utf-8 -*-

import pandas as pd
import requests
from lxml import etree

df = pd.DataFrame(columns=["产品名称", "产品编号", "产品描述"])


def request(url):
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0"}
    data = ""
    response = requests.request("GET", url, data=data, headers=headers)
    resp = response.text
    return resp


def info(link):
    resp = request(link)
    html = etree.HTML(resp)

    nodes = html.xpath('//div[@class="details-center"]/div[@class="items f-cb"]')
    content = {}
    for node in nodes:
        node_name = node.xpath('./div[1]//text()')
        node_name = ''.join([name.strip() for name in node_name])
        node_value = node.xpath('./div[2]//text()')
        node_value = ''.join([name.strip() for name in node_value])
        content[node_name] = node_value
        content["录音语种"] = content["数据名称"]
    if not content:
        print(link)
        print(resp)
        with open('a.html', 'a', encoding='utf8') as f:
            f.write(resp)

    return content


for i in range(1, 2):
    url = "http://www.speechocean.com/datacenter/recognition/{}.html?prosearch=#datacenter_do".format(i)
    resp = request(url)
    html = etree.HTML(resp)
    products = html.xpath('//div[@class="tit-list"]/div')
    products_table = []
    for product in products:
        product_url = ''.join(product.xpath('.//a/@href'))
        product_id = ''.join(product.xpath('.//a//div[@class="t0"]/text()'))
        product_name = ''.join(product.xpath('.//a//div[@class="j0"]/text()'))
        content = info(product_url)

        if content:
            product_desc = []
            for key, value in content.items():
                product_desc.append("{}:{}".format(key, value))
            product_desc = '\n'.join(product_desc)
            products_table.append([product_id, product_name, product_desc])

    df_temp = pd.DataFrame(products_table, columns=["产品名称", "产品编号", "产品描述"])
    df = df.append(df_temp, ignore_index=True)
df.to_excel('data.xls', index=False)
