
from brownie import network
from scripts.get_hash import hash_file, user_input
from scripts.deploy_creator import deploy_POP_Creator
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
import pytest


def test_show_balance():
    # Arrange
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local testing")
    account = get_account()
    creator = deploy_POP_Creator()
    add_cert_fee = creator.getMinimumFee({"from": account}) + 100
    # Act
    tx = creator.addCertificate(
        "certificate",
        "date",
        "title",
        account,
        "name",
        "additional",
        hash_file(user_input),
        {"from": account, "value": add_cert_fee}
    )
    tx.wait(1)
    # Assert
    current_balance = creator.showBalance({"from": account})
    assert current_balance > 0
