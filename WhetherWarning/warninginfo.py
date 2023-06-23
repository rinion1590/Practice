#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
import urllib.request
import os.path

base = os.path.dirname(os.path.abspath(__file__))

WEATHER_TRANS = json.load(open(base + "/transweather.json", "r"))
OFFICES_AREA_CODE = "120000" #地方エリアのコード
CLASS_AREA_CODE = "1210000" #市町村区のコード
AREA_URL = "https://www.jma.go.jp/bosai/common/const/area.json"

url = "https://www.jma.go.jp/bosai/warning/data/warning/%s.json" % (OFFICES_AREA_CODE)
def warnings():
        area_data = urllib.request.urlopen(url=AREA_URL)
        area_data = json.loads(area_data.read())
        area = area_data["class20s"][CLASS_AREA_CODE]["name"]
        warning_info = urllib.request.urlopen(url=url)
        warning_info = json.loads(warning_info.read())
        warning_codes = [warning["code"]
                        for class_area in warning_info["areaTypes"][1]["areas"]
                        if class_area["code"] == CLASS_AREA_CODE
                        for warning in class_area["warnings"]
                        if warning["status"] != "解除" and warning["status"] != "発表警報・注意報はなし"]
        warning_texts = [WEATHER_TRANS["warninginfo"][code] for code in warning_codes]
        return (warning_texts,area)
import requests

def main():
    url = "https://notify-api.line.me/api/notify"
    token = "qyk3XkjKFUGpIJuTzljUsyxgSiEXCBOeSSZuBxov8f0"
    headers = {"Authorization" : "Bearer "+ token}
    war=(' '.join((warnings()[0])))
    if warnings()[0] == []:
        message="現在発表されている警報はありません。"
    else:
        message = "現在発表されている情報:"+war  
    payload = {"message" :  message}

    r = requests.post(url ,headers = headers ,params=payload)

if __name__ == '__main__':
    main()
