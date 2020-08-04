import telebot
from telebot import types
import requests
import config
from bs4 import BeautifulSoup



bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def welcome(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup = types.InlineKeyboardMarkup(row_width=1)
    markup = types.InlineKeyboardMarkup(row_width=1)
    Dollar = types.InlineKeyboardButton("Dollars(USD)", callback_data='dollar')
    Euro = types.InlineKeyboardButton("Euro(EUR)", callback_data='euro')
    Bitcoin = types.InlineKeyboardButton("Bitcoin(BTC)", callback_data='bitcoin')
    Ethereum = types.InlineKeyboardButton("Ethereum(ETC)", callback_data='ethereum')
    Litecoin = types.InlineKeyboardButton("Litecoin(LTC)", callback_data='litecoin')
    Ripple = types.InlineKeyboardButton("Ripple(XRP)", callback_data='ripple')
    BitcoinCash = types.InlineKeyboardButton("Bitcoin Cash(BTC Cash)", callback_data='bitcoin_cash')
    Dash = types.InlineKeyboardButton("Digital Cash(Dash)", callback_data='dash')
    EthereumClassic = types.InlineKeyboardButton("Ethereum Classic(ETC Classic)", callback_data='ethereum_classic')
    IOTA = types.InlineKeyboardButton("IOTA(IOT)", callback_data='iota')
    NEO = types.InlineKeyboardButton("Neo(NEO)", callback_data='neo')
    NEM = types.InlineKeyboardButton("NEM(XEM)", callback_data='nem')
    Tether = types.InlineKeyboardButton("Tether(USDT)", callback_data='tether')
    Tezos = types.InlineKeyboardButton("Tezos(XTZ)", callback_data='tezos')
    TRON = types.InlineKeyboardButton("TRON(TRX)", callback_data='tron')

    markup.add(Dollar, Euro, Bitcoin, Ethereum, Litecoin, Ripple, BitcoinCash, Dash, EthereumClassic, IOTA, NEO, NEM, Tether, Tezos, TRON)

    bot.send_message(message.chat.id, "Вас приветствует бот по отслеживанию курса валют" + "\n" + "-"*71 + "\n" + "Выберите валюту, чтобы узнать ее курс на данный момент" + "\n" +  "-"*71, reply_markup=markup)




@bot.callback_query_handler(func=lambda call:True)
def info(call):
    if call.data == 'dollar':
        doll_RUB = config.dollars
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
        full_page = requests.get(doll_RUB, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll('span', {"class": "DFlfde SwHCTb", "data-precision":2})
        bot.send_message(call.message.chat.id, "="*37 + "\n" + "Курс 1 Dollar на данный момент: " + convert[0].text + " рублей" + "\n" + "="*37)



    elif call.data == 'euro':
        eu_RUB = config.euros
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
        full_page = requests.get(eu_RUB, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll('span', {"class": "DFlfde SwHCTb", "data-precision":2})
        bot.send_message(call.message.chat.id, "="*37 + "\n" + "Курс 1 Euro на данный момент: " + convert[0].text + " рублей" + "\n" + "="*37)



    elif call.data == 'bitcoin':
        BITCOIN_RUB = config.bitcoin
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
        full_page = requests.get(BITCOIN_RUB, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll('span', {"class": "DFlfde SwHCTb", "data-precision":2})
        bot.send_message(call.message.chat.id, "="*37 + "\n" + "Курс 1 Bitcoin на данный момент: " + convert[0].text + " рублей" + "\n" + "="*37)



    elif call.data == 'ethereum':
        Ethereum_RUB = config.ethereum
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
        full_page = requests.get(Ethereum_RUB, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll('span', {"class": "DFlfde SwHCTb", "data-precision":2})
        bot.send_message(call.message.chat.id, "="*37 + "\n" + "Курс 1 Ethereum на данный момент: " + convert[0].text + " рублей" + "\n" + "="*37)



    elif call.data == 'litecoin':
        Litecoin_RUB = config.litecoin
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
        full_page = requests.get(Litecoin_RUB, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll('span', {"class": "DFlfde SwHCTb", "data-precision":2})
        bot.send_message(call.message.chat.id, "="*37 + "\n" + "Курс 1 Litecoin на данный момент: " + convert[0].text + " рублей" + "\n" + "="*37)



    elif call.data == 'ripple':
        Ripple_RUB = config.ripple
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
        full_page = requests.get(Ripple_RUB, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll('span', {"class": "arial_26 inlineblock pid-1056895-last"})
        bot.send_message(call.message.chat.id, "="*37 + "\n" + "Курс 1 Ripple на данный момент: " + convert[0].text + " рублей" + "\n" + "="*37)



    elif call.data == 'bitcoin_cash':
        BitcoinCash_RUB = config.bitcoinCash
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
        full_page = requests.get(BitcoinCash_RUB, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll('span', {"class": "DFlfde SwHCTb", "data-precision":2})
        bot.send_message(call.message.chat.id, "="*37 + "\n" + "Курс 1 Bitcoin Cash на данный момент: " + convert[0].text + " рублей" + "\n" + "="*37)



    elif call.data == 'dash':
        Dash_RUB = config.dash
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
        full_page = requests.get(Dash_RUB, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll('span', {"class": "arial_26 inlineblock pid-1031690-last"})
        bot.send_message(call.message.chat.id, "="*37 + "\n" + "Курс 1 Dash на данный момент: " + convert[0].text + " рублей" + "\n" + "="*37)



    elif call.data == 'ethereum_classic':
        ethereumClassic_RUB = config.ethereumClassic
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
        full_page = requests.get(ethereumClassic_RUB, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll('div', {"class": "crypto_curr_val"})
        bot.send_message(call.message.chat.id, "="*37 + "\n" + "Курс 1 Ethereum Classic на данный момент: " + convert[0].text + " рублей" + "\n" + "="*37)



    elif call.data == 'iota':
        Iota_RUB = config.iota
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
        full_page = requests.get(Iota_RUB, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll('span', {"class": "arial_26 inlineblock pid-1064456-last"})
        bot.send_message(call.message.chat.id, "="*37 + "\n" + "Курс 1 Iota на данный момент: " + convert[0].text + " рублей" + "\n" + "="*37)



    elif call.data == 'neo':
        Neo_RUB = config.neo
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
        full_page = requests.get(Neo_RUB, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll('span', {"class": "arial_26 inlineblock pid-1122696-last"})
        bot.send_message(call.message.chat.id, "="*37 + "\n" + "Курс 1 Neo на данный момент: " + convert[0].text + " рублей" + "\n" + "="*37)



    elif call.data == 'nem':
        Nem_RUB = config.nem
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
        full_page = requests.get(Nem_RUB, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll('div', {"class": "analytics-crypto-item__instrument-price-left"})
        bot.send_message(call.message.chat.id, "="*37 + "\n" + "Курс 1 Nem на данный момент: " + convert[0].text + " рублей" + "\n" + "="*37)



    elif call.data == 'tether':
        Tether_RUB = config.tether
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
        full_page = requests.get(Tether_RUB, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll('span', {"class": "no-wrap"})
        bot.send_message(call.message.chat.id, "="*37 + "\n" + "Курс 1 Tether на данный момент: " + convert[0].text + " рублей" + "\n" + "="*37)



    elif call.data == 'tezos':
        tezos_RUB = config.tezos
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
        full_page = requests.get(tezos_RUB, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll('table', {"class": "curr_minmax"})
        bot.send_message(call.message.chat.id, "="*37 + "\n" + "Курс 1 Tezos на данный момент: " + convert[0].text + " рублей" + "\n" + "="*37)



    elif call.data == 'tron':
        Tron_RUB = config.tron
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"}
        full_page = requests.get(Tron_RUB, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll('span', {"class": "arial_26 inlineblock pid-1064461-last"})
        bot.send_message(call.message.chat.id, "="*37 + "\n" + "Курс 1 Tron на данный момент: " + convert[0].text + " рублей" + "\n" + "="*37)

@bot.message_handler(commands=['help'])
def help_me(message):
    bot.send_message(message.chat.id, "Техподдержка: https://t.me/CrystopherBauman" + "\n" + "-"*70 + "\n" + "🔥 У нас пояивлся обменник-бот с минимальной комиссией в 2%! 🔥 https://t.me/CryptoExchangerRUbot")






















bot.polling(none_stop=True)
