
import requests
from src.config.config import Config


def send_telegram_notification(deposit):
    message = (
        f"New Deposit Detected!\n"
        f"Tx Hash: {deposit.tx_hash}\n"
        f"Block Number: {deposit.block_number}\n"
        f"Amount: {deposit.fee} ETH\n"
        f"Pubkey: {deposit.pubkey}"
    )

    url = f"https://api.telegram.org/bot{Config.TELEGRAM_BOT_TOKEN}/sendMessage"
    params = {
        'chat_id': Config.TELEGRAM_CHAT_ID,
        'text': message
    }

    try:
        response = requests.get(url, params=params)
        if response.status_code == 200:
            print(f"Telegram notification sent for deposit {deposit.tx_hash}")
        else:
            print(f"Failed to send Telegram notification: {response.status_code}")
    except Exception as e:
        print(f"Error sending Telegram notification: {e}")
