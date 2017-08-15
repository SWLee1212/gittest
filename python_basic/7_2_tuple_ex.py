# 튜플 example
# 튜플을 리스트 자료형과 유사하나 한번 선언 및 데이터 할당 이후
# 변경이 불가함
# 그 외 리스트의 함수를 동일하게 사용 가능


a = (1,2,3)     # 튜플 자료형 선언 ()안에 데이터를 assign 하는 것이 특징

print(a+a, a*3)
print(len(a))

#a[0] = 1        # 이와 같이 새로운 값을 assign 하는 것은 불가함

t=(1)
print(type(t))

t=(1,)
print(type(t))
