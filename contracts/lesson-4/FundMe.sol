// SPDX-License-Identifier: MIT

pragma solidity ^0.8.18;

import {Ownable} from "@openzeppelin/contracts/access/Ownable.sol";
import {EthToUsdConverter} from "./EthToUsdConverter.sol";

error FundMe__TooLowFundSent();

contract FundMe is Ownable {
    using EthToUsdConverter for uint256;

    mapping(address => uint256) public s_addressToAmountFunded;
    uint256 public immutable s_minFundUSD = 1 * 10**18;

    function fund() public payable {
        if (msg.value.convert() < s_minFundUSD) {
            revert FundMe__TooLowFundSent();
        }

        s_addressToAmountFunded[msg.sender] += msg.value;
    }

    function withdraw() public payable onlyOwner {
        payable(msg.sender).transfer(address(this).balance);
    }
}
