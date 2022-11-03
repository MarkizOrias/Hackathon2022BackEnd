
from web3 import Web3
from brownie import network
from scripts.deploy_mocks import deploy_mocks
from scripts.get_hash import hash_file, user_input
from scripts.deploy_creator import deploy_POP_Creator
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
import pytest


def test_get_last_certificate():
    # Arrange
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local testing")
    account = get_account()
    creator = deploy_POP_Creator()
    add_cert_fee = creator.getMinimumFee() + 100
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
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local testing")
    get_last_cert = creator.getLastCertificate({"from": account})
    get_cert = creator.addressToContract(account, 0)
    assert get_last_cert == get_cert


def test_get_certificates_you_own():
    # Arrange
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local testing")
    account = get_account()
    creator = deploy_POP_Creator()
    add_cert_fee = creator.getMinimumFee() + 100
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
    index = 0
    get_cert = creator.addressToContract(account, index)
    get_owned = creator.getCertificatesYouOwn(account)
    assert get_cert == get_owned[index]


def test_get_minimum_fee():
    # Arrange
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local testing")
    account = get_account()
    deploy_mocks()
    creator = deploy_POP_Creator()
    # Act
    fee = creator.getMinimumFee()
    fee_in_eth = Web3.fromWei(fee, "ether")
    print(f'ETH Fee: {fee_in_eth}')
    # Assert
    assert fee_in_eth > 0.02
