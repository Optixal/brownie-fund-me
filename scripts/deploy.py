from brownie import FundMe, network, config
from scripts.helper import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_account, deploy_mock_aggregator


def deploy_fund_me():
    # Get account
    account = get_account()
    print(account)

    # Deploy mock aggregator first if on development chain, else use actual aggregator
    chain = network.show_active()
    print(f"Chain being used: {chain}")
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_addr = deploy_mock_aggregator()
    else:
        price_feed_addr = config["networks"][chain]["eth_usd_price_feed"]
    print(f"Using price feed address: {price_feed_addr}")

    # Deploy FundMe
    fund_me = FundMe.deploy(
        price_feed_addr,
        {"from": account},
        publish_source=config["networks"][chain].get("verify"),
    )
    print(f"Contract deployed to {fund_me.address}")
    return fund_me


def main():
    deploy_fund_me()
