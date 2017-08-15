import urllib.request
import re


url= "http://www.google.com/googlebooks/uspto-patents-grants-text.html"

html = urllib.request.urlopen(url)
html_contents = str(html.read().decode("cp949"))  #html 파일 읽고, 문자열로 변환
# cp949는 윈도우 용
# utf8은 리눅스 용

url_list = re.findall(r"(http)(.+)(zip)", html_contents)        # 튜플값으로 반환됨 나누어서 반환됨

# for url in url_list:
#     print("".join(url))
