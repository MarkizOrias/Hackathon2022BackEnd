from brownie import Contract, CopyRightLockCreator
from scripts.helpful_scripts import get_account

specific_address = "0x4D87157990574493F39107d3843C5dF3B78f5B2e"


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
    formatted_balance = float(previous_balance / 10**18)
    print(f"Funds Able To Withdraw: {formatted_balance} ETH")
    tx = creator.withdraw({"from": account})
    tx.wait(1)
    current_balance = creator.showBalance({"from": account})
    format_balance = float(current_balance / 10**18)
    print(f"Current balance of creator contract is: {format_balance}")


def balance_from_exact_contract():
    account = get_account()
    creator = Contract.from_explorer(specific_address)
    previous_balance = creator.showBalance({"from": account})
    formatted_balance = float(previous_balance / 10**18)
    print(f"Balance: {formatted_balance}")


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
    proof_of_prop_creator = CopyRightLockCreator[-1]
    current_balance = proof_of_prop_creator.showBalance({"from": account})
    formatted_balance = float(current_balance / 10**18)
    print(f"Current balance of creator contract is: {formatted_balance} ETH")
