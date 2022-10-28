
from brownie import ProofOfPropCreator


def main():
    show_balance()


# Neftyr: This Allows Us As Owners Check Balance On Creator Contract  
def show_balance():
    proof_of_prop_creator = ProofOfPropCreator[-1]
    current_balance = proof_of_prop_creator.showBalance()
    print(f"Current balance of creator contract is: {current_balance}")
