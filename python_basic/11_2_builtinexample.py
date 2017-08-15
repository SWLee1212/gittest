#built-in Exception 에러 메시지 예제

StringEx="123abc"

for value in StringEx:
    try:
        print(int(value))

    except Exception as err :               # 모드 Excetion에 대한 메시지 
        print(err)
