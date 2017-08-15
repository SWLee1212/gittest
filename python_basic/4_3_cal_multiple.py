# 구구단 계산기
print("구구단 몇단을 계산할가요?")

GetNum = int(input())

for index in range(1,10):
    print(GetNum, "X", index, "=", GetNum * index)

sentence = "I love you"
reverse_sentence = ""
for index in sentence:
    reverse_sentence = index + reverse_sentence
    print(reverse_sentence)

# 십진수에서 2진수로 변환
decimal = GetNum                            # while 문 안에 loop 인덱스는 미리 선언되어 있어야 함
result = ""                                 # for 문 처럼 loop 내에서 선언할 수 없음
while decimal > 0 :                         # 해당 조건이 참일 때만 실행
    remider = decimal %  2;
    decimal = decimal // 2;
    result = str(remider) + result
else :
    print(result)
