from brownie import ProofOfProp, MockV3Aggregator, network, config
from scripts.helpful_scripts import (deploy_mocks, get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS)
from web3 import Web3


def main():
    deploy_POP()


def deploy_POP():
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
        # use the most recent data from the MockV3Aggregator

    proof_of_prop = ProofOfProp.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )

    # check Reading contract in testnet (goerli etherscan)
    print(f"Contract depolyed to {proof_of_prop.address}")
    return proof_of_prop
