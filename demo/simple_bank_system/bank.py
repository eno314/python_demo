from typing import List


class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance


    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if self._is_valid_account(account1) and self._is_valid_account(account2):
            return self.withdraw(account1, money) and self.deposit(account2, money)
        return False

    def deposit(self, account: int, money: int) -> bool:
        return self._update_balance(account, money)

    def withdraw(self, account: int, money: int) -> bool:
        return self._update_balance(account, -money)

    def _is_valid_account(self, account: int) -> bool:
        return 1 <= account <= len(self.balance)

    def _update_balance(self, account: int, diff: int) -> bool:
        if not self._is_valid_account(account):
            return False
        if (diff < 0 and self.balance[account - 1] + diff < 0):
            return False
        self.balance[account - 1] += diff
        return True
