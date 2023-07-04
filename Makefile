ONESHELL:

-include .env

test-backend:
	set -o allexport; source .env; set +o allexport; brownie test

echo-test-backend:
	echo "set -o allexport; source .env; set +o allexport; brownie test"

lint:
	black .; \
	ruff scripts/ tests/

install:
	pip install ."[dev]"

compile:
	brownie compile

add-sepolia-infura:
	set -o allexport; source .env; brownie networks add Ethereum sepolia host="https://sepolia.infura.io/v3/${WEB3_INFURA_PROJECT_ID}" chainid=11155111

add-sepolia-alchemy:
	set -o allexport; source .env; brownie networks add Ethereum sepolia host="https://eth-sepolia.g.alchemy.com/v2/${WEB3_ALCHEMY_PROJECT_ID}" chainid=11155111 

deploy-sepolia:
	set -o allexport; source .env; brownie run scripts/deploy.py --network sepolia

solve-1:
	brownie run scripts/challenge-1/solve.py --network sepolia

solve-2:
	brownie run scripts/challenge-2/solve.py --network sepolia

solve-3:
	brownie run scripts/challenge-3/solve.py --network sepolia

solve-4:
	brownie run scripts/challenge-4/solve.py --network sepolia

solve-5:
	brownie run scripts/challenge-5/solve.py --network sepolia

solve-6:
	source .env; cast send 0x6c4791c3a9E9Bc5449045872Bd1b602d6385E3E1 "solveChallenge(string, string)" "hazelnut" "its_a_me_TMP" --private-key $(PRIVATE_KEY) --rpc-url $(ALCHEMY_SEPOLIA_RPC_URL)

solve-7:
	source .env; cast send 0xD7D127991c6A89Df752FC3daeC17540aE8B86101 "solveChallenge(uint256, string)" 84914 "its_a_me_TMP" --private-key $(PRIVATE_KEY) --rpc-url $(ALCHEMY_SEPOLIA_RPC_URL)

solve-6-py:
	brownie run scripts/challenge-6/solve.py --network sepolia

solve-7-py:
	brownie run scripts/challenge-7/solve.py --network sepolia
