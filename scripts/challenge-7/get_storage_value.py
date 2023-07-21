from scripts.utils import get_value_at_storage_location

SEPOLIA_CH_ADDRESS = "0xD7D127991c6A89Df752FC3daeC17540aE8B86101"
SEPOLIA_CH_9_ADDRESS = "0x33e1fD270599188BB1489a169dF1f0be08b83509"


def main():
    # get_value_at_storage_location(SEPOLIA_CH_ADDRESS, 777)
    get_value_at_storage_location(SEPOLIA_CH_ADDRESS, 1)
