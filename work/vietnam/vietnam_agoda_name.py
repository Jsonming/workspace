#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 17:21
# @Author  : yangmingming
# @Site    : 
# @File    : vietnam_agoda_name.py
# @Software: PyCharm


import requests
import json
from lxml import etree


class DemoSpider(object):
    def __init__(self):
        self.resp = None
        self.result = []

    def crawl(self, off_number=None):
        url = "https://www.agoda.com/api/vi-vn/Main/GetSearchResultList"

        querystring = {"cid": "1463261"}
        payload = {"SearchMessageID":"96a8426d-01b2-4784-8310-830a848800c5","IsPollDmc":"false","SearchType":1,"ObjectID":0,"HashId":"null","Filters":{"PriceRange":{"IsHavePriceFilterQueryParamter":"false","Min":0,"Max":0},"ProductType":[-1],"HotelName":""},"SelectedColumnTypes":{"ProductType":[-1]},"RateplanIDs":"null","TotalHotels":3582,"PlatformID":1001,"CurrentDate":"2019-04-18T16:47:03.1581023+07:00","SearchID":991110418164703100,"CityId":13170,"Latitude":0,"Longitude":0,"Radius":0,"RectangleSearchParams":"null","PageNumber":2,"PageSize":45,"SortOrder":1,"SortField":0,"PointsMaxProgramId":0,"PollTimes":0,"RequestedDataStatus":0,"MaxPollTimes":4,"CityName":"Hồ Chí Minh","ObjectName":"Hồ Chí Minh","AddressName":"null","CountryName":"Vietnam","CountryId":38,"IsAllowYesterdaySearch":"false","CultureInfo":"vi-VN","CurrencyCode":"CNY","UnavailableHotelId":0,"IsEnableAPS":"false","SelectedHotelId":0,"IsComparisonMode":"false","HasFilter":"false","LandingParameters":{"HeaderBannerUrl":"null","FooterBannerUrl":"null","SelectedHotelId":0,"LandingCityId":13170},"NewSSRSearchType":0,"IsWysiwyp":"false","RequestPriceView":"null","FinalPriceView":"null","MapType":3,"IsShowMobileAppPrice":"false","IsApsPeek":"false","IsRetina":"false","IsCriteriaDatesChanged":"false","TotalHotelsFormatted":"3.582","PreviewRoomFinalPrice":"null","ReferrerUrl":"null","CountryEnglishName":"Vietnam","CityEnglishName":"Ho Chi Minh City","Cid":1463261,"Tag":"null","ProductType":-1,"NumberOfBedrooms":[],"ShouldHideSoldOutProperty":"false","FamilyMode":"false","isAgMse":"false","ccallout":"false","defdate":"false","BankCid":"null","BankClpId":"null","Adults":2,"Children":0,"Rooms":1,"CheckIn":"2019-06-29T00:00:00","LengthOfStay":1,"ChildAges":[],"DefaultChildAge":8,"ChildAgesStr":"null","CheckOut":"2019-06-30T00:00:00","Text":"Hồ Chí Minh","IsDateless":"false","CheckboxType":0,"TravellerType":1}


        headers = {
            "cache-control": "no-cache",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
            "X-Foody-Api-Version": "1",
            "X-Foody-App-Type": "1004",
            "X-Foody-Client-Type": "1",
            "X-Foody-Client-Version": "1"
        }
        # response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
        response = requests.request("POST", url, data=payload, headers=headers)
        self.resp = response.text

    def parser(self):
        response = json.loads(self.resp)
        stores = response.get("ResultList")
        for store in stores:
            store_name = store.get("HotelDisplayName")
            self.result.append(store_name)

    def save(self):
        result = list(set(self.result))
        print(len(result))
        print(result)
        with open(r'C:\Users\Administrator\Desktop\name.txt', 'a', encoding='utf-8')as f:
            f.write('\n'.join(result))

    def run(self):
        self.crawl()
        self.parser()
        self.save()


if __name__ == '__main__':
    demo = DemoSpider()
    demo.run()
