
from brownie import network
from scripts.deploy_creator import deploy_POP_Creator
from scripts.helpful_scripts import get_account


def test_add_certificate():
    # Arrange
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
        "hash",
        {"from": account, "value": add_cert_fee}
    )
    tx.wait(1)
    # Assert
    cert_array, clients_array = creator.arrayLengthGetter()
    assert cert_array == 1
