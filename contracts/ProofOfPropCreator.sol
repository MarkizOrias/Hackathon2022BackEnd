// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
import "./ProofOfProp.sol";

contract ProofOfPropCreator {
    mapping(address => address[]) private addressToContract;
    ProofOfProp[] private certificatesStorageArray;

    mapping(address => uint256) public addressToAmountFunded; // GB
    address[] public propClients; // GB

    uint256 public usdEntryFee; // variable storing minimum fee
    AggregatorV3Interface internal ethUsdPriceFeed;

    constructor(address _priceFeedAddress) {
        ethUsdPriceFeed = AggregatorV3Interface(_priceFeedAddress); // Assignment of price feed variable
        usdEntryFee = 50 * (10**18);
    }

    // GB: created fund function, moved require from addCertificate
    function fund() public payable {
        require(
            msg.value >= getMinimumFee(),
            "You need to pay more ETH to create certificate!"
        );
        addressToAmountFunded[msg.sender] += msg.value;
        propClients.push(msg.sender);
    }

    // Client Needs to pay us in order to use "addCertificate" function.
    function addCertificate(
        string memory _certificate,
        string memory _date,
        string memory _title,
        address _address,
        string memory _name,
        string memory _additional,
        string memory _hash
    ) public payable returns (address) {
        // ToDo :
        // To use this function client has to pay >= minimumFee.
        // Money All Clients pay should be stored on ProofOfPropCreator Contract, so as owners of that Contract can withdraw it.

        ProofOfProp certificateStorage = new ProofOfProp(
            _certificate,
            _date,
            _title,
            _address,
            _name,
            _additional,
            _hash
        );
        // Below adding new Certificate(Contract) to array, which contains all certificates ever created by all clients.
        certificatesStorageArray.push(certificateStorage);
        // Below is mapping Client address with all Certificates(Contracts) he deployed (tracking all certificates, which given Client is owner of).
        addressToContract[msg.sender].push(address(certificateStorage));
        return address(certificateStorage); // GB: to read deployed POP
    }

    // Below Function Allows Client To Check All Certificate(Contracts) He Owns.
    function getCertificateYouOwn(address _yourAddress)
        public
        view
        returns (address[] memory)
    {
        return addressToContract[_yourAddress];
    }

    // Below Function Defines Minimal Fee To Use addCertificate() function.
    function getMinimumFee() public view returns (uint256) {
        (, int256 price, , , ) = ethUsdPriceFeed.latestRoundData(); // Takes this from AggregatorV3 latestRoundData
        uint256 adjustedPrice = uint256(price) * 10**10; // adjustedPrice has to be expressed with 18 decimals. From Chainlink pricefeed, we know ETH/USD has 8 decimals, so we need to multiply by 10^10
        uint256 costToEnter = (usdEntryFee * 10**18) / adjustedPrice; // We cannot return decimals, hence we need to express 50$ with 50 * 10*18 / 2000 (adjusted price of ETH)
        return costToEnter; // for testing
    }

    // GB: testing purpose - read balance during development. REMOVE IN PRODUCTION VERSION!!!
    function showBalance() public view returns (uint256) {
        uint256 POPbalance = address(this).balance;
        return POPbalance;
    }

    // ToDo : Below function allows us as Owners of this contract to withdraw money gathered on this contract.
    // function withdraw() payable onlyOwner public {

    // }
}
