# os 모듈을 활용하여 mkdir 실행하기

import os

if not os.path.isdir("log"):
    os.mkdir("log")

FILE_NAME = "log/count_log.txt"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME,"w", encoding="utf8") as my_file:
        my_file.write("기록이 시작 됩니다.\n")
        my_file.close()

with open("log/count_log.txt","a",encoding="utf8") as my_file:
    import random, datetime
    for i in range(1,11):
        stamp = str(datetime.datetime.now())
        value = random.random() * 1000000
        log_line = stamp + "\t" + str(value) + "값이 생성되었습니다." + "\n"
        my_file.write(log_line)
