
from brownie import Contract

from scripts.utils import get_account, get_abi

SEPOLIA_CH_ADDRESS = "0xD7D127991c6A89Df752FC3daeC17540aE8B86101"
TWITTER_HANDLE = "its_a_me_TMP"


def main():
    account = get_account()
    print(f"Solving 7th challenge with account {account.address}")
    
    challenge7 = Contract.from_abi(
        "LessonSeven",
        SEPOLIA_CH_ADDRESS,
        get_abi("scripts/challenge-7/challange_abi.json"),
    )
    
    tx = challenge7.solveChallenge(123, TWITTER_HANDLE, {"from": account, "gas": 123411, "allow_revert": True})
    tx.wait(1)
    print(tx)
    print(dir(tx))
