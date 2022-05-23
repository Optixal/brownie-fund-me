from brownie import FundMe
from scripts.helper import get_account


def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee()  # 0.025 eth = $50, eth = $2000
    print(f"Entrance fee: {entrance_fee}")
    print("Funding..")
    fund_me.fundUSD({"from": account, "value": entrance_fee})


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    print("Withdrawing..")
    fund_me.withdraw({"from": account})


def main():
    fund()
    withdraw()
