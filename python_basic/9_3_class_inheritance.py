# 클래스의 상속 예제

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return "My name is {0}".format(self.name)

class Korean(Person):                               # Korean이라는 클래스는 좀 더 포괄적인 클래스이고, Person이라는 클래스의 특성을 활용할 수 있음
    pass                                            # Korean 클래스가 Person 클래스를 상속받는다.

first_korean = Korean("SW", 33)
print(first_korean)
