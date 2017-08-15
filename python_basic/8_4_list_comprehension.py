# list comprehension 예제
# 리스트를 생성할 때 보다 python 다운 방법으로 생성 가능함

result = [i for i in range(10)]
print(result)

result = [i for i in range(10) if i % 2 is 0]
print(result)

num_1 = ['0','1','2','3','4']
num_2 = ['5','6','7','8','9']

num = [i+j for i in num_1 for j in num_2]
print(num)

char_1 = ['a', 'b','c']
char_2 = ['d', 'e','a']

result = [i+j for i in char_1 for j in char_2 if not(i == j)]
result.sort()
print(result)

words = 'the quick brown fox jumps over the lazy dog'.split()

w = [[i.upper(), i.lower(), len(i)] for i in words]
print(w)

for i in w:
    print(i)
