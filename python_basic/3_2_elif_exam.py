# elif 예제

print("Tell me your score ? ")
myscore = int(input())        # input으로 입력 받으면 항상 string으로 저장됨 따라서, 숫자로 변환 필요


if (myscore >= 90) :           # ()로 조건문 구분 가능하고 뒤에 반드시 : 붙여야 함
    print("A")                 # 들여쓰기는(indentation) 후 수행명령 입력
    print("Perfect!")
elif(myscore >= 80) :          # elif는 elseif와 같은 구문으로 if 조건이 거짓일 때 실행되는 구문으로
    print("B")                 # 해당 조건이 참인 경우에만 하위 구문이 실행됨
    print("Good!")
elif(myscore >= 70) :
    print("C")
    print("Not bad")  
else:
    print("Get out")            # else  구문뒤에서 반드시 :를 붙여야 함
    print("Bye")
