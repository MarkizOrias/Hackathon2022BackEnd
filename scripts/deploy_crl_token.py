from brownie import CopyRightLocker
from scripts.helpful_scripts import get_account
from web3 import Web3

# Supply still to be considered
initialSupply = Web3.toWei(1000000000, "ether")


def deploy_token():
    account = get_account()
    token = CopyRightLocker.deploy(initialSupply, {"from": account})
    print(token.name())
    return token


def main():
    deploy_token()
