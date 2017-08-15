# 3주차 테스트 코드
# Console In & Out

print("이름을 입력하세요 : ")
somebody = input()
print("안녕 ", somebody)      #print 함수에 문자열을 출력함 ("","") 와 같은 효과임

Inname = input();       #input()함수는 문자열을 입력 받음
                        #만약 입력 받은 문자열이 숫자라면 int(), float() 등의 숫자형 형변환이 필요함
print(Inname)
print(type(Inname))

Innum = int(input("정수를 입력하세요 : "))  #input("")에 문자열을 추가하여 원하는 원하는 문구를 추가 가능
print(Innum)
print(type(Innum));

Infloat = float(input("실수를 입력하세요 : "))
print("숫자는", Infloat)
