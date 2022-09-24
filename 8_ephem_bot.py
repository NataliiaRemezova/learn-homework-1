"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import datetime
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
import ephem


PLANETS = ['Sun', 'Moon', 'Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']


logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    filename="bot.log", level=logging.INFO)


def talk_to_me(update, context):
    text = update.message.text
    logging.info(f"The user sent new message: {text}")
    print(f"New Message: {text}")
    update.message.reply_text(text)


def greet_user(update, context):
    print("Was called /start")
    update.message.reply_text("Hello!")
    update.message.reply_text("If you want to know in which constellation was one of "
                              "the planet of Solar system, type '/planet' and then the name of planet\n"
                              f"Available planets: {PLANETS}\n"
                              "Example: '/planet Mars'")


def is_message_of_planets_correct(text):
    return len(str.split(text)) == 2


def is_planet_correct(text):
    if text in PLANETS:
        return True
    return False


def define_constellation_of_planet(planet):
    year_today = datetime.datetime.now().strftime('%Y')
    if planet == 'Sun':
        return ephem.constellation(ephem.Sun(year_today))
    elif planet == 'Moon':
        return ephem.constellation(ephem.Moon(year_today))
    elif planet == 'Mercury':
        return ephem.constellation(ephem.Mercury(year_today))
    elif planet == 'Venus':
        return ephem.constellation(ephem.Venus(year_today))
    elif planet == 'Mars':
        return ephem.constellation(ephem.Mars(year_today))
    elif planet == 'Jupiter':
        return ephem.constellation(ephem.Jupiter(year_today))
    elif planet == 'Saturn':
        return ephem.constellation(ephem.Saturn(year_today))
    elif planet == 'Uranus':
        return ephem.constellation(ephem.Uranus(year_today))
    elif planet == 'Neptune':
        return ephem.constellation(ephem.Neptune(year_today))
    elif planet == 'Pluto':
        return ephem.constellation(ephem.Pluto(year_today))


def find_constellation_of_planet(update, context):
    print("Was called /planet")
    text = update.message.text
    logging.info(f"The user sent new message: {text}")
    if not is_message_of_planets_correct(text) or not is_planet_correct(str.split(text)[1]):
        update.message.reply_text("Wrong message or planet!\n"
                                  f"Available planets: {PLANETS}\n"
                                  "Example: '/planet Mars'")
        return
    update.message.reply_text("This planet today is located in: ")
    update.message.reply_text(define_constellation_of_planet(str.split(text)[1]))


def main():
    my_bot = Updater(settings.API_KEY, use_context=True)

    dispatcher = my_bot.dispatcher
    dispatcher.add_handler(CommandHandler("start", greet_user))
    dispatcher.add_handler(CommandHandler("planet", find_constellation_of_planet))
    dispatcher.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Bot has started the work")
    my_bot.start_polling()
    my_bot.idle()


if __name__ == "__main__":
    main()
