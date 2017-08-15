# 리스트의 packing unpakcing 예제
# packing을 리스트화 하는 행위 자체로 여러 변수를 하나에 변수로 할당
# unpacking을 리스트로 선언된 멤버 변수를 다수의 변수에 각각 할당

t = [1, 2, 3]

a, b, c = t
# unpakcing 구분
# 할당 하려는 변수 갯수와 리스트 멤버 변수 숫자가 같아야 unpakcing 가능
print(t, a,b,c)
