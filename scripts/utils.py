import json

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
