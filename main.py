import telebot
import config
import random



bot = telebot.TeleBot(config.telegram_token)

chislo = random.randint(1, 10)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Привет, я загадал число от 1 до 10. Угадай его.")
    else:
        if int(message.text) == chislo:
            bot.send_message(message.from_user.id, "Вы угадали!!!")

        if int(message.text) > chislo:
            bot.send_message(message.from_user.id, "Нет это не " + message.text + ". А число которое я загадал меньше.")
        if int(message.text) < chislo:
            bot.send_message(message.from_user.id, "Нет это не " + message.text + ". А число которое я загадал больше.")


bot.polling()