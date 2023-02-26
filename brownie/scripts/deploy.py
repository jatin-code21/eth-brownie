from brownie import BasicContract, config, accounts
import os

def deploy_wallet():
    account = accounts.add(config["wallets"]["from_key"])
    wallet = BasicContract.deploy({"from":account}, publish_source=True)
    print(f"Contract deployed to {wallet.address}")
def main():
    deploy_wallet()