
from brownie import network, exceptions, accounts
from scripts.deploy_creator import deploy_POP_Creator
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
import pytest


def test_withdraw():
    # Arrange
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local testing")
    account = get_account()
    creator = deploy_POP_Creator()
    add_cert_fee = creator.getMinimumFee({"from": account}) + 100
    tx = creator.addCertificate(
        "certificate",
        "date",
        "title",
        account,
        "name",
        "additional",
        "hash",
        {"from": account, "value": add_cert_fee}
    )
    tx.wait(1)
    balance_before = creator.showBalance({"from": account})
    # Act
    tx_withdraw = creator.withdraw({"from": account})
    tx_withdraw.wait(1)
    balance_after = creator.showBalance({"from": account})
    print(f'Before Withdraw: {balance_before}')
    print(f'After Withdraw: {balance_after}')
    # Assert
    assert balance_before > balance_after
    assert balance_after == 0


def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local testing")
    creator = deploy_POP_Creator()
    thief_account = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        creator.withdraw({"from": thief_account})
