
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    RPC_URL ='https://mainnet.infura.io/v3/0daf7c0d23ae4db68e74242779b7c099'
    DEPOSIT_CONTRACT_ADDRESS ='0x00000000219ab540356cBB839Cbe05303d7705Fa'
    TELEGRAM_BOT_TOKEN ='6753479142:AAHQVev9q6DskcwlQcruAybMs0vyk9H_xlY'
    TELEGRAM_CHAT_ID ='@sayu_018'
    DATABASE_URI ='mongodb+srv://sayu:sayu18@cluster0.rex6x.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
    DB_NAME ='eth_deposit_tracker'


