from brownie import accounts, config, network


def get_account():
    if network.show_active() == 'development':
        return accounts[0]
    else:
        # return accounts.load("ethereum-dev")
        # return accounts.add(str(os.getenv("WEB3_PRIVATE_KEY")))
        return accounts.add(config["wallets"]["from_key"])
