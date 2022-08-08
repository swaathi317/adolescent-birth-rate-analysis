#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: swaathi
"""

import json


def main():
    with open("birthRateRaw.json") as json_file:
        data = json.load(json_file)

    data = data['fact']

    birthRate = []

    for singleData in data:
        bRateObj = {
            "Year": singleData['dim']['YEAR'],
            "Region": singleData['dim']['REGION'],
            "Country": singleData['dim']['COUNTRY'],
            "Birth rate": singleData['Value']
        }
        # take data that have age group between 15-19 years
        if(singleData['dim']['AGEGROUP'] == "15-19 years"):
            birthRate.append(bRateObj)

    with open('../Data_Analysis/cleanedBirthRate.json', 'w') as out:
        json.dump(birthRate, out)


if __name__ == '__main__':
    main()
