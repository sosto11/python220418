class Person:
    # 부모클래스의 초기화 메서드(생성자)
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber

    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))

class Student(Person):
    #자식 클래스의 재정의(덮어쓰기,overwrite)
    def __init__(self, name, phoneNumber, subject, studentID):
        #self.name = name
        #self.phoneNumber = phoneNumber
        Person.__init__(self,name,phoneNumber)
        self.subject = subject
        self.studentID = studentID

    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(self.name, self.phoneNumber))
        print("Info(Name:{0}, Phone Number: {1})".format(self.subject, self.studentID))



# 인스턴스(복사본)
p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234", "컴공", "991122")
print(p.__dict__)
print(s.__dict__)