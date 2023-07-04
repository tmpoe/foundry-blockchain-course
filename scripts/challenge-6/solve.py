
from brownie import Contract

from scripts.utils import get_account, get_abi

SEPOLIA_CH_ADDRESS = "0x6c4791c3a9E9Bc5449045872Bd1b602d6385E3E1"
TWITTER_HANDLE = "its_a_me_TMP"



def main():
    account = get_account()
    print(f"Solving 6th challenge with account {account.address}")
    
    challenge6 = Contract.from_abi(
        "LessonSix",
        SEPOLIA_CH_ADDRESS,
        get_abi("scripts/challenge-6/challange_abi.json"),
    )
    
    tx = challenge6.solveChallenge('hazelnut', TWITTER_HANDLE, {"from": account})
    tx.wait(1)
    print(tx)
    print(dir(tx))
