# if-else 구문 예제

print("Tell me your age ? ")
myage = int(input())        # input으로 입력 받으면 항상 string으로 저장됨 따라서, 숫자로 변환 필요


if (myage < 30) :           # ()로 조건문 구분 가능하고 뒤에 반드시 : 붙여야 함
    print("Go insie")       # 들여쓰기는(indentation) 후 수행명령 입력
    print("Welcome")
else:
    print("Get out")            # else  구문뒤에서 반드시 :를 붙여야 함
    print("Bye")

#   x == y
#   x is y          두 변수간 메모리 주소 비교

#  x !=y
# x is not y        두 변수간 메모리 주소 비교

if "abs":           # 0:은 항상 거짓
    print("항상 참")

if "":
    print("항상 거짓")
