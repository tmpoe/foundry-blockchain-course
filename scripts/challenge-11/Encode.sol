// SPDX-license-identifier: MIT

pragma solidity ^0.8.20;

contract Encode {
    function encode2() public pure returns (bytes memory) {
        return
            abi.encodeWithSignature(
                "returnTrueWithGoodValues(uint256,address)",
                9,
                0x28B4144Fe74b486a87e68074189Aa60f59577602
            );
    }

    function encode1() public pure returns (bytes4) {
        return bytes4(keccak256("returnTrue()"));
    }
}
