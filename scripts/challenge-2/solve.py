from brownie import Contract

from scripts.utils import get_account, get_abi

SEPOLIA_CH_ADDRESS = "0x5c1ddb86F11BB46D3067C702AC554aEaED9ff8f0"
TWITTER_HANDLE = ""


def main():
    account = get_account()
    print(f"Solving 2nd challenge with account {account.address}")
    challenge2 = Contract.from_abi(
        "LessonTwo",
        SEPOLIA_CH_ADDRESS,
        get_abi("scripts/challenge-2/challange_abi.json"),
    )
    print(challenge2)

    tx = challenge2.solveChallenge(123, TWITTER_HANDLE, {"from": account})
    tx.wait(1)
    print(tx.txid)  # 0xe7b69c35bafa42d6d1fd2be79fe44c6f72488be331e82e91e727032bc7f14926
