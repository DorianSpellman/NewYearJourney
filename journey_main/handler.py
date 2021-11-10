from aiohttp.client import *
from aiohttp import payload, web
from aiohttp.client import request
from random import randint, shuffle, choice

HOST_IP = "0.0.0.0"
HOST_PORT = 1288

stories = [] # Рассказы
state = 0  # Состояния

def handler_function(request):
    global state
    global stories
    buttons = []
    end_session = False
    message = ''
    session = request['session']
    version = request['version']
    request = request['request']
    list_of_request = request['nlu']['tokens']

    if session['new'] or state == 0:
        with open('steps.txt', newline='', encoding="utf-8") as fin:   
            stories = fin.readlines()

### Приветствие
        message = "Привет! Новый год - чудесное время года!" + choice (["\n Хотите отправиться в путешествие по миру этого праздника и узнать о нём больше?", "\n Отправимся в путешествие по новогоднему миру?"])   
        buttons = [button('Да!'), button('Не сейчас')]
        state = 1

### Начало       
    elif state == 1:
        
        if 'да' in list_of_request  or  'давай' in list_of_request  or  'Да!' in list_of_request  or  'вперёд' in list_of_request:
            message += choice(['Отлично, поехали!', 'Начинаем путешествие!']) + '\n'
            state = 20

        elif 'нет' in list_of_request or 'выход' in list_of_request or 'не' in list_of_request:
            state = 100

### История праздника
    if state == 20 and stories:
        story = stories[0] # запоминаем первый рассказ
        stories.pop(0)

        message += story # воспроизведение истории
        buttons = [button('Вперёд!'), button('Завершить путешествие')]
        state = 25

    elif state == 25:

        ### перепрыгивание на следующее
        if 'следующее' in list_of_request or 'дальше' in list_of_request or 'вперёд' in list_of_request:
            state = 30
        ### повтор рассказа
        elif 'назад' in list_of_request or 'повтори' in list_of_request or 'ещё' in list_of_request:
            state = 20
        ### завершение путешествия
        elif 'завершить' in list_of_request or 'заверши'in list_of_request:
            state = 80

### Символ года

    if state == 30 and stories:
        story = stories[0] # запоминаем следующий рассказ
        message += story # воспроизведение истории
        stories.pop(0)

        buttons = [button('Вперёд!'), button('Завершить путешествие')]
        state = 35 

    elif state == 35:
        ### перепрыгивание на следующее
        if 'следующее' in list_of_request or 'дальше' in list_of_request or 'вперёд' in list_of_request:
            state = 40
        ### повтор рассказа
        elif 'назад' in list_of_request or 'повтори' in list_of_request or 'ещё раз' in list_of_request:
            state = 30
        ### завершение путешествия
        elif 'завершить' in list_of_request or 'заверши'in list_of_request:
            state = 80

### Новый год в разных странах

    if state == 40 and stories:
        story = stories[0] 
        stories.pop(0) 
        message += story 

        buttons = [button('Вперёд!'), button('Завершить путешествие')]
        state = 45

    elif state == 45:
        ### перепрыгивание на следующее
        if 'следующее' in list_of_request or 'дальше' in list_of_request or 'вперёд' in list_of_request:
            state = 50
        ### повтор рассказа
        elif 'назад' in list_of_request or 'повтори' in list_of_request or 'ещё раз' in list_of_request:
            state = 40
        ### завершение путешествия
        elif 'завершить' in list_of_request or 'заверши'in list_of_request:
            state = 80

### Как строить снеговика

    if state == 50 and stories:
        story = stories[0] 
        stories.pop(0) 
        message += story + '\n'
        # Пегвый шаг
        story = stories[0] 
        stories.pop(0) 
        message += story 
        # Второй шаг
        story = stories[0] 
        stories.pop(0) 
        message += story 
        # Третий шаг
        story = stories[0] 
        stories.pop(0) 
        message += story 
        # Четвёртый шаг
        story = stories[0] 
        stories.pop(0) 
        message += story 

        buttons = [button('Вперёд!'), button('Завершить путешествие')]
        state = 55

    elif state == 55:
        ### перепрыгивание на следующее
        if 'следующее' in list_of_request or 'дальше' in list_of_request or 'вперёд' in list_of_request:
            state = 80
        ### повтор рассказа
        elif 'назад' in list_of_request or 'повтори' in list_of_request or 'ещё раз' in list_of_request:
            state = 50
        ### завершение путешествия
        elif 'завершить' in list_of_request or 'заверши'in list_of_request:
            state = 80

### Конец

    if state == 80:
        message = 'Наше путешествие в мир праздника подошло к концу. Хотите загадать желание вместе со мной?'
        buttons = [button('Да!'), button('Не сейчас')]
        state = 90
    
    elif state == 90:

        if 'да' in list_of_request or 'давай' in list_of_request:
            message = 'Отлично, тогда приготовьте бумажку и ручку! Можете позвать своих друзей или родных. \n Всё, что вам нужно - это написать желания и цели на следующий год. По окончанию соберите ваши желания и запечатайте в конверт до следующего года!'
            buttons = [button('Готово!'), button('Не сейчас')]
            state = 95
    
        elif 'не' in list_of_request or 'нет' in list_of_request or 'завершить' in list_of_request:
            state = 100

    if state == 95:
        if 'готово' in list_of_request or 'сделал' in list_of_request or 'загадал' in list_of_request or 'не' in list_of_request:
            state = 100


                

### Прощание
    if state == 100:
        message = choice(['До новых встреч!', "Пока!", "Рада была встрече!"]) + "\n Проведите день чудесно!"
        end_session = True

### Обработка ответов
    response_message = {
        "response": 
        {
            "text": message,
            "tts": message,
            "buttons": buttons,
            "end_session": end_session
        },
        "session": 
        {
            derived_key: session[derived_key] for derived_key 
            in ['session_id', 'user_id', 'message_id']
        },
            "version": version
    }
    return response_message

### кнопка

def button(title):
    return {"title": title}

async def webhook(request_obj):
    request_message = await request_obj.json()
    response = handler_function(request_message)

    return web.json_response(response)

def init():
    app = web.Application() # создаём приложение и кладём в новую переменную
    app.router.add_post("/webhook", webhook)
    web.run_app(app, host = HOST_IP, port =  HOST_PORT)

if __name__ == "__main__":
    init()
