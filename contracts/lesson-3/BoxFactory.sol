// SPDX-License-Identifier: MIT

pragma solidity ^0.8.9;

import {Box} from "./Box.sol";

contract BoxFactory {
    Box[] public boxes;

    function createBox() public {
        Box box = new Box();
        boxes.push(box);
    }

    function store(uint256 boxIndex, uint256 value) public {
        Box box = boxes[boxIndex];
        box.store(value);
    }

    function retrieve(uint256 boxIndex) public view returns (uint256) {
        Box box = boxes[boxIndex];
        return box.retrieve();
    }
}
