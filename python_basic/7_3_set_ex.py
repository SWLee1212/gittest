# set 자료형 예제
# set 자료형은 데이터의 중복을 허용하지 않음

s=set([1,2,3,1,2,3])

print(s)
print(type(s))
print(type({1,2,3,1,2,3}))

string_ex = "Hello, Hello"
string_ex = set(string_ex)

print(string_ex)

s.add(4)
print(s)
s.remove(1)
print(s)
s.update([1,2,3,4,5,6,7])
print(s)
s.discard(1)
print(s)
s.clear()
print(s)

set_1 = {1,2,3,4,5}
set_2 = {3,4,5,6,7}

print(set_1.union(set_2))
print(set_1 | set_2)
print(set_1.intersection(set_2))
print(set_1 & set_2)
print(set_1.difference(set_2))
print(set_1 - set_2)
