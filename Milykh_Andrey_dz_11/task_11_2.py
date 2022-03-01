# task_11_2.py
from actions.custom_exceptions import CustomMessage, CustomTypeError, CustomZeroDivision


def check_number(num: int):
    if not isinstance(num, int):
        raise CustomTypeError


def custom_division(x: int, y: int):
    try:
        check_number(x)
        check_number(y)
        if not y:
            raise CustomZeroDivision
        return x/y
    except CustomMessage as err:
        print(err)


a = 1
b = 0
print(custom_division(a, b))

b = -1
print(custom_division(a, b))

a = "test"
print(custom_division(a, b))

a = 15
b = [1, 2, 3]
print(custom_division(a, b))

b = 3
print(custom_division(a, b))
