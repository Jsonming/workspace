#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/12/5 13:12
# @Author  : yangmingming
# @Site    : 
# @File    : temp.py
# @Software: PyCharm
from urllib.parse import quote

ori_url = "https://push.api.bbci.co.uk/p?t=morph%3A%2F%2Fdata%2Fbbc-morph-lx-commentary-latest-data%2FassetUri%2Fnews%252Flive%252Fbusiness-48110448%2Flimit%2F31%2Fversion%2F4.1.27&c=1"
ori_url = "https://push.api.bbci.co.uk/p?t=morph%3A%2F%2Fdata%2Fbbc-morph-lx-commentary-latest-data%2FassetUri%2Fnews%252Flive%252Ftechnology-47078793%2Flimit%2F31%2Fversion%2F4.1.27&c=1"
base_url = "https://push.api.bbci.co.uk/p?"
arg = "morph://data/bbc-morph-lx-commentary-latest-data/assetUri/news%2Flive%2Fbusiness-48110448/limit/31/version/4.1.27"
add_url = "t={}&c=1".format(quote(arg, safe=''))
print(ori_url)
print(base_url + add_url)

url = "https://push.api.bbci.co.uk/p?t=morph%3A%2F%2Fdata%2Fbbc-morph-feature-toggle-manager%2FassetUri%2Fnews%252Flive%252Fbusiness-47739220%2FfeatureToggle%2Fdot-com-ads-enabled%2Fproject%2Fbbc-live%2Fversion%2F1.0.3&c=1&t=morph%3A%2F%2Fdata%2Fbbc-morph-feature-toggle-manager%2FassetUri%2Fnews%252Flive%252Fbusiness-47739220%2FfeatureToggle%2Flx-old-stream-map-rerender%2Fproject%2Fbbc-live%2Fversion%2F1.0.3&c=1&t=morph%3A%2F%2Fdata%2Fbbc-morph-feature-toggle-manager%2FassetUri%2Fnews%252Flive%252Fbusiness-47739220%2FfeatureToggle%2Freactions-stream-v4%2Fproject%2Fbbc-live%2Fversion%2F1.0.3&c=1&t=morph%3A%2F%2Fdata%2Fbbc-morph-lx-commentary-latest-data%2FassetUri%2Fnews%252Flive%252Fbusiness-47739220%2Flimit%2F21%2Fversion%2F4.1.27&c=1&t=morph%3A%2F%2Fdata%2Fbbc-morph-lx-commentary-latest-data%2FassetUri%2Fnews%252Flive%252Fbusiness-47739220%2Flimit%2F31%2Fversion%2F4.1.27&c=1&t=morph%3A%2F%2Fdata%2Fbbc-morph-lx-commentary-latest-data%2FassetUri%2Fnews%252Flive%252Fbusiness-47739220%2Flimit%2F41%2Fversion%2F4.1.27&c=1"
url = "https://push.api.bbci.co.uk/p?t=morph%3A%2F%2Fdata%2Fbbc-morph-feature-toggle-manager%2FassetUri%2Fnews%252Flive%252Ftechnology-47078793%2FfeatureToggle%2Fdot-com-ads-enabled%2Fproject%2Fbbc-live%2Fversion%2F1.0.3&c=1&t=morph%3A%2F%2Fdata%2Fbbc-morph-feature-toggle-manager%2FassetUri%2Fnews%252Flive%252Ftechnology-47078793%2FfeatureToggle%2Flx-old-stream-map-rerender%2Fproject%2Fbbc-live%2Fversion%2F1.0.3&c=1&t=morph%3A%2F%2Fdata%2Fbbc-morph-feature-toggle-manager%2FassetUri%2Fnews%252Flive%252Ftechnology-47078793%2FfeatureToggle%2Freactions-stream-v4%2Fproject%2Fbbc-live%2Fversion%2F1.0.3&c=1&t=morph%3A%2F%2Fdata%2Fbbc-morph-lx-commentary-latest-data%2FassetUri%2Fnews%252Flive%252Ftechnology-47078793%2Flimit%2F21%2Fversion%2F4.1.27&c=1&t=morph%3A%2F%2Fdata%2Fbbc-morph-lx-commentary-latest-data%2FassetUri%2Fnews%252Flive%252Ftechnology-47078793%2Flimit%2F31%2Fversion%2F4.1.27&c=1"
