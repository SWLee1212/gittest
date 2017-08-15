# 클래스 상속 및 멤버함수 재정의 사용 예제

class Person(object) :                                  # Object 클래스를 기본적으로 상속 받는 다는 의미
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def about_me(self):
        print("저의 이름은 ", self.name, "이고, 제 나이는 ", str(self.age), "살 입니다.")

class Employee(Person) :
    def __init__(self, name, age, gender, salary, hire_date):
        super().__init__(name, age, gender)             #  super라는 키워드로 상속받은 클래스 멤버 함수에 접근
        self.salary = salary                            # super 키워드를 쓰지 않고 부모 클래스와 같은 이름의 멤버 함수를 쓰면, 부모 클래스의 멤버함수를
                                                        # 재 정의하여 자식 클래스가 사용하게 됨
        self.hire_date = hire_date

    def do_work(self):
        print("일을 합니다.")

    def about_me(self):
        super().about_me()
        print("제 급여는 ", self.salary, "원 이고, 제 입사일은 " , self.hire_date, " 입니다.")

MyPerson = Person("sw", 32, "Male")
MyPerson.about_me()
MyEmployee = Employee("YM", 30, "Female", 300, "17-01-01")
MyEmployee.about_me()
