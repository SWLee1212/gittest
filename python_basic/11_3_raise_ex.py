#raise 예제

while True:
    Value = input("변환할 정수값을 입력하시오.")

    for digit in Value:
        if digit not in "0123456789":
            raise ValueError("숫자값을 입력하지 않았습니다.")            # 에러 발생 시 예외 처리 구문을 cmd창에 띄우고 프로그램을 종료시킴
        print("정수값으로 변환된 숫자 - ", int(Value))
