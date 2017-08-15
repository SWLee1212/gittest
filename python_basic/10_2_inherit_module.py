# 파이썬 내장 모듈

import random

random.randint(1,10)
random.random()

import os
os.system("cls")

import urllib.request
r = urllib.request.urlopen("http://google.co.kr")
r.read()
