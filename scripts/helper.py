from brownie import MockV3Aggregator, accounts, config, network
from web3 import Web3

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local"]
MOCK_AGGREGATOR_DECIMALS = 18
MOCK_AGGREGATOR_STARTING_PRICE = 2000


# If using dev, and ganache is using hardfork london (EIP-1559), specifiy gas price
if network.show_active() == "development":
    network.priority_fee("20 gwei")


def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        return accounts[0]
    else:
        # return accounts.load("ethereum-dev")
        # return accounts.add(str(os.getenv("WEB3_PRIVATE_KEY")))
        return accounts.add(config["wallets"]["from_key"])


def deploy_mock_aggregator():
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(
            MOCK_AGGREGATOR_DECIMALS, Web3.toWei(MOCK_AGGREGATOR_STARTING_PRICE, "ether"), {"from": get_account()}
        )
    else:
        print("Reusing mock aggregator.")
    address = MockV3Aggregator[-1].address
    print(f"Mock aggregator deployed to {address}")
    return address
