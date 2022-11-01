
from web3 import Web3
from brownie import network
from scripts.deploy_creator import deploy_POP_Creator
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
import pytest


def test_get_minimum_fee():
    # Arrange
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for integration testing")
    account = get_account()
    creator = deploy_POP_Creator()
    # Act
    fee = creator.getMinimumFee({"from": account})
    fee_in_eth = Web3.fromWei(fee, "ether")
    print(f'ETH Fee: {fee_in_eth}')
    # Assert
    assert fee_in_eth > 0.02