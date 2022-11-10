
from brownie import CopyRightLockCreator, MockV3Aggregator, network, config
from scripts.get_hash import hash_file, user_input
from scripts.helpful_scripts import (
    deploy_mocks,
    get_account,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)
import time


def main():
    deploy_CRL_Creator() # Neftyr: deploy creator contract (factory)
    # fund() # Disabled as requested
    show_balance() # Neftyr: show balance before any deployments
    deploy_CRL() # Neftyr: deploy contract for Client
    show_balance() # Neftyr: show balance after client certificate deployment


def deploy_CRL_Creator():
    account = get_account()

    # pass the price feed address to the contract
    # if we are on a persistent network like goerli, use the associated address
    # otherwise, deploy mocks
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
        print(f"price_feed_address {price_feed_address}")
        # use the most recent data from the MockV3Aggregator

    proof_of_prop_creator = CopyRightLockCreator.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    time.sleep(5)
    # check Reading contract in testnet (goerli etherscan)
    print(f"Contract depolyed to {proof_of_prop_creator.address}")
    return proof_of_prop_creator


# NI: TODO -> To be removed after testing on production example.
# MO: Disabled as it is not required
# def fund():
#     proof_of_prop_creator = CopyRightLockCreator[-1]
#     account = get_account()
#     minimum_fee = proof_of_prop_creator.getMinimumFee()
#     print(minimum_fee)
#     print(f"The current entry fee is {minimum_fee}")
#     print("Funding")
#     proof_of_prop_creator.fund({"from": account, "value": minimum_fee})
#     print("Funded!")


# MO: testing purpose - read balance during development
def show_balance():
    account = get_account()
    proof_of_prop_creator = CopyRightLockCreator[-1]
    current_balance = proof_of_prop_creator.showBalance({"from": account})
    print(f"Current balance of creator contract is: {current_balance}")


# Neftyr: To Be Moved Into "deploy_cert.py"
def deploy_CRL():
    account = get_account()
    proof_of_prop_creator = CopyRightLockCreator[-1]
    # Just to make sure fee will be covered, add some Wei to it: 100000000
    fee = proof_of_prop_creator.getMinimumFee({"from": account}) + 10 ** 8
    # Below deploy is paid from {"from": account} -> so we have to put account of our client here.
    pop_deploy = proof_of_prop_creator.addCertificate(
        "certificate",
        "date",
        "title",
        account, # NI: "proof_of_prop_creator" changed into "account" as owner of generated cert is our Client.
        "name",
        "additional",
        hash_file(user_input),
        {"from": account, "value": fee},
    )
    pop_deploy.wait(1)
    lastCert = proof_of_prop_creator.getLastCertificate({"from": account})
    print(f"Transaction: {pop_deploy}")
    print(f"Last Certificate: {lastCert}")
    # NI: TODO -> add return pop_deploy (In order to change contract owner)
