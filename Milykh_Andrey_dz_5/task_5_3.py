# Задание 3
# Есть два списка:
#
# tutors = [
#     'Иван', 'Анастасия', 'Петр', 'Сергей', 
#     'Дмитрий', 'Борис', 'Елена'
# ]
# klasses = [
#     '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
# ]
# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
#
# ('Иван', '9А')
# ('Анастасия', '7В')
# ...
#
# Количество генерируемых кортежей не должно быть больше tutors.
# Если в klassesсписке меньше элементов, чем в списке tutors, необходимо
# вывести последние кортежи в виде: (<tutor>, None), например:
#
# ('Станислав', None)
#
# Доказать, что вы имеете дело именно с генератором. Проверка его работы
# до полного обнаружения. Подумай, в каких случаях генератор даст эффект.
#
# ВНИМАНИЕ! используйте стартовый код для своей реализации:

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Станислав']
# klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
klasses = ['9А', '7В', '9Б', '9В', '8Б']


def check_gen(tutors_list: list, klasses_list: list):
    for num in range(0, len(tutors)):
        _tutors, _klasses = tutors_list, klasses_list
        _len_tutors, _len_klasses = len(_tutors), len(_klasses)
        if len(_tutors) > len(_klasses):
            for _i in range(0, (len(_tutors) - len(_klasses))):
                _klasses.append(None)    
        yield _tutors[num], _klasses[num]
    

generator = check_gen(tutors, klasses)
# добавьте здесь доказательство, что создали именно генератор
print(type(generator))
for _ in range(len(tutors)):
    print(next(generator))
# next(generator)  # если раскомментировать, то должно падать в traceback по StopIteration
