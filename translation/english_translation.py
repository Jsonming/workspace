#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/12 10:11
# @Author  : yangmingming
# @Site    : 
# @File    : english_translation.py
# @Software: PyCharm
import requests
import execjs
import json


class BaiDuTranslateWeb:
    def __init__(self):
        self.url = "https://fanyi.baidu.com/v2transapi"
        self.headers = {
            "Cookie": "BAIDUID=02725590C792FF940E803CB07B053FEA:FG=1; BIDUPSID=02725590C792FF940E803CB07B053FEA; PSTM=1557990196; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; H_PS_PSSID=1445_21097_29135_29238_28519_29099_28835; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1560304981,1560306621,1560307427,1560307630; yjs_js_security_passport=5385096b0496703a7c9d5b927d5b1b35dc0643ca_1560307633_js; locale=zh; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1560308016",
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Mobile Safari/537.36"
        }
        self.data = {
            "from": "en",
            "to": "zh",
            "query": None,
            "transtype": "translang",
            "simple_means_flag": 3,
            "sign": None,
            "token": "300f465c88543c5218f056447a33a348"
        }

    def get_baidu_sign(self):
        with open("baidusign.js") as f:
            jsData = f.read()
            sign = execjs.compile(jsData).call("e", self.input)
            return sign

    def run(self):
        self.input = "her"
        self.get_baidu_sign()
        self.data["query"] = self.input
        self.data["sign"] = self.get_baidu_sign()
        response = requests.post(url=self.url, data=self.data, headers=self.headers)
        self.result_strs = response.content.decode()
        print(self.result_strs)

    def get_translate_result(self):
        result_dict = json.loads(self.result_strs)
        if 'trans_result' in result_dict:
            result_dict = result_dict['trans_result']['data'][0] if len(
                result_dict['trans_result']['data']) > 0 else None
            result_dict = result_dict['result'][0] if len(result_dict['result']) > 0 else None
            result = result_dict[1] if len(result_dict) > 1 else None
            print("翻译结果为：")
            print(result)
        else:
            print("请输入内容再进行翻译")


if __name__ == '__main__':
    baidutranlate = BaiDuTranslateWeb()
    baidutranlate.run()




c8a14