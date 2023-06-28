# https://api.nasa.gov/planetary/apod?date=1998-05-05&api_key=DEMO_KEY
# https://api.nasa.gov/

import telebot, json, requests, random, time

def str_time_prop(start, end, time_format, prop):
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(time_format, time.localtime(ptime))

def random_date(start, end, prop):
    return str_time_prop(start, end, '%Y-%m-%d', prop)
    
def get_photo_from_nasa():
    data_json = requests.get(f'https://api.nasa.gov/planetary/apod?date={random_date("2016-1-1", "2023-1-1", random.random())}&api_key=DEMO_KEY')
    data = json.loads(data_json.text)

    return data.get('url')
 

token = '6050659800:AAHPcJ1bs_ZfMvxorDIWnrpb5VWakVA34ew'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['day'])
def get_everyday_photo(message):
    try:
        bot.send_photo(chat_id=message.chat.id, photo=get_photo_from_nasa(1), timeout=5)
    except:
        bot.send_message(message.chat.id, 'что-то пошло не по плану')

bot.infinity_polling()