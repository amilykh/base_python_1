class CustomMessage(Exception):
    _default_message: str = 'пользовательское исключение'

    def __init__(self, message: str = None):
        if message:
            self._default_message = message

    def __str__(self):
        return self._default_message


class CustomZeroDivision(CustomMessage):
    _default_message = 'нельзя делить на ноль!'


class CustomTypeError(CustomMessage):
    _default_message = 'делимое и делитель должны быть числами!'


class CustomItemListError(CustomMessage):
    _default_message = 'элемент списка может быть только числом!'