class Account:
    def __init__(self, balance):
        self.__balance = balance

    def pay(self, amount):
        self.__balance += amount

    def take(self, amount):
        if amount > self.__balance:
            print("Insufficient funds.")
        else:
            self.__balance -= amount

    def __str__(self):
        return f"Account balance: {self.__balance}"


if __name__ == "__main__":
    account = Account(100)
    print(account)

    account.pay(50)
    print(account)

    account.take(75)
    print(account)

    account.take(100)
    print(account)