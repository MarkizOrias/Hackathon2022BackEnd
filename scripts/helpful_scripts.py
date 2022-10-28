from brownie import network, config, accounts, MockV3Aggregator

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]

DECIMALS = 8
PRICE = 200000000000


def get_account():
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
    # if not in the development network, it will pull from config


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print(f"Deploying Mocks...")
    if len(MockV3Aggregator) <= 0:
        # checking the length of an array of deployed contract called MockV3Aggregator to deploy it only once
        MockV3Aggregator.deploy(
            DECIMALS,
            PRICE,
            {"from": get_account()}
            # from web3 import Web3 in head, Web3.toWei(2000, "ether") replacing 2000000000000000000000
        )
    print("Mocks deployed!")


# contract_to_mock = {"eth_usd_price_feed": MockV3Aggregator}


# def get_contract(contract_name):
#     """This function will grab the contract addresses from the brownie config
#     if defined, otherwise, it will deploy a mock version of that contract, and
#     return that mock contract.

#         Args:
#             contract_name (string)

#         Returns:
#             brownie.network.contract.ProjectContract: The most recently deployed
#             version of this contract.
#     """
#     contract_type = contract_to_mock[contract_name]
#     if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
#         if len(contract_type) <= 0:
#             # MockV3Aggregator.length
#             deploy_mocks()
#         contract = contract_type[-1]
#         # MockV3Aggregator[-1]
#     else:
#         contract_address = config["networks"][network.show_active()][contract_name]
#         # address
#         # ABI
#         contract = Contract.from_abi(
#             contract_type._name, contract_address, contract_type.abi
#         )
#         # MockV3Aggregator.abi
#     return contract
