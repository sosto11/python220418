# class.py
class Person:
    def __init__(self):
        self.name = "default name"
    def print(self):
        print("My name is {0}".format(self.name))

p1 = Person()
p1.print()

p1.name = "즈옹"

p1.print()

p1.age =30 # 인스턴스에 추가

print(p1.age)