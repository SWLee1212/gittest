# while 문 예제

i = 0
while i<10:         # loop index를 미리 모르는 경우 while이 유리
    print(i)
    i+=1
else:               # for 문이나 while을 끝내고 마지막으로 else 구문을 실행함
    print("1000")

for i in range(10):
    if i==5:
        break       #  반복 제어 수행 중 특정 조건을 만족하면 loop를 빠져 나옴, 유용함
    print(i)
else:               # break 문으로 반본 제어가 중간에 종료되면 else: 구문은 실행 안됨
    print("1000")

print("EOP")

for i in range(10):
    if i==5: continue    #  반복 제어 수행 중 특정 조건을 만족하면 loop를 실행 안함, 구문이 헷갈릴 수 있으므로 잘 안씀
    print(i)
