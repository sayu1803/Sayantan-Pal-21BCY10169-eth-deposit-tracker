
# ETH Deposit Tracker -py-block-scanner

## Overview

The ETH Deposit Tracker is a Python application designed to monitor Ethereum blocks for transactions to a specified Beacon Deposit Contract address. It scans new blocks in real-time, checks for deposits, and stores relevant transaction details in a MongoDB database. It also sends notifications via Telegram for new deposits.

## Features

- Connects to an Ethereum node using RPC (Infura, Alchemy, or a local node).
- Scans Ethereum blocks to detect transactions to a specified Beacon Deposit Contract address.
- Stores deposit details in a MongoDB database.
- Sends Telegram notifications for new deposits.
- Handles real-time data fetching and processing.

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/eth-deposit-tracker.git
   cd eth-deposit-tracker
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**

   Create a `.env` file in the root directory of the project and add the following variables:

   ```plaintext
   RPC_URL='your_ethereum_rpc_url'
   DEPOSIT_CONTRACT_ADDRESS='your_deposit_contract_address'
   TELEGRAM_BOT_TOKEN='your_telegram_bot_token'
   TELEGRAM_CHAT_ID='your_telegram_chat_id'
   DATABASE_URI='your_mongodb_uri'
   DB_NAME='your_database_name'
   ```

   Replace the placeholder values with your actual configuration details.

## Usage

Run the script to start scanning Ethereum blocks:

```bash
python -m src.eth_deposit_tracker
```

The application will:

- Connect to the Ethereum node.
- Start scanning from the latest block and continue in real-time.
- Process each block to check for transactions to the specified deposit contract.
- Store details of each deposit (amount, sender address, timestamp, etc.) in the MongoDB database.
- Send a Telegram notification for each new deposit detected.

## Error Handling

The application includes comprehensive error handling for API calls and RPC interactions. Errors and important events are logged for review.

















# Ethereum Deposit Tracker - node

## Overview

The Ethereum Deposit Tracker is designed to monitor and record ETH deposits on the Beacon Deposit Contract. The application focuses on fetching and recording only the latest transactions related to the Beacon Deposit Contract address.

## Features

- **Real-Time Monitoring**: Scans for the latest transactions related to the Beacon Deposit Contract.
- **Transaction Details**: Logs essential transaction details such as block number, timestamp, sender address, and amount.
- **Error Handling**: Includes robust error handling for API interactions.
- **Optional Notifications**: (Not implemented) Potential for integration with alerting systems.

## Contract Address

- **Beacon Deposit Contract Address**: `0x00000000219ab540356cBB839Cbe05303d7705Fa`

## Installation

### Prerequisites

- Node.js (v14 or later)
- npm (Node Package Manager)

### Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/YOUR_GITHUB_USERNAME/ethereum-deposit-tracker.git
   cd ethereum-deposit-tracker
   ```
2. **Install Dependencies**

```bash

npm install
```
Environment Configuration

Create a .env file in the root directory of the project and add the following environment variable:

env
```bash
INFURA_URL=https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID
Replace YOUR_INFURA_PROJECT_ID with your Infura project ID.
```

Usage
To start the Ethereum Deposit Tracker and begin monitoring the latest transactions:

```bash
Copy code
npm start
```
The application will connect to the Ethereum network and fetch the latest transactions related to the Beacon Deposit Contract.

## Limitations

- **Current Scope**: The application only scans the latest transactions related to the Beacon Deposit Contract and does not fetch or process historical transactions.
- **Internal Transactions**: The tracking of multiple deposits within a single transaction (internal transactions) is not implemented.

## Error Handling

Errors encountered during API calls or RPC interactions are logged to the console. Proper handling should be implemented for production environments.

## Optional Features (Not Implemented)

- **Alerting and Notifications**: Integration with notification systems like Telegram for real-time alerts.
- **Visualization**: Setup for visualization tools like Grafana to display deposit data.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests for improvements or new features.

