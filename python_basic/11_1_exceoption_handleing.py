# 예외처리 구문 예제

for i in range(10):
    try :
        print(i,10//i)                  # 예외 발생 가능한 코드 , 일반적인 코드
    except ZeroDivisionError as e:      # built-in exception에서 미리 정의한 예외 발생 시 메시지
        print(e)
        print("Not divided by 0")

# built-in exception
# IndexError
# NameError
# ZeroDivisionError
# ValueError
# FileNotFoundError


for i in range(10):
    try :
        result = 10/i
    except ZeroDivisionError:           # 예외가 발생하면 실행
        print("Not divided by 0")
    else:                               # 예외가 발생하지 않는 정상적인 구문에서는 실행됨
        print(result)


try :
    for i in range(10):
        result = 10/i
        print(i, result)               # 예외 발생 시 for문은 바로 빠져 나옴        
except ZeroDivisionError:              # 예외가 발생하면 실행
    print("Not divided by 0")
finally:                               # 예외가 발생하지 않는 정상적인 구문에서는 실행됨
    print("Exit")
