# BankAccount.py

#은행의 계정을 표현한 클래스 
class BankAccount:
    def __init__(self, id, name, balance):
        # 내부에 숨김(이름변경) private
        self.__id = id
        self.__name = name 
        self.__balance = balance 
        

    def deposit(self, amount):
        self.__balance += amount 
    def withdraw(self, amount):
        self.__balance -= amount
    # 문자열 출력하는 규칙 __str__
    def __str__(self):
        return "{0} , {1} , {2}".format(self.__id, \
            self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.withdraw(3000)

#print(account1.__balance) # 접근이 안됨. 에러
print(account1._BankAccount__balance) #이렇게하면 접근됨.
print(account1)
