import requests
import time


API_url : str = 'https://api.telegram.org/bot'
API_CATS_url : str = 'https://aws.random.cat/meow'
BOT_token = '6201426279:AAEqpUOSWWIAoss33W46k1N7TKhRQbImCVI'
ERROR_text = 'Извините, *здесь* должны были быть котики :()'

offset : int = -2
counter : int = 0
cat_link : str

while counter < 100:
    print('attemp = ', counter)
    updates = requests.get(f'{API_url}{BOT_token}/getUpdates?offset={offset + 1}').json()
    # print(updates['result'])
    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']

        cat_response = requests.get(API_CATS_url)
        if cat_response.status_code == 200:
            cat_link = cat_response.json()['file']
            requests.get(f'{API_url}{BOT_token}/sendPhoto?chat_id={chat_id}&photo={cat_link}')
        else:
            requests.get(f'{API_url}{BOT_token}/sendMessage?chat_id={chat_id}&text={ERROR_text}')

    time.sleep(1)
    counter += 1
