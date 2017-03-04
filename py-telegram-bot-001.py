# -*- coding: utf-8 -*-
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import os
import logging
#import config
import csv


telegram_token = "342496596:AAGdzdiuSuNB7kcx4uDsqtNsEkghg0PXa58"
#telegram_token = config.telegram_token
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level= logging.INFO)
logger = logging.getLogger(__name__)

updater = Updater(telegram_token)
dispatcher = updater.dispatcher

spb_adm=u'адмиралтейский'
spb_vas=u'василеостровский'
spb_vyb=u'выборгский'
spb_kln=u'калининский'
spb_kir=u'кировский'
spb_krg=u'красногвардейский'
spb_krs=u'красносельский'
spb_krd=u'кронштадский'
spb_msk=u'московский'
spb_nev=u'невский'
spb_prd=u'петроградский'
spb_pdv=u'петродворцовый'
spb_prm=u'приморский'
spb_frz=u'фрунзенский'
spb_cnt=u'центральный'

keyboard = [[InlineKeyboardButton(spb_adm, callback_data='spb_adm')], # адмиралтейский
            [InlineKeyboardButton(spb_vas, callback_data='spb_vas')], # василеостровский
            [InlineKeyboardButton(spb_vyb, callback_data='spb_vyb')], # выборгский
            [InlineKeyboardButton(spb_kln, callback_data='spb_kln')], # калининский
            [InlineKeyboardButton(spb_kir, callback_data='spb_kir')], # кировский
            [InlineKeyboardButton(spb_krg, callback_data='spb_krg')], # красногвардейский
            [InlineKeyboardButton(spb_krs, callback_data='spb_krs')], # красносельский
            [InlineKeyboardButton(spb_krd, callback_data='spb_krd')], # кронштадский
            [InlineKeyboardButton(spb_msk, callback_data='spb_msk')], # московский
            [InlineKeyboardButton(spb_nev, callback_data='spb_nev')], # невский
            [InlineKeyboardButton(spb_prd, callback_data='spb_prd')], # петроградский
            [InlineKeyboardButton(spb_pdv, callback_data='spb_pdv')], # петродворцовый
            [InlineKeyboardButton(spb_prm, callback_data='spb_prm')], # приморский
            [InlineKeyboardButton(spb_frz, callback_data='spb_frz')], # фрунзенский
            [InlineKeyboardButton(spb_cnt, callback_data='spb_cnt')]  # центральны                
            ]

def find_address(district=None):
    result = ""
    if district!=None:
        with open('D:\\Projects\\Py-Telegram-Bot\\districts.csv') as csvfile:
             reader = csv.reader(csvfile, delimiter=',', quotechar='"')
             for row in reader:
                 if result != "":
                     result += "\n"
                 if district.lower() == row[0].lower():
                     result += row[1]
    return result

def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat.id, text='Привет! Я помогу Вам правильно рассортировать Ваши отходы.'\
                    'Доступные команды:'\
                    '/start - начало работы со мой'\
                    '/helpme - помощь по командам и как мной пользоваться'\
                    '/recycle или /recycle <наименование> - введите ключевое слово, к примеру "пластиковая бутылка" и я помогу определить можно ее утилизировать или нет'\
                    '/where или /where <район города> - подскажу, где пункт сбора в вашем районе'\
                    '/types - подскажу какие отходы бывают'\
                    '/metro или /metro <станция метро> - подскажу, где пункт сбора отностельно метро')

"""
/recycle
/where
/types
/metro
"""

def recycle_cmd(bot, update, **args):
    print (args)
    bot.sendMessage(chat_id=update.message.chat.id, text='recycle!!')
    recycle_args = args.get("args")
    bot.sendMessage(chat_id=update.message.chat.id, text=len(recycle_args).__str__())

def where_cmd(bot, update, **args):
    msgText = 'where!! '
    query = update.callback_query
    where_args = args.get("args")
    buttonsListFlg=False
    address = ""
    if len(where_args) > 0:
        print (where_args[0])
        address= find_address(where_args[0])
        if address!="":
            msgText=msgText+' '+address;
        else:
            buttonsListFlg=True
    else:
        buttonsListFlg=True
    if buttonsListFlg:
        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.sendMessage(chat_id=update.message.chat_id, reply_markup=reply_markup, text='Выберите пожалуйста район города:')
    else:
        bot.sendMessage(chat_id=update.message.chat.id, text=msgText)    
    
def types_cmd(bot, update, pass_args=True):
    bot.sendMessage(chat_id=update.message.chat.id, text='types!!')

def help_cmd(bot, update):
    bot.sendMessage(chat_id=update.message.chat.id, text='Привет!'\
                    'Доступные команды:'\
                    '/recycle или /recycle <наименование> - введите ключевое слово, к примеру "пластиковая бутылка" и я помогу определить можно ее утилизировать или нет'\
                    '/where или /where <район города> - подскажу, где пункт сбора в вашем районе'\
                    '/types - подскажу какие отходы бывают'\
                    '/metro или /metro <станция метро> - подскажу, где пункт сбора отностельно метро')

def metro_cmd(bot, update, **args):
    bot.sendMessage(chat_id=update.message.chat.id, text='Метро:')

def button(bot, update):
    query = update.callback_query
    city_place_code = query.data
    keyboard_back = [[InlineKeyboardButton(" «< ", callback_data='back')]]
    reply_markup = InlineKeyboardMarkup(keyboard_back)
    if city_place_code == 'back':
        text = 'Пожалуйста, выберите, район города:'
        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.sendMessage(chat_id=query.message.chat.id, text=text, reply_markup=reply_markup,message_id=query.message.message_id)
    elif city_place_code == 'spb_adm':
        city_place = spb_adm
    elif city_place_code == 'spb_vas':
        city_place = spb_vas
    elif city_place_code == 'spb_vyb':
        city_place = spb_vyb
    elif city_place_code == 'spb_kln':
        city_place = spb_kln
    elif city_place_code == 'spb_kir':
        city_place = spb_kir
    elif city_place_code == 'spb_krg':
        city_place = spb_krg
    elif city_place_code == 'spb_krs':
        city_place = spb_krs
    elif city_place_code == 'spb_krd':
        city_place = spb_krd
    elif city_place_code == 'spb_msk':
        city_place = spb_msk
    elif city_place_code == 'spb_nev':
        city_place = spb_nev
    elif city_place_code == 'spb_prd':
        city_place = spb_prd
    elif city_place_code == 'spb_pdv':
        city_place = spb_pdv
    elif city_place_code == 'spb_prm':
        city_place = spb_prm
    elif city_place_code == 'spb_frz':
        city_place = spb_frz
    elif city_place_code == 'spb_cnt':
        city_place = spb_cnt
    address= find_address(city_place)
    if address == "":
        address = "В данном районе нет пункта сбора. Просьба выборать ближайший район города к вашему"
        bot.sendMessage(chat_id=query.message.chat.id, text=address, reply_markup=reply_markup,message_id=query.message.message_id)
    else:
        bot.sendMessage(chat_id=update.message.chat.id, text=address)

start_handler = CommandHandler('start', start)
recycle_handler = CommandHandler('recycle', recycle_cmd, pass_args=True)
where_handler = CommandHandler('where', where_cmd, pass_args=True)
types_handler = CommandHandler('types', types_cmd, pass_args=True)
help_handler = CommandHandler('helpme', help_cmd)
metro_handler = CommandHandler('helpme', metro_cmd, pass_args=True)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(recycle_handler)
dispatcher.add_handler(where_handler)
dispatcher.add_handler(types_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(CallbackQueryHandler(button))

if __name__ == '__main__':
    updater.start_polling()
    updater.idle()
    #updater.start_webhook(listen='127.0.0.1', port=5003, url_path=telegram_token)
    #updater.bot.setWebhook(webhook_url='https://95.85.37.72/'+telegram_token,
    #                       certificate=open('/home/deploy/it-volunteer-bot/cert.pem', 'rb'))
    print('hi')
