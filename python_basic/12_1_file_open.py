# file open 예제

# my_file = open("i_have_a_dream.txt","r")
# contents = my_file.read()                   # read()함수로 읽으면 본문은 string 형태로 읽어드림
# print(type(contents))
# my_file.close()                             # close()하지 않으면 해당 파일을 open, read 한 후에 계속해서 파일 접근 권한을 점유하고 있어서
#                                             # 다른 프로그램에서 접근이 불가함
#                                             # 따라서 파일 처리가 끝나면 close 해주는 것이 좋음
#
# #with 구문을 사용하여 파일을 open하면 with 의 indentatoin 구문이 끝나면 파일 close 자동으로 실행됨
# with open("i_have_a_dream.txt","r") as my_file:
#     contents = my_file.read()
#     print(type(contents))
#
#
# with open("i_have_a_dream.txt","r") as my_file:
#     contents_list = my_file.readlines()             # txt 파일을 \n 단위로 구분하여 리스트 변수화 함
#     print(type(contents_list), contents_list)
#     print(len(contents_list))

# with open("i_have_a_dream.txt","r") as my_file:
#     i=0
#     while True:
#         line = my_file.readline().replace("\n","")
#
#         if line.strip() != "":
#             continue                        # 해당 구문이 참이면 아래 구문을 실행하지 않고 위로 올라감
#         if not line:
#             break
#         print(str(i)+"===="+line)
#         i += 1
i=0
while i<5:
    i +=1
    if i == 3:
        continue
    print(i)
