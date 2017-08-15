# 1~100까지 임의 숫자를 생성하고 이를 맞히는 게임

import random

guess_number = random.randint(1, 10)
print("숫자를 맞춰 보세요(1~10) ")

user_input = int(input())

while user_input is not guess_number :
    if user_input > guess_number :
        print("숫자가 너무 큽니다.")
    else:
        print("숫자가 너무 작습니다.")
    user_input = int(input())
else:
    print("정답입니다.")
    print("임의의 숫자는", guess_number,"입니다.")

print(1 is 1)                   # is, == 와 같은 것
print(1 is not 0)               # is, !=와 같은 구문
