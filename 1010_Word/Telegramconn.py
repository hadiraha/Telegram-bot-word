import asyncio
from telegram import Bot
from telegram.ext import Application
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class TelegramBot:
    def __init__(self):
        self.token = os.getenv("TELEGRAM_API_TOKEN")
        self.chat_id = os.getenv("TELEGRAM_CHAT_ID")
        if not self.token or not self.chat_id:
            raise ValueError("TELEGRAM_API_TOKEN and TELEGRAM_CHAT_ID must be set in .env")
        self.bot = Bot(token=self.token)

    async def send_message(self, text):
        """
        Sends a message to the specified Telegram chat or channel.
        """
        await self.bot.send_message(chat_id=self.chat_id, text=text)
        
    async def send_batch_messages(self, messages, batch_size=5, delay=1):
        """
        Sends messages in batches to avoid spamming too many messages.
        Introduces a delay between messages and handles flood control.
        """
        for i in range(0, len(messages), batch_size):
            batch = messages[i:i+batch_size]
            for message in batch:
                try:
                    await self.send_message(message)
                    await asyncio.sleep(delay)  # Add a delay between messages
                except Exception as e:
                    if 'Retry in' in str(e):
                        retry_after = int(str(e).split('Retry in ')[1].split(' ')[0])
                        print(f"Flood control exceeded. Retrying in {retry_after} seconds...")
                        await asyncio.sleep(retry_after)
                        await self.send_message(message)
                    else:
                        print(f"Error sending message: {e}")
# Testing the Telegram Bot integration
if __name__ == "__main__":
    async def main():
        telegram_bot = TelegramBot()
        try:
            await telegram_bot.send_message("Testing Telegram Bot")
            print("Test message sent successfully.")
        except Exception as e:
            print(f"Error sending test message: {e}")

    asyncio.run(main())