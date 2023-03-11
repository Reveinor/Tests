import telebot
import openai
import os

# Set up the Telegram bot using your bot token
bot = telebot.TeleBot('YOUR_TELEGRAM_BOT_TOKEN')

# Set up the OpenAI API using your API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Define a function to handle incoming messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Call the OpenAI API to get the answer to the user's question
    response = openai.Completion.create(
        engine='davinci',
        prompt=message.text,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Send the answer back to the user
    bot.reply_to(message, response.choices[0].text)

# Start the bot
bot.polling()
