# -*- coding: utf-8 -*-
"""
deserialize json
"""
import json


class DeserializeJson:
    # konstruktor
    def __init__(self, filename):
        print("let's deserialize something")
        tempdata = open(filename, encoding="utf8")
        self.data = json.load(tempdata)

    def somestats(self):
        example_stat = 0
        JST_data = {}
        for dep in self.data:
            typ_JST = dep['typ_JST']
            wojewodztwo = dep['Województwo']
            if typ_JST == 'GM' and wojewodztwo == 'dolnośląskie':
                example_stat += 1
            if wojewodztwo not in JST_data:
                JST_data[wojewodztwo] = {
                    typ_JST: 1
                }
                continue
            if typ_JST in JST_data[wojewodztwo]:
                JST_data[wojewodztwo][typ_JST] += 1
            else:
                JST_data[wojewodztwo][typ_JST] = 1

        print(
            f'liczba urzędów miejskich w województwie dolnośląskim: {str(example_stat)}'
        )
        for wojewodztwo in JST_data:
            print(f"Typy w {wojewodztwo}")
            for typ in JST_data[wojewodztwo]:
                print(f"{typ}: {JST_data[wojewodztwo][typ]}")
