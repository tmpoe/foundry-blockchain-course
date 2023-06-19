from brownie import Contract

from scripts.utils import get_account, get_abi

SEPOLIA_MINT_ADDRESS = "0x25056312685339b49e1d1C5a0b72Ff9eff13AF77"
TWITTER_HANDLE = "its_a_me_TMP"


def main():
    account = get_account()
    print(f"Calling mint with account {account.address}")
    challenge1 = Contract.from_abi(
        "LessonOne",
        SEPOLIA_MINT_ADDRESS,
        get_abi("scripts/challenge-1/challange_abi.json"),
    )
    print(challenge1)

    tx = challenge1.solveChallenge(TWITTER_HANDLE, {"from": account})
    tx.wait(1)
    print(tx.txid)  # 0xe7b69c35bafa42d6d1fd2be79fe44c6f72488be331e82e91e727032bc7f14926
