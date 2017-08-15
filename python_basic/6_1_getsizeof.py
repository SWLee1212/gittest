import sys

print("문자열 사이즈 a, ab, abc : ", sys.getsizeof("a"), sys.getsizeof("ab"), sys.getsizeof("abc"))
# 문자열 하나는 1byte 메모리 사이즈가 필요함
# 문자 하나의 경우 getsizeof() 하면 32비트 컴퓨터 인경우 26비트가 기본적으로 필요함
# 이는 파이썬에서 기본적으로 문자열을 저장하기 위하여 약 25byte 공간이 필요하기 때문
print("boolean 사이즈 : ",sys.getsizeof(True))
print("int 사이즈 : ",sys.getsizeof(1))
print("float 사이즈 : ",sys.getsizeof(1.11))

#문자열 인덱싱 방안
# 왼쪽과 오른쪽 인덱싱이 모두 가능함,
#왼쪽에서 카운트할 경우 0,1,2, 순으로 인덱싱
#오른쪽에서 카운트할 경우 -1,-2,-3 순으로 인덱싱

a="Hello"

print(a[0], a[4])
print(a[-1], a[-5])

a="Agency for Defense Development"

print(a[0:6])         # 인덱스 0을 포함하여 -> 방향으로 6까지 출력
print(a[0:])          # 인덱스 0을 포함하여 -> 방향으로 끝까지 출력
print(a[-11:])        # -11번부터 -> 방향으로 끝가지 출력
print(a[-11:-5])      # -11번부터 -> 방향으로 6글자 출력
print(a[:])
print(a[-50:50])      # 인덱스 값 범위를 넘어서면 자동으로 처음과 끝을 출력
#print(a[-50])         # 인덱스 값 범위를 넘어선 특정 값을 출력하는 것은 안됨
print(a[::2])         # 인덱스 0부터 -> 방향으로 2칸씩 띄어진 값
print(a[5::2])         # 인덱스 5부터 -> 방향으로 2칸씩 띄어진 값
print(a[-1::-2])      # 인덱스 0부터 <- 2칸씩 띄어진 값

a = "Agency"
b = "for Defense"

print(a * 2)

if 'g' in a:
    print("g is in the string.")
else :
    print("g is not in the string.")
