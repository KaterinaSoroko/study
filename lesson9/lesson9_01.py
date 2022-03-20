"""
пополнение счета возможно только отдельной транзакцией (например, через кассу),
при инициализации изменение не доступно.
"""
from dataclasses import dataclass


@dataclass
class BankClient:
    name: str
    surname: str
    user_name: str
    password: str
    account_number: int
    BANK_TRANSACTION: int = 0
    COUNT_TRANSACTION: int = 0
    __money: int = 0

    @classmethod
    def money_of_accounts(cls, transaction):
        cls.BANK_TRANSACTION += transaction
        cls.COUNT_TRANSACTION += 1

    @classmethod
    def print_bank_transaction(cls):
        print(f"Было проведено {cls.COUNT_TRANSACTION} транзакций на сумму {cls.BANK_TRANSACTION}$")

    @classmethod
    def zeroing_bank_transaction(cls):
        cls.BANK_TRANSACTION = 0
        cls.COUNT_TRANSACTION = 0

    @staticmethod
    def send_message():
        print("The bank is closed today.")

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, transaction):
        self.__money += transaction
        BankClient.money_of_accounts(transaction)
        if transaction > 0:
            print(f"Счет пополнен на сумму {transaction}$. В данный момент на счету {self.__money}$.")
        else:
            print(f"Со счета списана сумма {transaction}$. В данный момент на счету {self.__money}$.")


client_1 = BankClient(name="Olga", surname="Star", user_name="Star_Olga", password="1234", account_number=157969645)
client_1.money = 500
client_1.money = -100
print(f"На счету {client_1.name} {client_1.surname}: {client_1.money}$")
client_2 = BankClient(name="Ivan", surname="Ivanov", user_name="Ivanov_007", password="Ivan", account_number=157956313)
client_2.money = 900
client_2.money = -90
BankClient.print_bank_transaction()
BankClient.zeroing_bank_transaction()
client_1.money = 500
client_2.money = -400
BankClient.print_bank_transaction()
