import pytest
from demo.simple_bank_system.bank import Bank


def test_scenario():
    bank = Bank([10, 100, 20, 50, 30])
    assert bank.withdraw(3, 10)
    assert bank.transfer(5, 1, 20)
    assert bank.deposit(5, 20)
    assert not bank.transfer(3, 4, 15)
    assert not bank.withdraw(10, 50)


@pytest.mark.parametrize("account", [0, 6])
def test_deposit_invalid_account(account):
    bank = Bank([10, 100, 20, 50, 30])
    assert not bank.deposit(account, 10)


@pytest.mark.parametrize("account", [0, 6])
def test_withdraw_invalid_account(account):
    bank = Bank([10, 100, 20, 50, 30])
    assert not bank.withdraw(account, 10)


def test_transfer_invalid_target_account():
    bank = Bank([10, 100, 20, 50, 30])
    original_source_balance = bank.balance[0]
    assert not bank.transfer(1, 6, 5)
    assert bank.balance[0] == original_source_balance


def test_transfer_invalid_source_account():
    bank = Bank([10, 100, 20, 50, 30])
    target_before = bank.balance[1]
    assert not bank.transfer(0, 2, 5)
    assert bank.balance[1] == target_before
