# list 연산 예제

colors = ["red","blue","green"]
colors2 = ['orange', 'black','yellow']

colors + colors2
# 파이썬에서는 print를 하지 않더라도 위에 처럼 입력하면 자동 cmd에서 출력
total_colors = colors + colors2
print(total_colors)
# 서로 다은 list 값 합치기


colors[0] = 'white'
# 특정 인덱스에 새로운 값 입력하기
colors * 2
# list 값 반복하기
print(colors)


colors.append("magenta")
#colors.append("black", "white")
# list에 새로운 변수 추가하기, 인덱스는 맨 마지막에 추가
# append()안에 있는 변수 자체를 추가함, 하나만 가능, ["",""]를 하면 이를 문자열로 받아 들여 그 자체가 들어감
print(colors)

colors.extend(["black", "white"])
print(colors)

colors.insert(0,"pupple")
print(colors)
# 특정 인덱스 번호에 새로운 변수 추가 시

colors.remove("pupple")
# 리스트 내 특정 변수 값 삭제
print(colors)

del colors[0]
# 리스트 내 특정 인덱스 값 삭제
print(colors)


a = [colors ,1,0.1,True]
# 리스트 안에 또다른 리스트를 멤버로 입력 가능
# 이 때 a라는 리스트의 a[0]을 colors 리스트의 주소(첫번째 인덱스)를 가르킴
print(a)
