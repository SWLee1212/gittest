import urllib.request
import re

url = "http://finance.naver.com/item/main.nhn?code=005930"
html = urllib.request.urlopen(url)
html_contents = str(html.read().decode("ms949"))

stock_results = re.findall("(\<dl class=\"blind\"\>)([\s\S]+?)(\<\/dl\>)", html_contents)
samsung_stock = stock_results[0]
samsung_index = samsung_stock[1]            # 괄호에 따라 튜플 리스트가 발생


index_list = re.findall("(\<dd\>)([\s\S]+?)(\<\/dd\>)",samsung_index)        # 모든 문자, [a-zA-Z]보다 포괄적임

print(index_list)       # 변수가 3개인 튜플 리스트가 발생
for index in index_list:
    print (index[1].split(" "))
