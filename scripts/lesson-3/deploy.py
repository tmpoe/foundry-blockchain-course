from brownie import Contract, BoxFactory

from scripts.utils import get_account

def main():
    account = get_account()
    print(f"Deploying BoxFactory with account {account.address}")
    boxFactory = BoxFactory.deploy({"from": account})
    print(f"BoxFactory deployed to {boxFactory.address}")
