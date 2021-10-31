import os
import telebot


bot = telebot.TeleBot("2059677624:AAGUQpY8_WrRtc8aTwOoR_j4NJUsP8wh3rE")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "Hello! I'm Hatrshila Chat Bot")


@bot.message_handler(commands=["how"])
def send_message(message):
  bot.send_message(message, "How")


bot.polling()

