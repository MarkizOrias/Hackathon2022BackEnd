// contracts/CopyRightLocker.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

// Our Own Token For Business Purposes In Near Future
contract CopyRightLocker is ERC20 {
    constructor(uint256 initialSupply) ERC20("CopyRightLocker", "CRL") {
        _mint(msg.sender, initialSupply);
    }
}
