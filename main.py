import os
import telebot


bot = telebot.TeleBot("API එක දාහන් උස්සන්නෙ නැතුව මගෙ ඒව")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "Hello! I'm Uvindu Bro Chat Bot")


@bot.message_handler(commands=["how"])
def send_message(message):
  bot.send_message(message.chat.id, "http://rewardsads.netlify.app")



bot.polling()
