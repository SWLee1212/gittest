# stack and que 자료 구조

# stack LIFO 구조

a=[1,2,3,4,5]

a.append(20)
a.append(30)
a.append(40)

for index in range(len(a)):
    print(index, a)
    a.pop()

word = "agency for defense development" # str 변수
word_list = list(word)                  # str 변수를 list로 변환
result = []
for index in range(len(word_list)):
    result.append(word_list.pop())      #pop 된 순서대로 문자를 result 리스트에 순차적으로 추가함

print(result)                           #' ', ' ' 분리된 리스트 내 문자열 변수
print("".join(result))                  # join 이라는 함수로 합칠 수 있음
print(word[::-1])


# Queue FIF 구조
a=[1,2,3,4,5]

a.append(20)
a.append(30)
a.append(40)
for index in range(len(a)):
    print(index, a)
    a.pop(0)                            # ()안에 인덱스 값을 뽑아옴. list에는 값이 사라짐
