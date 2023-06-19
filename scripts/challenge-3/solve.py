from brownie import Contract

from scripts.utils import get_account, get_abi

SEPOLIA_MINT_ADDRESS = "0x4A62A8901e6113dEF0AEeEC77E531779cd40da73"
TWITTER_HANDLE = "its_a_me_TMP"

BOOLEAN_ARRAY_LENGTH = 5


def main():
    account = get_account()
    print(f"Solving 3rd challenge with account {account.address}")
    challenge3 = Contract.from_abi(
        "LessonThree",
        SEPOLIA_MINT_ADDRESS,
        get_abi("scripts/challenge-3/challange_abi.json"),
    )

    for i in range(BOOLEAN_ARRAY_LENGTH):
        try:
            tx = challenge3.solveChallenge(i, 3, TWITTER_HANDLE, {"from": account})
            tx.wait(1)
            print(tx)
            print(dir(tx))
            break
        except Exception as e:
            print(e)
