from brownie import BoxFactory

from scripts.utils import get_account

REDEPLOY = False


def main():
    account = get_account()
    if REDEPLOY:
        print(f"Deploying BoxFactory with account {account.address}")
        boxFactory = BoxFactory.deploy({"from": account})
        print(f"BoxFactory deployed to {boxFactory.address}")
    else:
        boxFactory = BoxFactory[-1]

    print(f"Calling createBox with account {account.address}")
    tx = boxFactory.createBox({"from": account})
    tx.wait(1)

    print(f"Calling store with account {account.address}")
    tx = boxFactory.store(0, 42, {"from": account})
    tx.wait(-1)

    print(f"Value of box 0 is {boxFactory.retrieve(0)}")
