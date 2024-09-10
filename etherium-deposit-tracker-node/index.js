import Web3 from 'web3';
import dotenv from 'dotenv';
import fs from 'fs';

// Load environment variables from .env file
dotenv.config();

// Initialize web3 instance using Infura/Alchemy API
const web3 = new Web3(`https://mainnet.infura.io/v3/${process.env.INFURA_API_KEY}`);

// Function to track and fetch transaction details
const trackTransaction = async (txHash) => {
  try {
    // Fetch the transaction by hash
    const transaction = await web3.eth.getTransaction(txHash);

    if (transaction) {
      console.log(`Transaction Hash: ${transaction.hash}`);
      console.log(`Block Number: ${transaction.blockNumber}`);
      console.log(`From: ${transaction.from}`);
      console.log(`To: ${transaction.to}`);
      console.log(`Value: ${web3.utils.fromWei(transaction.value, 'ether')} ETH`);

      // Fetch transaction receipt for additional details
      const receipt = await web3.eth.getTransactionReceipt(txHash);

      if (receipt) {
        console.log(`Status: ${receipt.status ? 'Success' : 'Failed'}`);
        console.log(`Gas Used: ${receipt.gasUsed}`);

        // Store deposit data in a JSON file
        const depositData = {
          transactionHash: transaction.hash,
          blockNumber: transaction.blockNumber,
          from: transaction.from,
          to: transaction.to,
          value: web3.utils.fromWei(transaction.value, 'ether'),  // Convert value to ETH
          status: receipt.status ? 'Success' : 'Failed',
          gasUsed: receipt.gasUsed, // gasUsed might be a BigInt
        };
        saveToJSON(depositData);
      }
    } else {
      console.log(`Transaction ${txHash} not found.`);
    }
  } catch (error) {
    console.error(`Error fetching transaction ${txHash}:`, error);
  }
};

// Function to save deposit data to a JSON file
const saveToJSON = (depositData) => {
  const filePath = './tracked_deposits.json';

  // Recursively convert BigInt values to strings in an object
  const convertBigIntToString = (obj) => {
    for (let key in obj) {
      if (typeof obj[key] === 'bigint') {
        obj[key] = obj[key].toString(); // Convert BigInt to string
      } else if (typeof obj[key] === 'object' && obj[key] !== null) {
        convertBigIntToString(obj[key]); // Recursively convert if nested object
      }
    }
  };

  // Convert BigInt fields to strings in the depositData object
  convertBigIntToString(depositData);

  // Check if the JSON file already exists and read its contents
  let deposits = [];
  if (fs.existsSync(filePath)) {
    const data = fs.readFileSync(filePath);
    deposits = JSON.parse(data);
  }

  // Add the new deposit data
  deposits.push(depositData);

  // Write the updated deposits to the file
  fs.writeFileSync(filePath, JSON.stringify(deposits, null, 2));
  console.log('Deposit data saved to tracked_deposits.json');
};

// Example transaction hashes to track
const depositTx1 = '0x1391be19259f10e01336a383217cf35344dd7aa157e95030f46235448ef5e5d6';
const depositTx2 = '0x53c98c3371014fd54275ebc90a6e42dffa2eee427915cab5f80f1e3e9c64eba4';

// Call the function to track both deposits
trackTransaction(depositTx1);
trackTransaction(depositTx2);
