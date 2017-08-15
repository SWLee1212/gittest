import re
import urllib.request


url = "https://docs.python.org/3/library/index.html"
html = urllib.request.urlopen(url)
html_contents = str(html.read())

os_results = re.findall(r"()",html_contents)
#print(html_contents)

for result in os_results:
    print(result)
