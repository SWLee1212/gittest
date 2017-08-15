# 함수 선언 및 실행 예제

def cal_rec_are(x,y):               #함수 선언 및 구현 (x,y)는 함수의 parameter로 칭함
    print("사각형 넓이 계산 함수")
    return x*y                      #함수가 미리 선언 되더라고 인터프리터는 코드의 첫줄을 훝어내려가면 함수의 존재만 파악
                                    #실재 함수가 호출되는 순간에 함수가 실행 됨

def a_cal_rec_are(x,y):
    print(x*y)

rec_x = 10
rec_y = 20

print("사각형 넓이 : ", cal_rec_are(rec_x, rec_y))   # 실제 함수에 대입되는 입력값을 argument라고 함
print(a_cal_rec_are(rec_x,rec_y))                   # 리턴값이 없는 함수를 실행한 결과를 print로 출력하면 함수는 None 값을 반환하는 것을 볼 수 있음
                                                    # 이는 리턴 값이 없는 함수를 실행하면 반환값은 None 임을 알 수 있음

# ctrl + / 하면 전체 주석/주석 해제
