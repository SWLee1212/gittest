# split 함수 예제
# 도메인이나 문자열을 검사할 때 적용 가능

items = 'one, two, three'         # split 함수를 호출하면 리스트 변수로 출력됨
print(items.split())              # 함수가 인자가 없으면 빈칸을 기준으로 문자열을 분리하여 unpacking
print(items.split(','))           # 함수 인자가 ',' 문자열이면 문자열을 기준으로 unpacking함

a, b, c = items.split()             # split 함수 출력인 리스트 변수를 다시 unpakcing 함

print(a,b,c)

example = 'cs50.gachon.edu'

print(example.split('.'))
