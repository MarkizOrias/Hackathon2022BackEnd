
from brownie import CopyRightLockCreator
from scripts.helpful_scripts import get_account


def main():
    withdraw()


# Neftyr: Below Will Withdraw All Funds From Creator Contract
def withdraw():
    creator = CopyRightLockCreator[-1]
    account = get_account()
    previous_balance = creator.showBalance({"from": account})
    print(f"Funds Able To Withdraw: {previous_balance}")
    tx = creator.withdraw({"from": account})
    tx.wait(1)
    current_balance = creator.showBalance({"from": account})
    print(f"Current balance of creator contract is: {current_balance}")
