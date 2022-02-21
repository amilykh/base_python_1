# task_9_3.py
# Задание 3
# Реализовать базовый класс Worker (работник):
#
# - определить атрибуты: name, surname, position (должность), income (доход);
#
# - последний атрибут должен быть защищённым и ссылаться на словарь,
#   содержащий элементы «оклад» и «премия», например,
#   {"wage": wage, "bonus": bonus};
#
# - создать класс Position (должность) на базе класса Worker;
#
# - в классе Position реализовать методы получения полного имени
#   сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
#
# - проверить работу примера на реальных данных: создать экземпляры класса
#   Position, передать данные, проверить значения атрибутов, вызвать
#   методы экземпляров.
#
class Worker:

    def __init__(self, name: str, surname: str, position: str, income: dict):
        self.__name = name
        self.__surname = surname
        self.__position = position
        self._income = income

    def get_name(self) -> str:
        return self.__name

    def get_surname(self) -> str:
        return self.__surname

    def get_position(self) -> str:
        return self.__position

    def get_income(self) -> dict:
        return self._income


class Position(Worker):

    def get_full_name(self) -> str:
        """Возвращает строку по формату 'Имя Фамилия'"""
        return f"{self.get_name().capitalize()} {self.get_surname().capitalize()}"

    def get_total_income(self) -> int:
        """Возвращает суммарный ежемесячных доход"""
        _summa = 0
        for _value in self.get_income().values():
            _summa += _value
        return _summa


if __name__ == '__main__':
    welder = Position('иван', 'васильев', 'сварщик',
                      {'wage': 50000, 'bonus': 15000})
    driver = Position('петр', 'николаев', 'водитель',
                      {'wage': 30000, 'bonus': 7500})
    scientist = Position('геннадий', 'разумов', 'ученый',
                         {'wage': 150000, 'bonus': 25000})
    print(welder.get_full_name(), welder.get_total_income())  # Иван Васильев 65000
    print(driver.get_full_name(), driver.get_total_income())  # Петр Николаев 37500
    print(scientist.get_full_name(), scientist.get_total_income())  # Геннадий Разумов
    