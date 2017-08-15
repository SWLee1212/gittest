# 파이썬에서 클래스 선언 및 사용 예제

class SoccerPlayer(object):
    def __init__(self, name, position, back_number):
        self.name = name
        self.position = position
        self.back_number = back_number
        print(id(self))                                         # self 가 sw 객체의 id가 동일함(주소가 동일함)

    def change_back_number(self, new_number):                   # self 변수는 객체 그 자체를 의미함
        print("선수의 등번호를 변경합니다. From %d to %d " % (self.back_number, new_number))
        self.back_number = new_number

    def __str__(self):
        return "Hello, My name is %s. I play in %s in center. " % (self.name, self.position)

# sw라는 객체가 정의됨
sw = SoccerPlayer("sw","MF",10)             # def __init__ 가 호출됨(실행)
print(sw)                                   # 객체의 __str__함수가 실행되면수 str 변수가 return됨
print(id(sw))

print("현재 선수의 등번호는 : ",sw.back_number)  # 객체 내 멤버 변수 접근
sw.change_back_number(99)                   # def change_back_number가 실행됨

print("현재 선수의 등번호는 : ",sw.back_number)


name = ["sw","jong hae","by"]
position = ["MF","FW","DF"]
number = [99,11,8]

PlayerObjects = [SoccerPlayer(index_name, index_position, index_number) for index_name, index_position, index_number in \
                zip(name,position,number)]

for OjectStr in PlayerObjects:
    print(OjectStr)
