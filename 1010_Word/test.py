from bale import Bot, Message, Update
import os
from dotenv import load_dotenv
import asyncio

# Load environment variables from .env file
load_dotenv()

class BaleBot:
    def __init__(self):
        """
        Initialize the Bale bot with API credentials from the environment variables.
        """
        self.token = os.getenv("BALE_API_TOKEN")
        self.chat_id = os.getenv("BALE_CHAT_ID")
        if not self.token or not self.chat_id:
            raise ValueError("BALE_API_TOKEN and BALE_CHAT_ID must be set in .env")
        self.bot = Bot(self.token)
        self.client = Bot(self.token)

    async def run(self,text):
        async with self.client as bot:
            await bot.send_message(chat_id=self.chat_id, text=text ) 


    # async def sending_messages(self, text):
        
    #     #Sends a message to the specified Telegram chat or channel.
        
    #     await self.bot.send_message(chat_id=self.chat_id, text=text)
        
        
    async def send_batch_messages(self, messages, batch_size=5, delay=1):
        
        # Sends messages in batches to avoid spamming too many messages.
        # Introduces a delay between messages and handles flood control.
        
        for i in range(0, len(messages), batch_size):
            batch = messages[i:i+batch_size]
            for message in batch:
                try:
                    await self.run(message)
                    await asyncio.sleep(delay)  # Add a delay between messages
                except Exception as e:
                    if 'Retry in' in str(e):
                        retry_after = int(str(e).split('Retry in ')[1].split(' ')[0])
                        print(f"Flood control exceeded. Retrying in {retry_after} seconds...")
                        await asyncio.sleep(retry_after)
                        await self.run(message)
                    else:
                        print(f"Error sending message: {e}")

# Test
if __name__ == "__main__":
    async def main():
        bale_bot = BaleBot()
        messages = ["This is a test message for Bale bot.", "Here is another message!", "Bale integration is working!"]
        try:
            await bale_bot.send_batch_messages(messages)
            print("All messages sent successfully to Bale.")
        except Exception as e:
            print(f"An error occurred while sending messages to Bale: {e}")

    asyncio.run(main())