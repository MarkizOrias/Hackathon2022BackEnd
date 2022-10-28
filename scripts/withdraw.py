
from brownie import ProofOfPropCreator
from scripts.helpful_scripts import get_account


def main():
    withdraw()


def withdraw():
    creator = ProofOfPropCreator[-1]
    account = get_account()
    previous_balance = creator.showBalance()
    print(f"Funds Able To Withdraw: {previous_balance}")
    creator.withdraw({"from": account})
    current_balance = creator.showBalance()
    print(f"Current balance of creator contract is: {current_balance}")
