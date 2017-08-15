def add(x,y):
    return x+y

def multi(x,y):
    return x*y

def divide(x,y):
    return x/y

def main():
    base_line = float(input("밑변의 길이는?"))
    upper_line = float(input("윗변의 길이는?"))
    height = float(input("높이는?"))

    area = divide(add(base_line,upper_line)*height,2)
    print(area)

# python shell에 직접 들어가지 않고, cmd 창에서 python 파일 이름을 치면
# 아래 구문이 실행됨

if __name__ == '__main__':
    main()
#    print(add(10,2))
#    print(multi(10,2))
#    print(divide(10,2))
#_가 두번 들어가면? python shell에서 import 할 때 에러가 발생


#점프 투 파이썬 - https://wididocs.net/book/1
#코드아카데미 - https://www.codeacademy.com
#코드파이트 - https://codefights.com
#생활코딩 - https://opentutorials.org/course
#코세라 - https://www.coursera.org
