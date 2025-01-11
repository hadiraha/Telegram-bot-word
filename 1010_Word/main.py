import asyncio
from docxParser import DocxParser
from Telegramconn import TelegramBot

async def main():
    # Path to the Word document
    # file_path = r'file path'  # Update this to the actual file path
    file_path = input("Enter the path to your Word document: ").strip()

    # Step 1: Extract content from the Word document
    print("Extracting content from the Word document...")
    try:
        parser = DocxParser(file_path)
        content = parser.extract_headings_content()

        if not content:
            print("No content found under 'Heading 4'. Exiting.")
            return
    except Exception as e:
        print(f"Error extracting content: {e}")
        return

    # Step 2: Send content to Telegram
    print("Sending content to Telegram...")
    try:
        bot = TelegramBot()
        await bot.send_batch_messages(content, batch_size=5, delay=1)  # Add a 1-second delay
        print("All content sent successfully!")
    except Exception as e:
        print(f"Error sending messages to Telegram: {e}")

if __name__ == "__main__":
    asyncio.run(main())