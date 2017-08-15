# zip 예제
# 길이가 같은 여러 개이 문자열 리스트 변수를 zip 하면 각 인덱스 별로 묶을 수 있음
list_a = ['a','b','c']
list_b = ['d','e','f']
list_c = ['g','h','i']

list_sum = [i for i in zip(list_a, list_b, list_c)]     # 이 때 튜플 변수로 묶어진다.
print(list_sum, type(list_sum), type(list_sum[0]))

for a, b,c in zip(list_a,list_b,list_c):
    print(a,b,c)

print([sum(x) for x in zip((1,2,3),(10,20,30),(100,200,300,400))])

list_a = ['a1','b1','c1']
list_b = ['a2','b2','c2']
print([[i, x] for i,x in enumerate(zip(list_a,list_b))])
