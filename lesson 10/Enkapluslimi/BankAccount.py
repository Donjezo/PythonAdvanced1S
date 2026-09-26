class BackAccount:

    def __init__(self,owner,balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balence(self):
        return self.__balance


account = BackAccount("donjeta",100)

print(account.get_balence())
account.deposit(50)

print(account.get_balence())