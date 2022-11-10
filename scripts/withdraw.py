
from brownie import Contract, CopyRightLockCreator
from scripts.helpful_scripts import get_account

specific_address = "0xd8614E7110d3FBdB9e49c5569f45f4e92fAaa270"


# Neftyr: Below Will Withdraw All Funds From Creator Contract
def main():
    withdraw_from_exact_contract()
    balance_from_exact_contract()
    # withdraw_from_last_contract()
    # balance_from_last_contract()


def withdraw_from_exact_contract():
    account = get_account()
    creator = Contract.from_explorer(specific_address)
    previous_balance = creator.showBalance({"from": account})
    print(f"Funds Able To Withdraw: {previous_balance}")
    tx = creator.withdraw({"from": account})
    tx.wait(1)
    current_balance = creator.showBalance({"from": account})
    print(f"Current balance of creator contract is: {current_balance}")


def balance_from_exact_contract():
    account = get_account()
    creator = Contract.from_explorer(specific_address)
    previous_balance = creator.showBalance({"from": account})
    print(f'Balance: {previous_balance}')


def withdraw_from_last_contract():
    account = get_account()
    creator = CopyRightLockCreator[-1]
    previous_balance = creator.showBalance({"from": account})
    print(f"Funds Able To Withdraw: {previous_balance}")
    tx = creator.withdraw({"from": account})
    tx.wait(1)
    current_balance = creator.showBalance({"from": account})
    print(f"Current balance of creator contract is: {current_balance}")


def balance_from_last_contract():
    account = get_account()
    creator = CopyRightLockCreator[-1]
    previous_balance = creator.showBalance({"from": account})
    print(f'Balance: {previous_balance}')
