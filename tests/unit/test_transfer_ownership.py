
from brownie import accounts, network, ProofOfPropCreator
from scripts.get_hash import hash_file, user_input
from scripts.deploy_creator import deploy_POP_Creator
from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS
import pytest


def test_transfer_ownership():
    # Arrange
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local testing")
    deploy_POP_Creator()
    creator_contract = ProofOfPropCreator[-1]
    account_one = accounts[0]
    account_two = accounts[1]
    account_three = accounts[2]
    fee = creator_contract.getMinimumFee() + 10 ** 8
    starting_balance = creator_contract.showBalance({"from": account_one})
    # Client One ------------------------------------------------------------------------------------------------------
    add_cert_one = creator_contract.addCertificate(
        "certificate",
        "date",
        "title",
        account_one, # Niferu: "creator_contract" changed into "account" as owner of generated cert is our Client.
        "name",
        "additional",
        hash_file(user_input),
        {"from": account_one, "value": fee},
    )
    add_cert_one.wait(1)
    get_certs_one = creator_contract.getCertificatesYouOwn(account_one)
    print(f'Certificates Owned By {account_one} Are: {get_certs_one}')
    # Client Two ------------------------------------------------------------------------------------------------------
    # First Cert
    add_cert_two_1 = creator_contract.addCertificate(
        "certificate",
        "date",
        "title",
        account_two, # Niferu: "creator_contract" changed into "account" as owner of generated cert is our Client.
        "name_one",
        "additional",
        hash_file(user_input),
        {"from": account_two, "value": fee},
    )
    add_cert_two_1.wait(1)
    # Second Cert
    add_cert_two_2 = creator_contract.addCertificate(
        "certificate",
        "date",
        "title",
        account_two, # Niferu: "creator_contract" changed into "account" as owner of generated cert is our Client.
        "name_two",
        "additional",
        hash_file(user_input),
        {"from": account_two, "value": fee},
    )
    add_cert_two_2.wait(1)
    # Third Cert
    add_cert_two_3 = creator_contract.addCertificate(
        "certificate",
        "date",
        "title",
        account_two, # Niferu: "creator_contract" changed into "account" as owner of generated cert is our Client.
        "name_three",
        "additional",
        hash_file(user_input),
        {"from": account_two, "value": fee},
    )
    add_cert_two_3.wait(1)
    get_certs_two = creator_contract.getCertificatesYouOwn(account_two)
    print(f'Certificates Owned By {account_two} Are: {get_certs_two}')
    # Client Three ------------------------------------------------------------------------------------------------------
    get_certs_three = creator_contract.getCertificatesYouOwn(account_three)
    print(f'Certificates Owned By {account_three} Are: {get_certs_three}')
    balance_after_deploying_certs = creator_contract.showBalance({"from": account_one})
    print(f'Starting Balance: {starting_balance}')
    print(f'Balance After All Clients Deployments Of Certs: {balance_after_deploying_certs}')
    cert_to_move = get_certs_two[1]
    print(f'Cert To Move Address: {cert_to_move}')
    # Act
    # We will try to move middle certificate owned by Client 2 to Client 3 and Client 1 by different clients as thiefs
    
    # Case 1 (MALICIOUS) ------------------------------------------------------------------------------------------------------
    # Try to move Cert 2 from Client 2 to Client 3 as Client 3
    print("Case 1 ------------------------------------------------------------------------------------------------------")
    case_one = creator_contract.transferOwnership(account_three, account_three, cert_to_move, {"from": account_three, "value": fee})
    case_one.wait(1)
    print("First Malicious Transfer Of Ownership Attempt Completed!")
    get_certs_two_case_one = creator_contract.getCertificatesYouOwn(account_two)
    print(f'Certificates Owned By Client 2 {account_two} Are: {get_certs_two_case_one}')
    get_certs_three_case_one = creator_contract.getCertificatesYouOwn(account_three)
    print(f'Certificates Owned By Client 3 {account_three} Are: {get_certs_three_case_one}')
    all_certs_stored, certs_owned_by_client_two_case_one = creator_contract.arrayLengthGetter(account_two, {"from": account_one})
    all_certs_stored, certs_owned_by_client_three_case_one = creator_contract.arrayLengthGetter(account_three, {"from": account_one})
    print(f'Amount Of Certs Owned By Client 2: {certs_owned_by_client_two_case_one}')
    print(f'Amount Of Certs Owned By Client 3: {certs_owned_by_client_three_case_one}')
    
    # Case 2 (MALICIOUS) ------------------------------------------------------------------------------------------------------
    # Try to move Cert 2 from Client 2 to Client 3 as Client 1 (Who is owner of creator contract)
    print("Case 2 ------------------------------------------------------------------------------------------------------")
    case_two = creator_contract.transferOwnership(account_one, account_three, cert_to_move, {"from": account_one, "value": fee})
    case_two.wait(1)
    print("Second Malicious Transfer Of Ownership Attempt Completed!")
    get_certs_two_case_two = creator_contract.getCertificatesYouOwn(account_two)
    print(f'Certificates Owned By Client 2 {account_two} Are: {get_certs_two_case_two}')
    get_certs_three_case_two = creator_contract.getCertificatesYouOwn(account_three)
    print(f'Certificates Owned By Client 3 {account_three} Are: {get_certs_three_case_two}')
    all_certs_stored, certs_owned_by_client_two_case_two = creator_contract.arrayLengthGetter(account_two, {"from": account_one})
    all_certs_stored, certs_owned_by_client_three_case_two = creator_contract.arrayLengthGetter(account_three, {"from": account_one})
    print(f'Amount Of Certs Owned By Client 2: {certs_owned_by_client_two_case_two}')
    print(f'Amount Of Certs Owned By Client 3: {certs_owned_by_client_three_case_two}')
    
    # Balance Check After 2 Ownership Transfer Attempts
    balance_after_case = creator_contract.showBalance({"from": account_one})
    print(f'Balance After 2 Ownership Transfer Attempts: {balance_after_case}')
    
    # Case 3 (CORRECT) ------------------------------------------------------------------------------------------------------
    # Try to move Cert 2 from Client 2 to Client 3 as Client 2 (Who is owner of Cert 2)
    print("Case 3 ------------------------------------------------------------------------------------------------------")
    case_three = creator_contract.transferOwnership(account_two, account_three, cert_to_move, {"from": account_two, "value": fee})
    case_three.wait(1)
    print("Correct Transfer Of Ownership Attempt Completed!")
    get_certs_two_case_three = creator_contract.getCertificatesYouOwn(account_two)
    print(f'Certificates Owned By Client 2 {account_two} Are: {get_certs_two_case_three}')
    get_certs_three_case_three = creator_contract.getCertificatesYouOwn(account_three)
    print(f'Certificates Owned By Client 3 {account_three} Are: {get_certs_three_case_three}')
    all_certs_stored, certs_owned_by_client_two_case_three = creator_contract.arrayLengthGetter(account_two, {"from": account_one})
    all_certs_stored, certs_owned_by_client_three_case_three = creator_contract.arrayLengthGetter(account_three, {"from": account_one})
    print(f'Amount Of Certs Owned By Client 2: {certs_owned_by_client_two_case_three}')
    print(f'Amount Of Certs Owned By Client 3: {certs_owned_by_client_three_case_three}')
    all_certs_stored, certs_owned_by_client_one = creator_contract.arrayLengthGetter(account_one, {"from": account_one})
    all_certs, certs_owned_by_clients = creator_contract.arrayLengthGetter(account_one, {"from": account_one})
    print(f'All Certs: {all_certs}')

    # Balance Check After Last Ownership Transfer Correct Attempt
    balance_after_last = creator_contract.showBalance({"from": account_one})
    print(f'Balance After 3 Ownership Transfer Attempts: {balance_after_last}')

    # Assert
    # Assert Case 1
    assert certs_owned_by_client_two_case_one == 3
    assert certs_owned_by_client_three_case_one == 0
    # Assert Case 2
    assert certs_owned_by_client_two_case_two == 3
    assert certs_owned_by_client_three_case_two == 0
    # Assert Case 3
    assert certs_owned_by_client_one == 1
    assert certs_owned_by_client_two_case_three == 2
    assert certs_owned_by_client_three_case_three == 1
    assert all_certs == 4
