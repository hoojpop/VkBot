'''
[!] Большая благодарность - nomnoms12 [!]

Автор: hoojpop

Все вопросы писать на почту = capturebot@inbox.ru

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

v1.2.1 - 08.07.19
- Вот и настало это обновление, но есть и пару не до счётов. Так ещё и не была добавлена команда: !бан.

Но есть и хорошие новости. Добавил несколько команд. !пуш, теперь можно созвать всех участников вашей беседы.

!пуш [Причина]

Также добавил команду: !сервер, где указывается на каком сервере Вы играете, в какой банде, а также IP.

Добавил команду: !вики, можно узнать какую либо информацию прямиком из ВК.

!вики [Запрос]

Команда: !чат, покажет информацию о беседе. Название, количество участников, количество написанных сообщений, настройки беседы (тоесть, можно ли приглашать людей в беседу, можно ли менять название, закреплять сообщение и т.д)

!имя - Генерирует рандомный РП ник, словарь со временем будет пополняться, но в будущем хочу парсить с сайта, чтобы было легче.

!аноним - Отправить анонимное сообщение.

!покинуть [Причина] - Покинуть беседу с определённой причиной.

'''

from vk_api import VkApi
from vk_api.bot_longpoll import *
from threading import Timer
from datetime import datetime
from datetime import timedelta
from random import *
import time
import sys

# =========================================================================================

print('... Запуск бота')
time.sleep(1)

__author__ = "hoojpop"

# Переменные

now = time.localtime()
peer_id_ = 2000000001

gang = 'Ballas'
ip = '185.169.134.91:7777'
server = 'Evolve 03'

error01 = '- &#128559; Упс, что-то видимо не так.\n\n' \
          '1. Попробуйте выдать боту права администратора.\n' \
          '2. Проверьте правильно ли Вы ввели ID пользователя.'

error02 = '- &#128683; Вам недоступна данная команда.'

error03 = '- &#128533; Я не могу изменить название беседы.\n\n' \
          '1. Попробуйте выдать боту права администратора.'

error04 = '- &#9881; Команда в разработке.'

join_text = '- &#128524; Спасибо, что подписался на группу. Вся информамация на странице группы.'
leave_text = '- &#128543; Ну, куда же ты? Надеюсь ты ещё вернёшься.'

anonim = ['&#129313;', '&#128125;', '&#128124;', '&#128520;', '&#128127;', '&#128121;', '&#128123;', '&#128126;', '&#128128;', '&#128122;', '&#128019;']

NameRp = ['Aaron','Abraham','Adam','Adrian','Aidan','Alan','Albert','Alejandro','Alex','Alexander','Alfred','Andrew','Angel','Anthony','Antonio','Ashton','Austin', 'Benjamin','Bernard','Blake','Brandon','Brian','Bruce','Bryan	Bailey','Barbara','Beatrice','Belinda','Brianna','Bridjet','Brooke', 'Cameron','Carl','Carlos','Charles','Christopher','Cole','Connor','Caleb','Carter','Chase','Christian','Clifford','Cody','Colin','Curtis','Cyrus	Caroline','Catherine','Cecilia','Celia','Chloe','Christine','Claire', 'Daniel','David','Dennis','Devin','Diego','Dominic','Donald','Douglas','Dylan	Daisy','Danielle','Deborah','Delia','Destiny','Diana','Dorothy', 'Edward','Elijah','Eric','Ethan','Evan	Eleanor','Elizabeth','Ella','Emily','Emma','Erin','Evelyn'
              'Francis','Fred', 'Faith','Fiona','Florence','Freda', 'Gabriel','Gavin','Geoffrey','George','Gerld','Gilbert','Gordon','Graham','Gregory	Gloria','Gabriella','Gabrielle','Gladys','Grace', 'Harold','Harry','Hayden','Henry','Herbert','Horace','Howard','Hugh','Hunter	Hailey','Haley','Hannah','Helen', 'Jack','Jackson','Jacob','Jaden','Jake','James','Jason','Jayden','Jeffery','Jeremiah','Jesse','Jesus','John','Jonathan','Jordan','Jose','Joseph','Joshua','Juan','Julian','Justin	Jacqueline','Jada','Jane','Jasmine','Jenna','Jennifer','Jessica','Jocelyn','Jordan','Josephine','Joyce','Julia','Keith','Kevin','Kyle','Kaitlyn','Katelyn','Katherine','Kathryn','Kayla','Kaylee','Kimberly','Kylie', 'Landon','Lawrence','Leonars','Lewis','Logan','Louis','Lucas','Luke	Laura','Lauren','Leah','Leonora','Leslie','Lillian','Lily','Linda','Lorna','Luccile','Lucy','Lynn'
            , 'Malcolm','Martin','Mason','Matthew','Michael','Miguel','Miles','Morgan	Mabel','Mackenzie','Madeline','Madison','Makayla','Margaret','Maria','Marisa','Marjorie','Mary','Maya','Megan','Melanie','Melissa','Mia','Michelle','Mildred','Molly','Monica', 'Nathan','Nathaniel','Neil','Nicholas','Noah','Norman	Nancy','Natalie','Nicole','Nora', 'Oliver','Oscar','Oswald','Owe']


# admins

moder = [0]
admin = [IDs пользователей, которых хотите добавить в админы, через запятую]

softFps = '\n/ CLEO:\n\n• n1_Memory_Cleaner.cs:\n' \
          '   \a- Выделяет память для игры, комадной /cmem. Оптимальное значение 400' \
          '\n\n• fog.cs:\n' \
          '   \a- Изменение дальности прорисовки в игре. Команда: /fog [Дистанция]' \
          '\n\n• FPSUnlock.cs:\n' \
          '   \a- Снимает ограничение FPS' \
          '\n\n• FPSupACH.cs:\n' \
          '   \a- Убирает полностью игроков из вашей фракции по клисту. Комадна: /ach, деактивация точно такая же.' \
          '\n\n• gamefixer.cs:\n' \
          '   \a- Дополнительные функции для поднятия FPS. Команда: /ghelp' \
          '\n\n• rivafpscontrol.cs:\n' \
          '   \a- Самонастройка FPS. Команда: /fpshelp.' \
          '\n\n• boostfps.cs, memory_full.cs, memory512.cs, memory2048.cs:\n' \
          '   \a- Выделение памяти для игры.\n' \
          '\n/ ASI:' \
          '\n\n• FPSBOOST.asi, FPSBOOST.ini, FPSBOOST.exe:\n' \
          '   \a- Перед игрой запускать "FPSBOOST.exe"' \
          '\n\n• FPSUnlockRXByDarkP1xel.ASI:\n' \
          '   \a- Отключение ограничения FPS.' \
          '\n\n• NoShadows.asi:\n' \
          '   \a- Удаление теней из игры.' \
          '\n\n• SilentPatchSA.asi, SilentPatchSA.ini:\n' \
          '   \a- Один из лучших модов для GTA в мире.Цель мода - избавиться от исходных ошибок игры, чего Rockstar не сделал.' \
          '\n\n• skygrad.asi:\n' \
          '   \a- Небольшой плагин, применяющий эффект сглаживания к градиенту неба, тем самым исправляющий неприятные цветовые линии на небе.\n'

softUseful = 'Текст'

# Авторизация

print('... Авторизация')

vk_session = VkApi(token='#[ВАШ ТОКЕН ГРУППЫ]#')
longpoll = VkBotLongPoll(vk_session, '#[ВАШ ID ГРУППЫ]#')
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

def wikiFind():

    import wikipedia

    wikipedia.set_lang("RU")

    try:
        page = wikipedia.page("Recommendation")
    except wikipedia.exceptions.DisambiguationError as e:
        print (e.options)

    write_msg(vk, chat_id, 'Идёт поиск..')

    try:

        write_msg(vk, chat_id, '&#127760; Результат: \n\n| ' + str(wikipedia.summary(request[5:])))
    except:

        write_msg(vk, chat_id, '- &#128530; Что-то пошло не так.\n\n'
                               '1. Попробуйте точно указать запрос.\n'
                               '2. Повторите попытку.')

def callAll():

    peer_id = event.obj.get('peer_id')

    chat = vk.messages.getConversationMembers(peer_id=peer_id)

    mess = '&#128233; Все пользователи беседы созваны. \n Причина: ' + request[4:] + '\n\n'

    for user in chat['profiles']:

        cloud = '@id' + str(user['id']) + '(💬)'
        mess += cloud

    vk.messages.send(
        chat_id=chat_id,
        message=mess,
    )

def randomNameRp():

    import random

    nameRp = random.choice(NameRp)
    nameRp0 = random.choice(NameRp)

    write_msg(vk, chat_id, '- &#9881; Генерация имени..')
    time.sleep(1)
    write_msg(vk, chat_id, '- Рандомный РП ник: ' + nameRp + '_' + nameRp0)

def anonimSend():

    import random

    smileAnonim = random.choice(anonim)

    write_msg(vk, chat_id, '- ' + smileAnonim + ' Аноним: ' + request[8:])

def getChat(vk, chat_id):

    peer_id = event.obj.get('peer_id')

    chat = vk.messages.getConversationsById(peer_ids=peer_id)
    CountMsg = event.obj.get('conversation_message_id')

    rulesChat = chat["items"][0]["chat_settings"]["acl"]
    nameChat = chat['items'][0]['chat_settings']['title']
    membersCount = chat['items'][0]['chat_settings']['members_count']
    msgCount = CountMsg

    vk.messages.send(
        chat_id=chat_id,
        message='&#128196; | Информация о беседе: \n' + '\n&#9999; | Название: ' + str(nameChat) + '\n&#128101; | Количество участников беседы: ' + str(membersCount) + '\n&#9881; | Настройки беседы: ' + 'В разработке' + '\n&#9993; | Количество написанных сообщений: ' + str(msgCount))


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

    vkSession = VkApi(token=#[ВАШ ТОКЕН ГРУППЫ]#)
    vk = vkSession.get_api()

    event = longpoll.listen()

    chat_id_ = # Ваш ID беседы

    # ========================================================================================================

    delta = get_delta(10, 0)
    t = CustomTimer(vk, chat_id_, '- Проснулся? Ну доброе утро &#128578;', delta=delta, interval=86400)
    t.start()

    delta = get_delta(23, 50)
    t = CustomTimer(vk, chat_id_, '- Всем спокойной ночи, а самым смелым, удачных каптов &#128521;', delta = delta, interval = 86400)
    t.start()

    # ========================================================================================================

    delta = get_delta(0, 30)
    t = CustomTimer(vk, chat_id_, '- Держу в курсе, до капта осталось 30 минут', delta=delta, interval=86400)
    t.start()

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

    # ========================================================================================================

    delta = get_delta(2, 30)
    t = CustomTimer(vk, chat_id_, '- Держу в курсе, до капта осталось 30 минут', delta=delta, interval=86400)
    t.start()

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

    # ========================================================================================================

    delta = get_delta(4, 30)
    t = CustomTimer(vk, chat_id_, '- Держу в курсе, до капта осталось 30 минут', delta=delta, interval=86400)
    t.start()

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

    # ========================================================================================================

    delta = get_delta(6, 30)
    t = CustomTimer(vk, chat_id_, '- Держу в курсе, до капта осталось 30 минут', delta=delta, interval=86400)
    t.start()

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

    # ========================================================================================================

    delta = get_delta(8, 30)
    t = CustomTimer(vk, chat_id_, '- Держу в курсе, до капта осталось 30 минут', delta=delta, interval=86400)
    t.start()

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

    # ========================================================================================================

    delta = get_delta(10, 30)
    t = CustomTimer(vk, chat_id_, '- Держу в курсе, до капта осталось 30 минут', delta=delta, interval=86400)
    t.start()

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

    # ========================================================================================================

    delta = get_delta(12, 30)
    t = CustomTimer(vk, chat_id_, '- Держу в курсе, до капта осталось 30 минут', delta=delta, interval=86400)
    t.start()

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

    # ========================================================================================================

    delta = get_delta(14, 30)
    t = CustomTimer(vk, chat_id_, '- Держу в курсе, до капта осталось 30 минут', delta=delta, interval=86400)
    t.start()

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

    # ========================================================================================================

    delta = get_delta(16, 30)
    t = CustomTimer(vk, chat_id_, '- Держу в курсе, до капта осталось 30 минут', delta=delta, interval=86400)
    t.start()

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


    # ========================================================================================================

    delta = get_delta(18, 30)
    t = CustomTimer(vk, chat_id_, '- Держу в курсе, до капта осталось 30 минут', delta=delta, interval=86400)
    t.start()

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

    # ========================================================================================================

    delta = get_delta(20, 30)
    t = CustomTimer(vk, chat_id_, '- Держу в курсе, до капта осталось 30 минут', delta=delta, interval=86400)
    t.start()

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

    # ========================================================================================================

    delta = get_delta(22, 30)
    t = CustomTimer(vk, chat_id_, '- Держу в курсе, до капта осталось 30 минут', delta=delta, interval=86400)
    t.start()

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

# ======================================================================================================================

# === MAIN === #

for event in longpoll.listen():

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
                write_msg(vk, chat_id, error03)

            if request[0:2] == "@ " and not user_id in admin:

                write_msg(vk, chat_id, error02)

        if request == "!софт":

            write_msg(vk, chat_id, '- &#128194; FPS UPs: https://vk.cc/9wk47y' + '\n\n============================'+ softFps + '\n - &#128194; Полезное: https://vk.cc/9wkaQg' + '\n============================'+ softUseful)

        if request[0:5] == "!кик " and user_id in admin:

            try:
                vk.messages.removeChatUser(chat_id=chat_id, user_id=request[5:])
            except:
                write_msg(vk, chat_id, error01)

        if request[0:5] == "!кик " and not user_id in admin:

            write_msg(vk, chat_id, error02)

        if request == '!чат' and user_id in admin:

            getChat(vk, chat_id)

        if request[0:5] == "!бан " and user_id in admin:

             write_msg(vk, chat_id, error04)

        if request[0:4] == "!пуш":

            callAll()

        if request[0:5] == "!вики":

            wikiFind()

        if request[0:8] == "!аноним ":

            anonimSend()

        if request == "!имя":

            randomNameRp()
            
        if request[0:10] == "!покинуть ":

            user_id = event.object.get('from_id')

            write_msg(vk, chat_id, '- &#128173; @id' + str(user_id) + '(Пользователь) покинул беседу. \n\n'
                                                                 'Причина: ' + request[
                                                                               10:] + '\n\n- У вас есть время с ним попрощаться.')
            time.sleep(5)

            try:
                vk.messages.removeChatUser(chat_id=chat_id, user_id=user_id)
            except:
                write_msg(vk, chat_id, '- Я не могу тебя исключить из беседы.\n\n'
                                       '1. Попробуйте выдать боту права администратора.')
                
# ======================================================================================================================

# Проверка на подписки и отписки для сообщества / Проверка на вступление и выход из беседы

    if event.type == VkBotEventType.GROUP_JOIN:

        user_id = event.obj.user_id

        vk.messages.send(

            user_id=user_id,
            message=join_text

        )

    if event.type == VkBotEventType.GROUP_LEAVE:

        user_id = event.obj.user_id

        vk.messages.send(

            user_id=user_id,
            message=leave_text
        )

# ======================================================================================================================

# Логи для консоли.

    if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat:

        chat_id = event.chat_id
        user_id = event.obj.from_id
        firstName = vk.users.get(user_id=user_id)[0]['first_name']
        lastName = vk.users.get(user_id=user_id)[0]['last_name']
        chat = vk.messages.getConversationsById(peer_ids=peer_id)
        nameChat = chat['items'][0]['chat_settings']['title']
        text = event.obj.get('text')
        Event = event.type

        print('')
        print('========================================')
        print('Беседа / Название: №' + str(chat_id) + ' / ' + str(nameChat))
        print('Имя: ' + str(firstName))
        print('Фамилия: ' + str(lastName))
        print('ID: ' + str(user_id))
        print('Сообщение: ' + str(text))
        print('========================================')
