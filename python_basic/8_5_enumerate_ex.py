# enumerate 예제
# 문자열 변수를 enumerate 하면 문자열을 분리하면서 각 문자열에 인덱스를 붙여줌
words = ['tic', 'tac', 'toe']
for i, v in enumerate(words):
    print(i, v)
enum_words = [[i, v] for i,v in enumerate(words)]
print(enum_words)

print(list(enumerate(words)))
dict_words = {i:v for i,v in enumerate(words)}

print(dict_words)
