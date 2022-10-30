
from scripts.deploy_creator import deploy_POP_Creator
from scripts.helpful_scripts import get_account


def test_get_balance():
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
    current_balance = creator.showBalance()
    assert current_balance > 0
