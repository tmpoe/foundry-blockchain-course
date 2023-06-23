
from brownie import Contract

from scripts.utils import get_account, get_abi

SEPOLIA_CH_ADDRESS = "0x1b30DA2a868704483143A4D46865Ac9585629fd0"
TWITTER_HANDLE = "its_a_me_TMP"

BOOLEAN_ARRAY_LENGTH = 5


def main():
    account = get_account()
    print(f"Solving 4th challenge with account {account.address}")
    
    guessed_price = 18858727000000000000000
    challenge4 = Contract.from_abi(
        "LessonFour",
        SEPOLIA_CH_ADDRESS,
        get_abi("scripts/challenge-4/challange_abi.json"),
    )
    
    tx = challenge4.solveChallenge(guessed_price, TWITTER_HANDLE, {"from": account})
    tx.wait(1)
    print(tx)
    print(dir(tx))
