# 함수 내 지역 변수, 전역 변수 범위 예제

def cal(x,y):
    total =x+y                                          # 전역 변수 total과 이름은 같지만, 지역변수 메모리에 새롭게 할당됨, 함수에서는 지역변수total을 사용
    print("In function")
    print("a: ", str(a), "b:", \
        str(b), "a+b:", str(a+b), "total: ", str(total))
    return total

a = 5
b = 7
total = 0

print("In program -1")
print("a: ", str(a), "b:", \
    str(b), "a+b:", str(a+b), "total: ", str(total))

sum = cal(a,b)
print("After calculation")
print("total :", str(total), "sum:",str(sum))
