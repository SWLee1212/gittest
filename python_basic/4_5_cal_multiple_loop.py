# 0 이라는 숫자 입력하기 전까지 계속하여 구구단을 계산하는 프로그램

print("구구단 몇단을 계산할가요? (1~9)")


GetNum = int(input())

while GetNum > 0 and GetNum < 10 :
    for index in range(1,10):
        print(GetNum, "X", index, "=", GetNum * index)

    print("구구단 몇단을 계산할가요? (1~9)")
    GetNum = int(input())

else:
    print("구구단 게임을 종료합니다.")
