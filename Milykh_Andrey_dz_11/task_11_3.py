# task_11_3.py
from actions.custom_exceptions import CustomMessage, CustomItemListError


def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


result_lst = []
print("Формируем список, состоящий из чисел...")
while True:
    user_input = input("Введите число или 'stop' для завершения: ")
    if user_input == 'stop':
        break
    try:
        if user_input.isdigit():  # целое число
            result_lst.append(int(user_input))
            continue
        elif user_input[0] == '-' and user_input[1:].isdigit():
            result_lst.append(int(user_input))
            continue
        elif is_float(user_input):  # float число
            result_lst.append(float(user_input))
        else:
            raise CustomItemListError
    except CustomMessage as err:
        print(err)

print(result_lst)
