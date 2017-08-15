
import urllib.request
import re                   # regular expression 모듈


base_url = "http://web.eecs.umich.edu/~radev/coursera-slides/"

html = urllib.request.urlopen(base_url)
html_contents = str(html.read().decode("cp949"))

# print(html_contents)
url_list = re.findall(r"(nlpintro)(.+)Edit(\.)(pdf)", html_contents)

for url in url_list:
    file_name = "".join(url)
    full_url = base_url+file_name                                       # Download 하기 위해서는 base url 주소에 각 주소를 합쳐야 함
    print(full_url)
    fname, header = urllib.request.urlretrieve(full_url,file_name)
    print("End Download")
