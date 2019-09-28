# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 17:01:37 2019

@author: Kritartha Patowary
"""

import requests
import json
response = requests.get("https://jsonplaceholder.typicode.com/todos")
if response.status_code==200:
    todos= json.loads(response.text)
    print(todos)
print(type(todos))