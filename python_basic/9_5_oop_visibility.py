# 클래스의 가시성(Visibility), 캡슐화 예제

class Product(object):
    def __str__(self):
        return "나는 제품이다."

class Inventory(object):
    def __init__(self):
        self.__items = []                           # 변수 앞에 __를 붙여서 Visibility 속성을 부여, 외부 클래스에서 접근 불가
                                                    # private 변수로 선언
    def add_new_item(self, product):
        if type(product) == Product :
            self.__items.append(product)
            print("new item added")
        else:
            raise ValueError("Invaild Item")

    def get_number_of_items(self):
        return len(self.__items)

    @property                                       #
    def items(self):                                # 함수 이름이 변수 이름과 같은 필요는 없음
        return self.__items                         # 다른 클라이언트 클래스에서 private 변수에 접근할 수 있음

my_inventory = Inventory()
my_inventory.add_new_item(Product())
my_inventory.add_new_item(Product())
print(my_inventory.get_number_of_items())

# print(my_inventory.__items)                     # __items 변수에는 접근할 수 없음
# my_inventory.add_new_item(object)

items = my_inventory.items
items.append(Product())
print(my_inventory.get_number_of_items())                     # __items 변수에는 접근할 수 없음

print(items[0])
print(items[1])
