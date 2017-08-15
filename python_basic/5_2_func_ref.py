# 함수의 argument 넘기기

def spam(eggs):
    eggs.append(1)  # 리스트변수에 새로운 값을 삽입 하는 것까지는 링크가 깨어지지 않음
    print("ham ", ham)      # ham은 전역 변수인가??
    eggs = [2,3]    # 리스트에 새로운 변수를 할당하면 이 때 링크가 깨어짐
                    # 해당 변수를 새로운 메모리에 할당됨
    print("ham ", ham)
    print("eggs ", eggs)


def test(t):
    t = 20          # 새로운 할당이 발생하면 객체와 원래 변수 간에 링크가 끊어짐, 메모리 주소가 같은 주소를 가리키지 않음
    print("In Function :",t)


ham = [0]       # 전역 변수 선언인가??
spam(ham)       # ham 리스트 객체를 argument로 하여 함수 호출
print("ham ",ham)


print("================")
x=10
y=20
test(x)
test(y)
print(x, y)
