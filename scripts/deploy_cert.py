
from brownie import ProofOfPropCreator
from scripts.helpful_scripts import get_account


def main():
    deploy_certificate()
    show_balance()


# Neftyr: under development
def deploy_certificate():
    account = get_account()
    proof_of_prop_creator = ProofOfPropCreator[-1]
    # Just to make sure fee will be covered, add some Wei to it: 100000000
    fee = proof_of_prop_creator.getMinimumFee() + 10 ** 8
    # Below deploy is paid from {"from": account} -> so we have to put account of our client here.
    pop_deploy = proof_of_prop_creator.addCertificate(
        "certificate",
        "date",
        "title",
        proof_of_prop_creator,
        "name",
        "additional",
        "hash",
        {"from": account, "value": fee},
    )
    pop_deploy.wait(1)
    lastCert = proof_of_prop_creator.getLastCertificate()
    print(f"Transaction: {pop_deploy}")
    print(f"Last Certificate: {lastCert}")


def show_balance():
    proof_of_prop_creator = ProofOfPropCreator[-1]
    current_balance = proof_of_prop_creator.showBalance()
    print(f"Current balance of creator contract is: {current_balance}")
