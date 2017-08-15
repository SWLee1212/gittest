import urllib.request

url = "http://storage.googleapis.com/patents/grant_full_text/2014/ipg140107.zip"

print("Start Download")
fname, header = urllib.request.urlretrieve(url, "ipg140107.zip")

print(fname)            # 파일 이름
print(header)           # 인터넷과 어떤 정보를 주고 받았는지에 대한 정보

print("End Download")
