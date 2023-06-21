// SPDX-License-Identifier: MIT

pragma solidity ^0.8.9;

import {Ownable} from "@openzeppelin/contracts/access/Ownable.sol";
import {AggregatorV3Interface} from "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

error FundMe__TooLowFundSent();

contract FundMe is Ownable {
    mapping(address => uint256) public s_addressToAmountFunded;
    uint256 public immutable s_minFundUSD = 1 * 10**18;
    AggregatorV3Interface internal s_dataFeed;

    // Uses sepolia field - hard-wired but it is okay
    constructor() {
        s_dataFeed = AggregatorV3Interface(
            0x694AA1769357215DE4FAC081bf1f309aDC325306
        );
    }

    function fund() public payable {
        if (convertWeiToUsd(msg.value) < s_minFundUSD) {
            revert FundMe__TooLowFundSent();
        }

        s_addressToAmountFunded[msg.sender] += msg.value;
    }

    function withdraw() public payable onlyOwner {
        payable(msg.sender).transfer(address(this).balance);
    }

    function convertWeiToUsd(uint256 weiAmount) private view returns (uint256) {
        uint256 ethPrice = getPrice();
        return (weiAmount * ethPrice) / (1e18);
    }

    function getPrice() private view returns (uint256) {
        // prettier-ignore
        (
            /* uint80 roundID */,
            int answer,
            /*uint startedAt*/,
            /*uint timeStamp*/,
            /*uint80 answeredInRound*/
        ) = s_dataFeed.latestRoundData();
        return uint256(answer) * 10**10;
    }
}
