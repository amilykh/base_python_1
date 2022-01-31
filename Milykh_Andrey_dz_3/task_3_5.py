# Задание 5
# '''
# Реализовать функцию get_jokes(), возвращающую n шуток,
# сформированных из трех случайных слов, взятых из трёх
# списков (по одному из каждого):
#
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#
# Например:

# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]

# Документировать код функции.
#
# * Сможете ли вы добавить еще один аргумент — флаг,
#   разрешающий или запрещающий повторы слов в шутках
#   (когда каждое слово можно использовать только
#   в одной шутке)?
#
# * Сможете ли вы сделать аргументы именованными?
# '''
from random import choice


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(count: int) -> list:
    """Возвращает список шуток в количестве count"""
    # пишите реализацию своей программы здесь
    _list_out = []
    for i in range(count):
        _list_out.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')

    return _list_out


print(get_jokes(2))
print(get_jokes(10))


# Раскомментируйте для реализации подзаданий:
# документирование, флаг и именованные аргументы
def get_jokes_adv(count: int, repetition: bool = False) -> list:
    """
    Возвращает список шуток в количестве count

    :param count:  количество шуток
    :param repetition:  флаг, разрешающий или запрещающий
            повторы слов в шутках  (когда каждое слово можно
            использовать только в одной шутке)
            Если повторы запрещены ( repetition == False),
            количество шуток не может быть больше 5.
    :return:  список шуток
    """
    # пишите реализацию здесь
    _list_out = []
    _count = count

    if repetition is True:
        _count = len(nouns)

    for i in range(_count):
        if repetition is True:
            _words = []
            # work with nouns
            _word = choice(nouns)
            _words.append(_word)
            nouns.remove(_word)
            # work with adverbs
            _word = choice(adverbs)
            _words.append(_word)
            adverbs.remove(_word)
            # work with adjectives
            _word = choice(adjectives)
            _words.append(_word)
            adjectives.remove(_word)
            _joke_str = " ".join(_words)
            _list_out.append(_joke_str)
        else:
            _list_out.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')

    return _list_out


print(get_jokes_adv(2))
print(get_jokes_adv(10, True))
