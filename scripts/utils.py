import json
import os

from typing import Optional
from brownie import network, accounts, config
from brownie.network.account import Account

NON_FORKED_LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["hardhat", "development", "ganache"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = NON_FORKED_LOCAL_BLOCKCHAIN_ENVIRONMENTS + [
    "mainnet-fork",
    "binance-fork",
    "matic-fork",
]


def get_account(idx: Optional[int] = None) -> Account:
    if idx is not None:
        return accounts[idx]
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    return accounts.add(config["wallets"]["from_key"])


def get_abi(path):
    with open(path, encoding="utf-8") as f:
        abi = json.load(f)
        print(abi)
        return abi


def get_value_at_storage_location(contract_address, storage_location):
    from web3 import Web3

    # Connect to the Ethereum network
    infura_url = os.environ.get("INFURA_SEPOLIA_RPC_URL")
    print(f"Connecting to Infura node at {infura_url}")
    web3 = Web3(Web3.HTTPProvider(infura_url))

    # Define the contract address and storage location
    contract_address = contract_address
    storage_location = storage_location

    value = web3.eth.get_storage_at(contract_address, storage_location)
    value_int = int.from_bytes(value, byteorder="big")
    print("Value at storage location:", value_int)
