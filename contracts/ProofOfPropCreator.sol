// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./ProofOfProp.sol";

contract ProofOfPropCreator {

    // certificatesStorageArray -> it allows you to search contracts by index
    // ToDo: mapping, which allows you to search contract you own
    mapping(address => address[]) public addressToContract;
    
    ProofOfProp[] public certificatesStorageArray;

    function addCertificate(
        string memory _certificate,
        string memory _date,
        string memory _title,
        address _address,
        string memory _name,
        string memory _additional,
        string memory _hash,
        address _priceFeedAddress) public {
            ProofOfProp certificateStorage = new ProofOfProp(_certificate, _date, _title, _address, _name, _additional, _hash, _priceFeedAddress);
            certificatesStorageArray.push(certificateStorage);

            // ToDo: mapping, which allows you to search contract you own
            addressToContract[msg.sender] = address(certificateStorage);
            // addressToContract[msg.sender].push(address(certificateStorage)); *Not Working !!!*
    }

    // ToDo: mapping, which allows you to search contract you own
    function getCertificateYouOwn(address _yourAddress) public view returns (ProofOfProp[] memory) {
        if(msg.sender == _yourAddress){
            return certificatesStorageArray;
        }
    }
}
