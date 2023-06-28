ONESHELL:

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

add-sepolia:
	set -o allexport; source .env; brownie networks add Ethereum sepolia host="https://sepolia.infura.io/v3/${WEB3_INFURA_PROJECT_ID}" chainid=11155111

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
	source .env; cast send 0x6c4791c3a9E9Bc5449045872Bd1b602d6385E3E1 "solveChallenge(string, string)" "hazelnut" "its_a_me_TMP" -f 0xC75444ef801b50f5601230db66F784e2078BE7Bb --rpc-url $$SEPOLIA_RPC_URL