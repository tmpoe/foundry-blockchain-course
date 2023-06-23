
from brownie import Contract

from scripts.utils import get_account, get_abi

SEPOLIA_CH_ADDRESS = "0x4b3a7F293091708dDD6B8748179aeAF80E9c1bA2"
TWITTER_HANDLE = "its_a_me_TMP"

BOOLEAN_ARRAY_LENGTH = 5


def main():
    account = get_account()
    print(f"Solving 5th challenge with account {account.address}")
    
    pw = "password"
    challenge5 = Contract.from_abi(
        "LessonFive",
        SEPOLIA_CH_ADDRESS,
        get_abi("scripts/challenge-5/challange_abi.json"),
    )
    
    tx = challenge5.solveChallenge(pw, TWITTER_HANDLE, {"from": account})
    tx.wait(1)
    print(tx)
    print(dir(tx))
