
from brownie import ProofOfProp
from scripts.deploy_creator import deploy_POP_Creator
from scripts.helpful_scripts import get_account

# getLastCertificate
# getCertificateYouOwn
# getMinimumFee


def test_get_last_certificate():
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
    get_last_cert = creator.getLastCertificate()
    get_cert = creator.addressToContract(account, 0)
    assert get_last_cert == get_cert


def test_get_certificate_you_own():
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
    index = 0
    get_cert = creator.addressToContract(account, index)
    get_owned = creator.getCertificateYouOwn(account)
    assert get_cert == get_owned[index]


def test_get_minimum_fee():
    pass
