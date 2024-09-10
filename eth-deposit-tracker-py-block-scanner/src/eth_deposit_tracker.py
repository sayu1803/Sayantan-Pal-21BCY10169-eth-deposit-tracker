from web3 import Web3
from datetime import datetime
from src.config.config import Config  # This assumes config.py is in the src directory

from src.db import store_deposit
from src.telegram_notifications import send_telegram_notification
from src.utils import get_pubkey_from_tx

import sys
import os

# Add the project root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Connect to Ethereum node
web3 = Web3(Web3.HTTPProvider(Config.RPC_URL))

# Beacon Deposit Contract Address
DEPOSIT_CONTRACT_ADDRESS = Web3.to_checksum_address(Config.DEPOSIT_CONTRACT_ADDRESS)

# Class to store deposit data
class Deposit:
    def __init__(self, block_number, block_timestamp, fee, tx_hash, pubkey):
        self.block_number = block_number
        self.block_timestamp = block_timestamp
        self.fee = fee
        self.tx_hash = tx_hash
        self.pubkey = pubkey

    def to_dict(self):
        return {
            'block_number': self.block_number,
            'block_timestamp': self.block_timestamp,
            'fee': self.fee,
            'tx_hash': self.tx_hash,
            'pubkey': self.pubkey,
        }

# Track deposits
def track_deposits():
    latest_block = web3.eth.block_number
    print(f"Starting deposit tracker at block {latest_block}...")

    while True:
        try:
            current_block = web3.eth.block_number
            if current_block > latest_block:
                for block_number in range(latest_block + 1, current_block + 1):
                    process_block(block_number)
                latest_block = current_block
        except Exception as e:
            print(f"Error in fetching block: {e}")

# Process each block to detect deposits
def process_block(block_number):
    block = web3.eth.get_block(block_number, full_transactions=True)
    print(f"Processing Block {block_number}")

    for tx in block.transactions:
        if tx.to and tx.to.lower() == DEPOSIT_CONTRACT_ADDRESS.lower():
            # Extract deposit details
            gas_fee = web3.fromWei(tx.gas_price * tx.gas, 'ether')
            pubkey = get_pubkey_from_tx(tx)  # Get pubkey using ABI decoding

            deposit = Deposit(
                block_number=block_number,
                block_timestamp=datetime.utcfromtimestamp(block.timestamp).isoformat(),
                fee=str(gas_fee),
                tx_hash=tx.hash.hex(),
                pubkey=pubkey
            )

            # Store deposit in the database
            store_deposit(deposit)

            # Send Telegram notification
            send_telegram_notification(deposit)
            print(f"New deposit processed: {deposit.tx_hash}")

if __name__ == '__main__':
    if web3.is_connected():
        track_deposits()
    else:
        print("Failed to connect to Ethereum node.")