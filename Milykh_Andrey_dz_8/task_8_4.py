# task_8_4.py#
# Задание 4
# Написать декоратор с аргументом-функцией (callback), позволяющий
# валидировать входные значения функции и выбрасывать исключение ValueError,
# если что-то не так


def val_checker(func):
    def wrapper(arg):
        # print("код, который отработает перед вызовом функции")
        print(f"Run function: {str(func.__name__)}(), with param: {arg}")
        try:
            if int(arg) >= 0:
                return func(arg)
            else:
                raise ValueError
        except ValueError:
            print(f'ValueError: wrong val {arg}')

    return wrapper


@val_checker
def calc_cube(x):
    """Возведение числа в третью степень"""
    return x**3


if __name__ == '__main__':
    print(calc_cube(5))
    print(calc_cube('ss'))
    print(calc_cube(-5))
