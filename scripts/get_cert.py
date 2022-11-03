
from brownie import ProofOfPropCreator
from scripts.helpful_scripts import get_account


def main():
    get_cert()


# Neftyr:
# TODO (We Can Add Small Fee Here)
# This Function Is For Client To Show Them, Which Contracts(Certificates) They Own
def get_cert():
    account = get_account()
    proof_of_prop_creator = ProofOfPropCreator[-1]
    get_cert = proof_of_prop_creator.getCertificatesYouOwn(account)
    print(f'You Are Owner Of Following Certificates: {get_cert}')
    return get_cert
