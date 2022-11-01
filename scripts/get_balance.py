
from brownie import ProofOfPropCreator
from scripts.helpful_scripts import get_account


def main():
    show_balance()


# Neftyr: This Allows Us As Owners Check Balance On Creator Contract  
def show_balance():
    account = get_account()
    proof_of_prop_creator = ProofOfPropCreator[-1]
    current_balance = proof_of_prop_creator.showBalance({"from": account})
    print(f"Current balance of creator contract is: {current_balance}")
