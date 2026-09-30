
import pytest
from bank_account import BankAccount


# ========================================
# Test 1 - Initial Balance
# ========================================

def test_new_account_starts_with_zero_balance():
    # A new account should start with a balance of 0.
    account = BankAccount()

    assert account.get_balance() == 0


# ========================================
# Test 2 - Deposit Once
# ========================================

def test_deposit_money_once():
    # Depositing 100 should result in a balance of 100.
    account = BankAccount()

    account.deposit(100)

    assert account.get_balance() == 100


# ========================================
# Test 3 - Deposit Twice
# ========================================

def test_deposit_money_twice():
    # Depositing 100 and then 50 should result in 150.
    account = BankAccount()

    account.deposit(100)
    account.deposit(50)

    assert account.get_balance() == 150


# ========================================
# Test 4 - Withdraw Money
# ========================================

def test_withdraw_money():
    # Depositing 100 and withdrawing 30 should leave 70.
    account = BankAccount()

    account.deposit(100)
    account.withdraw(30)

    assert account.get_balance() == 70


# ========================================
# Test 5 - Multiple Operations
# ========================================

def test_balance_after_deposit_and_withdraw():
    # 200 - 50 + 25 = 175
    account = BankAccount()

    account.deposit(200)
    account.withdraw(50)
    account.deposit(25)

    assert account.get_balance() == 175


# ========================================
# Test 6 - New Account Is Empty
# ========================================

def test_is_empty_returns_true_for_new_account():
    # A new account has a zero balance.
    account = BankAccount()

    assert account.is_empty() is True


# ========================================
# Test 7 - Account Is Not Empty
# ========================================

def test_is_empty_returns_false_after_deposit():
    # After depositing money, the account is not empty.
    account = BankAccount()

    account.deposit(100)

    assert account.is_empty() is False


# ========================================
# BONUS TESTS
# ========================================


# ========================================
# Bonus 1 - Deposit Zero
# ========================================

def test_deposit_zero():
    # Depositing 0 should not change the balance.
    account = BankAccount()

    account.deposit(0)

    assert account.get_balance() == 0
    assert account.is_empty() is True


# ========================================
# Bonus 2 - Withdraw All Money
# ========================================

def test_withdraw_all_money():
    # Withdrawing the full balance should leave 0.
    account = BankAccount()

    account.deposit(100)
    account.withdraw(100)

    assert account.get_balance() == 0
    assert account.is_empty() is True


# ========================================
# Bonus 3 - Deposit, Withdraw, Deposit
# ========================================

def test_deposit_withdraw_deposit_again():
    # 100 - 40 + 20 = 80
    account = BankAccount()

    account.deposit(100)
    account.withdraw(40)
    account.deposit(20)

    assert account.get_balance() == 80
    assert account.is_empty() is False