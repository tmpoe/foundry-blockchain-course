from scripts.utils import get_value_at_storage_location
SEPOLIA_CH_ADDRESS = "0xD7D127991c6A89Df752FC3daeC17540aE8B86101"

def main():
    get_value_at_storage_location(SEPOLIA_CH_ADDRESS, 777)