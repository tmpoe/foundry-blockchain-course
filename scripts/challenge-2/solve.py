from brownie import Contract

from scripts.utils import get_account, get_abi

SEPOLIA_MINT_ADDRESS = "0x5c1ddb86F11BB46D3067C702AC554aEaED9ff8f0"
TWITTER_HANDLE = ""


def main():
    account = get_account()
    print(f"Solvind 2nd challenge with account {account.address}")
    mint_contract = Contract.from_abi(
        "LessonTwo",
        SEPOLIA_MINT_ADDRESS,
        get_abi("scripts/challenge-2/challange_abi.json"),
    )
    print(mint_contract)

    tx = mint_contract.solveChallenge(123, TWITTER_HANDLE, {"from": account})
    tx.wait(1)
    print(tx.txid)  # 0xe7b69c35bafa42d6d1fd2be79fe44c6f72488be331e82e91e727032bc7f14926