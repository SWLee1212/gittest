# join 함수 예제
# 분리되어 있는 리스트 변수 내 문자열을 어떠한 기준으로 합치는 기능

example = ['one', 'two', 'three']   # 리스트 내부에 문자열간의 구분은 쉼표로 가능함

print("".join(example))             # 함수 입력에 문자열로 선언된 리스트 변수를 입력
                                    # 앞에 입력은 문자열을 합칠 때 조건
print(", ".join(example))           # 함수 출력은 합쳐진 문자열
print("-".join(example), type("-".join(example)))


print(example[::-1])                # 문자열 또는 리스트 변수 접근 시 [] 임!!
