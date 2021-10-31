import os
import telebot


bot = telebot.TeleBot("2059677624:AAEiHUtgR6VYNStUdpn1F3UaIpJQTseHmP0")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(message, "Hello! I'm Hatrshila Chat Bot")


@bot.message_handler(commands=["how"])
def send_message(message):
  bot.send_message(message, "How")


bot.polling()

