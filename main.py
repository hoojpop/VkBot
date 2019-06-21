'''
[!] Большая благодарность - nomnoms12, gil9red [!]

Автор: hoojpop

Все вопросы писать на почту = stepan2x2@mail.ru

v1.0 - Rls:

v1.1 - 16.06.19:
- Бот начал уведомлять о "каптах" каждые два часа, начиная с 1:00 до 23:00.
- Бот начал изменять чат, текст пока можно будет поменять в коде, но со временем добавлю команду. Которая, запомнит ваше название и к названию будет добавлять время, когда следующий "капт": 1:00 / "НАЗВАНИЕ".
- Маленькая фича, бот уведомляет, когда начинатеся утро и ночь.

v1.2 - 21.06.19
- Теперь бот может изменять название вашей беседы, одной командой. @ Название. Для этого нужно выдать администратора боту.
- Вам кто-то надоел? Кто-то нарушил правила в вашей беседе? Командой !кик и указав ID пользователя, вы сможете исключить его из вашей беседы. !кик 99999999. Также для бота нужно выдать администратора.

- Прочее команды для самой игры. Командой !софт, бот вышлет ссылку на софт для FPS и Полезные для игры.
- Также есть команда !моды, но пока что ничего нету.

- Убран модуль Samp, так как он плохо работает, я полностью от него отказался.

'''

from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from threading import Timer
from datetime import datetime
from datetime import timedelta
from random import random
import time
import json

# =========================================================================================

print('... Запуск бота')
time.sleep(1)

__author__ = "hoojpop"

# Переменные

now = time.localtime()
peer_id_ = 2000000000 

'''
:peer_id_
Математика. 2000000000 + id беседы. Id беседы можно узнать в ссылке передя в саму беседу. 
https://vk.com/im?sel= ( c1 ) <-- Это id беседы.
'''

gang = 'Rifa'
ip = '185.169.134.68:7777'
server = 'Evolve 02'

# admins

moder = [0]
admin = [id's людей, кого хотите поместить в админов]

# Авторизация

print('... Авторизация')

vk_session = VkApi(token='[ ! Ваш токен ! ]')
longpoll = VkBotLongPoll(vk_session, '[ ! ID вашей группы ! ]')
vk = vk_session.get_api()

print('... Бот авторизован')


# def's

def write_msg(vk, chat_id, message):

    random_id = round(random() * 10 ** 9)

    vk.messages.send(
        random_id=random_id,
        chat_id=chat_id,
        message=message,
    )

def send_msg(vk, user_id, message):

    random_id = round(random() * 10 ** 9)

    vk.messages.send(
        random_id=random_id,
        user_id=user_id,
        message=message,
    )

def editChat_(vk, chat_id, title):

    vk.messages.editChat(chat_id=chat_id, title=title)


def get_delta(hour=0, minute=0, second=0, microsecond=0):
    now = datetime.now()
    run_at = now.replace(hour=hour, minute=minute, second=second, microsecond=microsecond)
    if run_at < now:
        run_at += timedelta(days=1)

    return (run_at - now).total_seconds()


class CustomTimer:
    def __init__(self, *args, delta=0.0, function=write_msg, interval=86400.0, **kwargs):
        self.delta = delta
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs

        self.timer = None

    def callback(self):
        self.function(*self.args, **self.kwargs)
        self.normal_start()

    def normal_start(self):
        self.timer = Timer(self.interval, self.callback)
        self.timer.start()

    def start(self):
        self.timer = Timer(self.delta, self.callback)
        self.timer.start()

class EditChat:
    def __init__(self, *args, delta=0.0, function=editChat_, interval=86400.0, **kwargs):
        self.delta = delta
        self.interval = interval
        self.function = function
        self.args = args
        self.kwargs = kwargs

        self.timer = None

    def callback(self):
        self.function(*self.args, **self.kwargs)
        self.normal_start()

    def normal_start(self):
        self.timer = Timer(self.interval, self.callback)
        self.timer.start()

    def start(self):
        self.timer = Timer(self.delta, self.callback)
        self.timer.start()

if __name__ == '__main__':

    vkSession = VkApi(token='[ ! Ваш токен ! ]')
    vk = vkSession.get_api()

    chat_id_ = [ ! ID вашей беседы ! ]

    # ========================================================================================================

    delta = get_delta(10, 0)
    t = CustomTimer(vk, chat_id_, '- Проснулся? Ну доброе утро &#128578;', delta=delta, interval=86400)
    t.start()

    delta = get_delta(23, 50)
    t = CustomTimer(vk, chat_id_, '- Всем спокойной ночи, а самым смелым, удачных каптов &#128521;', delta = delta, interval = 86400)
    t.start()

    # ========================================================================================================

    delta = get_delta(0, 45)
    t = CustomTimer(vk, chat_id_, '- До капта осталось 15 минут, все заходим!', delta=delta, interval=86400)
    t.start()

    delta = get_delta(0, 50)
    t = CustomTimer(vk, chat_id_, '- До капта осталось 10 минут!', delta=delta, interval=86400)
    t.start()

    delta = get_delta(1, 0)
    t = CustomTimer(vk, chat_id_, '- Капт начался, заходим!', delta=delta, interval=86400)
    t.start()

    delta = get_delta(1, 20)
    t = CustomTimer(vk, chat_id_, '- Капт закончился, следующий капт в 3:00', delta=delta, interval=86400)
    t.start()
    delta = get_delta(1, 20)
    c = EditChat(vk, chat_id_, '[ ! ВАШ ТЕКСТ ! ]', delta=delta, interval=86400)
    c.start()


    # ========================================================================================================

    delta = get_delta(2, 45)
    t = CustomTimer(vk, chat_id_, '- До капта осталось 15 минут, все заходим!', delta=delta, interval=86400)
    t.start()
    
    delta = get_delta(2, 50)
    t = CustomTimer(vk, chat_id_, '- До капта осталось 10 минут!', delta=delta, interval=86400)
    t.start()

    delta = get_delta(2, 0)
    t = CustomTimer(vk, chat_id_, '- Капт начался, заходим!', delta=delta, interval=86400)
    t.start()

    delta = get_delta(3, 20)
    t = CustomTimer(vk, chat_id_, '- Капт закончился, следующий капт в 5:00, после рестарта.', delta=delta, interval=86400)
    t.start()
    delta = get_delta(3, 20)
    c = EditChat(vk, chat_id_, '[ ! ВАШ ТЕКСТ ! ]', delta=delta, interval=86400)
    c.start()

    # ========================================================================================================

    delta = get_delta(4, 45)
    t = CustomTimer(vk, chat_id_, '- До капта осталось 15 минут, все заходим!', delta=delta, interval=86400)
    t.start()

    delta = get_delta(4, 50)
    t = CustomTimer(vk, chat_id_, '- До капта осталось 10 минут, готовимся!', delta=delta, interval=86400)
    t.start()

    delta = get_delta(5, 0)
    t = CustomTimer(vk, chat_id_, '- Капт начался, удачи!', delta=delta, interval=86400)
    t.start()

    delta = get_delta(5, 20)
    t = CustomTimer(vk, chat_id_, '- Капт закончился, следующий капт в 7:00', delta=delta, interval=86400)
    t.start()
    delta = get_delta(5, 20)
    c = EditChat(vk, chat_id_, '[ ! ВАШ ТЕКСТ ! ]', delta=delta, interval=86400)
    c.start()

    # ========================================================================================================

    delta = get_delta(6, 45)
    t = CustomTimer(vk, chat_id_, '- До капта осталось 15 минут, все заходим!', delta=delta, interval=86400)
    t.start()

    delta = get_delta(6, 50)
    t = CustomTimer(vk, chat_id_, '- До капта осталось 10 минут, готовимся!', delta=delta, interval=86400)
    t.start()

    delta = get_delta(7, 0)
    t = CustomTimer(vk, chat_id_, '- Капт начался, удачи!', delta=delta, interval=86400)
    t.start()

    delta = get_delta(7, 20)
    t = CustomTimer(vk, chat_id_, '- Капт закончился, следующий капт в 9:00', delta=delta, interval=86400)
    t.start()
    delta = get_delta(7, 20)
    c = EditChat(vk, chat_id_, '[ ! ВАШ ТЕКСТ ! ]', delta=delta, interval=86400)
    c.start()

    # ========================================================================================================

    delta = get_delta(8, 45)
    t = CustomTimer(vk, chat_id_, '- До капта осталось 15 минут, все заходим!', delta=delta, interval=86400)
    t.start()

    delta = get_delta(8, 50)
    t = CustomTimer(vk, chat_id_, '- До капта осталось 10 минут, готовимся!', delta=delta, interval=86400)
    t.start()

    delta = get_delta(9, 0)
    t = CustomTimer(vk, chat_id_, '- Капт начался, удачи!', delta=delta, interval=86400)
    t.start()

    delta = get_delta(9, 20)
    t = CustomTimer(vk, chat_id_, '- Капт закончился, следующий капт в 11:00', delta=delta, interval=86400)
    t.start()
    delta = get_delta(9, 20)
    c = EditChat(vk, chat_id_, '[ ! ВАШ ТЕКСТ ! ]', delta=delta, interval=86400)
    c.start()

    # ========================================================================================================

    delta = get_delta(10, 45)
    t = CustomTimer(vk, chat_id_, '- До капта осталось 15 минут, все заходим!', delta=delta, interval=86400)
    t.start()

    delta = get_delta(10, 50)
    t = CustomTimer(vk, chat_id_, '- До капта осталось 10 минут, готовимся!', delta=delta, interval=86400)
    t.start()

    delta = get_delta(11, 0)
    t = CustomTimer(vk, chat_id_, '- Капт начался, удачи!', delta=delta, interval=86400)
    t.start()

    delta = get_delta(11, 20)
    t = CustomTimer(vk, chat_id_, '- Капт закончился, следующий капт в 13:00', delta=delta, interval=86400)
    t.start()
    delta = get_delta(11, 20)
    c = EditChat(vk, chat_id_, '[ ! ВАШ ТЕКСТ ! ]', delta=delta, interval=86400)
    c.start()

    # ========================================================================================================

    delta = get_delta(12, 45)
    t = CustomTimer(vk, chat_id_, '- До капта осталось 15 минут, все заходим!', delta=delta, interval=86400)
    t.start()

    delta = get_delta(12, 50)
    t = CustomTimer(vk, chat_id_, '- До капта осталось 10 минут, готовимся!', delta=delta, interval=86400)
    t.start()

    delta = get_delta(13, 0)
    t = CustomTimer(vk, chat_id_, '- Капт начался, удачи!', delta=delta, interval=86400)
    t.start()

    delta = get_delta(13, 20)
    t = CustomTimer(vk, chat_id_, '- Капт закончился, следующий капт в 15:00', delta=delta, interval=86400)
    t.start()
    delta = get_delta(13, 20)
    c = EditChat(vk, chat_id_, '[ ! ВАШ ТЕКСТ ! ]', delta=delta, interval=86400)
    c.start()

    # ========================================================================================================

    delta = get_delta(14, 45)
    t = CustomTimer(vk, chat_id_, '- До капта осталось 15 минут, все заходим!', delta=delta, interval=86400)
    t.start()

    delta = get_delta(14, 50)
    t = CustomTimer(vk, chat_id_, '- До капта осталось 10 минут, готовимся!', delta=delta, interval=86400)
    t.start()

    delta = get_delta(15, 0)
    t = CustomTimer(vk, chat_id_, '- Капт начался, удачи!', delta=delta, interval=86400)
    t.start()

    delta = get_delta(15, 20)
    t = CustomTimer(vk, chat_id_, '- Капт закончился, следующий капт в 17:00', delta=delta, interval=86400)
    t.start()
    delta = get_delta(15, 20)
    c = EditChat(vk, chat_id_, '[ ! ВАШ ТЕКСТ ! ]', delta=delta, interval=86400)
    c.start()

    # ========================================================================================================

    delta = get_delta(16, 45)
    t = CustomTimer(vk, chat_id_, '- До капта осталось 15 минут, все заходим!', delta=delta, interval=86400)
    t.start()

    delta = get_delta(16, 50)
    t = CustomTimer(vk, chat_id_, '- До капта осталось 10 минут, готовимся!', delta=delta, interval=86400)
    t.start()

    delta = get_delta(17, 0)
    t = CustomTimer(vk, chat_id_, '- Капт начался, удачи!', delta=delta, interval=86400)
    t.start()

    delta = get_delta(17, 20)
    t = CustomTimer(vk, chat_id_, '- Капт закончился, следующий капт в 19:00', delta=delta, interval=86400)
    t.start()
    delta = get_delta(17, 20)
    c = EditChat(vk, chat_id_, '[ ! ВАШ ТЕКСТ ! ]', delta=delta, interval=86400)
    c.start()

    # ========================================================================================================

    delta = get_delta(18, 45)
    t = CustomTimer(vk, chat_id_, '- До капта осталось 15 минут, все заходим!', delta=delta, interval=86400)
    t.start()

    delta = get_delta(18, 50)
    t = CustomTimer(vk, chat_id_, '- До капта осталось 10 минут, готовимся!', delta=delta, interval=86400)
    t.start()

    delta = get_delta(19, 0)
    t = CustomTimer(vk, chat_id_, '- Капт начался, удачи!', delta=delta, interval=86400)
    t.start()

    delta = get_delta(19, 20)
    t = CustomTimer(vk, chat_id_, '- Капт закончился, следующий капт в 21:00', delta=delta, interval=86400)
    t.start()
    delta = get_delta(19, 20)
    c = EditChat(vk, chat_id_, '[ ! ВАШ ТЕКСТ ! ]', delta=delta, interval=86400)
    c.start()

    # ========================================================================================================

    delta = get_delta(20, 45)
    t = CustomTimer(vk, chat_id_, '- До капта осталось 15 минут, все заходим!', delta=delta, interval=86400)
    t.start()

    delta = get_delta(20, 50)
    t = CustomTimer(vk, chat_id_, '- До капта осталось 10 минут, готовимся!', delta=delta, interval=86400)
    t.start()

    delta = get_delta(21, 0)
    t = CustomTimer(vk, chat_id_, '- Капт начался, удачи!', delta=delta, interval=86400)
    t.start()

    delta = get_delta(21, 20)
    t = CustomTimer(vk, chat_id_, '- Капт закончился, следующий капт в 23:00', delta=delta, interval=86400)
    t.start()
    delta = get_delta(21, 20)
    c = EditChat(vk, chat_id_, '[ ! ВАШ ТЕКСТ ! ]', delta=delta, interval=86400)
    c.start()

    # ========================================================================================================

    delta = get_delta(22, 45)
    t = CustomTimer(vk, chat_id_, '- До капта осталось 15 минут, все заходим!', delta=delta, interval=86400)
    t.start()

    delta = get_delta(22, 50)
    t = CustomTimer(vk, chat_id_, '- До капта осталось 10 минут, готовимся!', delta=delta, interval=86400)
    t.start()

    delta = get_delta(23, 0)
    t = CustomTimer(vk, chat_id_, '- Капт начался, удачи!', delta=delta, interval=86400)
    t.start()

    delta = get_delta(23, 20)
    t = CustomTimer(vk, chat_id_, '- Капт закончился, следующий капт в 1:00, удачных ночных каптов.', delta=delta, interval=86400)
    t.start()
    delta = get_delta(23, 20)
    c = EditChat(vk, chat_id_, '[ ! ВАШ ТЕКСТ ! ]', delta=delta, interval=86400)
    c.start()

# ========================================================================================================

# === MAIN === #

for event in longpoll.listen():

    print(event)

    if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat:

        request = event.object.get('text')
        user_id = event.object.get('from_id')
        peer_id = event.object.get('peer_id')
        chat_id = event.chat_id

        if request == "!сервер":

            write_msg(vk, chat_id, '- Мы играем на сервере: '+ server + '\n- IP: '+ ip + '\n- Банда: ' + gang)

        if request[0:2] == "@ " and user_id in admin:

            try:
                editChat_(vk, chat_id, request[2:])
            except:
                write_msg(vk, chat_id, '- Я не могу менять название беседы, попробуй выдать мне администратора.')

            if request[0:2] == "@ " and not user_id in admin:

                write_msg(vk, chat_id, '- Вам запрещенно пользоваться данной командой.')

        if request == "!софт":

            write_msg(vk, chat_id, '- FPS UPs: https://vk.cc/9wk47y' + '\n - Полезное: https://vk.cc/9wkaQg')

        if request == "!моды":

            write_msg(vk, chat_id, '- Моды: Чуть позже.')

        if request[0:5] == "!кик " and user_id in admin:

            try:
                vk.messages.removeChatUser(chat_id=chat_id, user_id=request[5:])
            except:
                write_msg(vk, chat_id, '- Шо то не так, попробуй указать правильный ID пользователя.')

        if request == "!кик " and not user_id in admin:

            write_msg(vk, chat_id, '- Вам запрещено пользоваться данной командой')

