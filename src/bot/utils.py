import random
import shelve

import src.bot.settings as conf


def set_user_data(chat_id, data):
    """
    Записываем юзера в игроки и запоминаем, что он должен ответить.
    Либо обновляем информацию.
    """
    with shelve.open(conf.USER_STATE) as storage:
        storage[str(chat_id)] = data


def set_user_state(chat_id, state):
    """
    Указываем позицию хода игрока.
    """
    with shelve.open(conf.USER_STATE) as storage:
        data = storage[str(chat_id)]
        data['state'] = state
        storage[str(chat_id)] = data


def finish_user_game(chat_id):
    """
    Заканчиваем игру текущего пользователя и удаляем правильный ответ из хранилища
    """
    with shelve.open(conf.USER_STATE) as storage:
        del storage[str(chat_id)]


def get_user_data(chat_id):
    """
    Получаем правильный ответ для текущего юзера.
    В случае, если человек просто ввёл какие-то символы, не начав игру, возвращаем None
    """
    with shelve.open(conf.USER_STATE) as storage:
        try:
            return storage[str(chat_id)]
        except KeyError:
            return None


def get_user_state(chat_id):
    with shelve.open(conf.USER_STATE) as storage:
        try:
            return storage[str(chat_id)]['state']
        except KeyError:
            return None


def get_random_word():
    list_words = ['кошка', 'собака']
    return random.choice(list_words)


def convert_question_to_word(question, prefix=None):
    list_words = []
    for model in conf.LIST_MODELS:
        list_words += model.get_words(question, prefix)

    return list_words[0] if list_words else None


# for tests

# def convert_question_to_word(question, prefix=None):
#     return random.choice([question.split()[0], None])

