# Telegram-bot-word
Pass an office word document, It will extract the contents bellow a specific heading, then it will send it by Telegram messenger!

This project automates the extraction of content from Microsoft Word documents (structured using Heading 4) and sends the extracted content to a Telegram group or channel. It simplifies the process of managing large volumes of Word documents and sharing their content on Telegram.

**Features**

Extracts text under Heading 4 from Word documents.
Supports Farsi and other languages.
Skips sections with no content below the Heading 4.
Sends content in batches to Telegram to comply with Telegram's rate limits.
Fully customizable for different use cases.

**Requirements**
Python 3.8+
  Libraries:
    python-docx
    python-telegram-bot
    dotenv
    

