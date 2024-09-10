# src/utils.py
from web3 import Web3
from src.config.config import Config

# ABI for the Beacon Deposit Contract
BEACON_DEPOSIT_ABI = [
    {
        "inputs": [
            {"internalType": "bytes", "name": "pubkey", "type": "bytes"},
            {"internalType": "bytes", "name": "withdrawal_credentials", "type": "bytes"},
            {"internalType": "bytes", "name": "signature", "type": "bytes"},
            {"internalType": "bytes32", "name": "deposit_data_root", "type": "bytes32"}
        ],
        "name": "deposit",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    }
]


def get_pubkey_from_tx(tx):
    """
    Decodes the public key from the transaction input of the Beacon Deposit Contract's 'deposit' function.
    """
    try:
        # Create a contract instance using web3.py
        contract = Web3(Web3.HTTPProvider(Config.RPC_URL)).eth.contract(
            address=Config.DEPOSIT_CONTRACT_ADDRESS,
            abi=BEACON_DEPOSIT_ABI
        )

        # Decode the transaction input data using the ABI
        function_data = contract.decode_function_input(tx.input)

        # Extract the public key (first argument in the 'deposit' function)
        pubkey = function_data[1]['pubkey']

        # Return the public key as a hexadecimal string
        return pubkey.hex()

    except Exception as e:
        print(f"Error decoding transaction: {e}")
        return None
