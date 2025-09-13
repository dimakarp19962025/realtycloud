#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 00:14:35 2025

@author: dimakarp1996
"""

import requests

def get_info_by_address(address="г Москва, ул Череповецкая, д 16"):

    url = "https://api.realtycloud.ru/property/info/history"
    
    params = {
        "address": address,
        "table": "sale"
    }
    
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:136.0) Gecko/20100101 Firefox/136.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJJUCI6IjQ2LjEzOC41MS4xMzEiLCJJRCI6Ijg4ZWYwODNjLTkwYTItMTFmMC1hOWJiLTUyNTQwMDIxZTgzZiIsIlJvbGVJRCI6MywiZXhwIjoxNzYwNDAyMzI2fQ.jdBN5spDFSXttemM0uhNBILbZXSUdflRtWCoPoXD4-A",
        "Origin": "https://rc-data.realtycloud.ru",
        "Referer": "https://rc-data.realtycloud.ru/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site"
    }
    
    response = requests.get(url, params=params, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        return data['data']['properties']
    else:
        print(f"Request failed with status code: {response.status_code}")
        print(response.text)
        print(address)
        assert False
