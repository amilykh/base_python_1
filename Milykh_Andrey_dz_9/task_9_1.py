# task_9_1.py
# Задание 1
# Создать класс TrafficLight (светофор):
#
# - определить у него один атрибут color (цвет) и метод running (запуск);
# - атрибут реализовать как приватный;
# - в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
# - продолжительность первого состояния (red) составляет 4 секунды, второго (yellow) — 2 секунды,
#   третьего (green) — 3 секунды;
# - переключение между режимами должно осуществляться только в указанном порядке (красный,
#   жёлтый, зелёный) и в stdout каждый цвет должен принтоваться ТОЛЬКО ОДИН раз в момент
#   переключения с указанием исходного кол-ва секунд, т.е. формат строки вывода
#   <текущий цвет> <значение секунд> сек;
# - проверить работу примера, создав экземпляр и вызвав описанный метод.
# Пример, stdout при обращении к методу running:
#
# $ traffic = TrafficLight()
# $ traffic.running()
# red 4 сек
# yellow 2 сек
# green 3 сек
#
import time


class TrafficLight:
    __color: str

    def running(self):
        colors = {'red': 4, 'yellow': 2, 'green': 3}
        for key, values in colors.items():
            __color = key
            lighting = values
            print(f'{__color} {lighting} сек')
            while lighting:
                time.sleep(1)
                lighting -= 1


if __name__ == '__main__':
    traffic = TrafficLight()
    traffic.running()
    