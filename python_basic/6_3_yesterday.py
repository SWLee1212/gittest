f = open("yesterday.txt",'r')
yesterday_lyric = ""

while 1:
    line = f.readline()
    if not line:
        break
    yesterday_lyric = yesterday_lyric + line.strip() + "\n"

f.close()

n_of_yesterday = yesterday_lyric.count("yesterday")         # 연속하여 내장함수 호출 가능
n_of_Yesterday = yesterday_lyric.count("Yesterday")         # 연속하여 내장함수 호출 가능
print(yesterday_lyric)
print("Number of a Word 'yesterday'", n_of_yesterday)
print("Number of a Word 'Yesterday'", n_of_Yesterday)
