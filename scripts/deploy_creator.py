
from brownie import CopyRightLockCreator, MockV3Aggregator, network, config
from scripts.helpful_scripts import (
    deploy_mocks,
    get_account,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)
import time


def main():
    deploy_CRL_Creator() # Neftyr: deploy creator contract (factory)
    show_balance() # Neftyr: show balance before any deployments


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


# MO: testing purpose - read balance during development
def show_balance():
    account = get_account()
    proof_of_prop_creator = CopyRightLockCreator[-1]
    current_balance = proof_of_prop_creator.showBalance({"from": account})
    print(f"Current balance of creator contract is: {current_balance}")
