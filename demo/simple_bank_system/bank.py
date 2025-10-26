from typing import List


class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance


    def transfer(self, account1: int, account2: int, money: int) -> bool:
        return self.withdraw(account1, money) and self.deposit(account2, money)


    def deposit(self, account: int, money: int) -> bool:
        return self.update_balance(account, money)


    def withdraw(self, account: int, money: int) -> bool:
        return self.update_balance(account, -money)

    def update_balance(self, account: int, diff: int) -> bool:
        if (account < 1 or account > len(self.balance)):
            return False
        if (diff < 0 and self.balance[account - 1] + diff < 0):
            return False
        self.balance[account - 1] += diff
        return True
