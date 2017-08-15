# 클래스 다형성 구현 예제

class Animal(object):
    def __init__(self, name):
        self.name = name

    def talk(self):
        raise NotImplementedError("Subclass must implement abstract method.")

class Cat(Animal):
    def talk(self):
        return "Meow!"

class Dog(Animal):
    def talk(self):
        return "Woof!"

class Human(Animal):
    def talk(self):
        return "Hellow"

animals = [Cat("Missy"),
            Human("SW"),
            Dog("Lassie")]

for animal in animals:
    print(type(animal))
    print(animal.name, " : ", animal.talk())
