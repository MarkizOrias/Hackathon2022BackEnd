// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "./ProofOfProp.sol";

contract ProofOfPropCreator {

    mapping(address => address[]) private addressToContract;
    ProofOfProp[] private certificatesStorageArray;

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
            addressToContract[msg.sender].push(address(certificateStorage));
    }

    function getCertificateYouOwn(address _yourAddress) public view returns (address[] memory) {
        return addressToContract[_yourAddress];
    }
}
