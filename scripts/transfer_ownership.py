from brownie import Contract, CopyRightLockCreator
from scripts.helpful_scripts import get_account

# In order to paste "input()" data use: Ctrl + Shift + V
specific_address = "0xeE7935713c6C005FbEB067287359C78E0cd3b150"


def main():
    current_owner = get_account()
    new_owner = input("Enter New Owner Address: ")
    cert_address = input("Enter Address Of Certificate You Want To Move: ")
    # transfer_ownership_last(current_owner, new_owner, cert_address)
    transfer_ownership_exact(current_owner, new_owner, cert_address)


def transfer_ownership_last(current_owner, new_owner, cert_address):
    proof_of_prop_creator = CopyRightLockCreator[-1]
    fee = proof_of_prop_creator.getMinimumFee({"from": current_owner}) + 10**8
    transfer_ownership = proof_of_prop_creator.transOwnership(
        current_owner, new_owner, cert_address, {"from": current_owner, "value": fee}
    )
    transfer_ownership.wait(1)
    print("Certificate Ownership Has Been Transferred!")


def transfer_ownership_exact(current_owner, new_owner, cert_address):
    proof_of_prop_creator = Contract.from_explorer(specific_address)
    fee = proof_of_prop_creator.getMinimumFee({"from": current_owner}) + 10**8
    transfer_ownership = proof_of_prop_creator.transOwnership(
        current_owner, new_owner, cert_address, {"from": current_owner, "value": fee}
    )
    transfer_ownership.wait(1)
    print("Certificate Ownership Has Been Transferred!")
