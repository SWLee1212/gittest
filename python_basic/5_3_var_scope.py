# 변수의 사용 범위

def test(t):
    print(x)
    t = 20                  # t는 로컬 변수로 함수 내에서만 사용 가능
    print("In func :", t)

def f():
    #global s               # global s로 선언하면 이 s 변수가 전역 변수 s와 같음을 선언하는 것임
    s = "I love London"     # 지역 변수 s 선언 전역 변수 s와 같은 이름이지만, 또 다른 메모리에 지역 변수 선언 형태로 변수 할당
    print(s)

x = 10                      # x는 전역 변수 선언
test(x)
print(t)

s = "I love Paris"          # 전역 변수 s
print(s)
