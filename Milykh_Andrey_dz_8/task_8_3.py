# task_8_3.py
# Задание 3
# Написать декоратор для логирования типов позиционных аргументов функции


def type_logger(fn):
    def wrapper(*args):
        # print("код, который отработает перед вызовом функции")
        print(f"{str(fn.__name__)}(", end="")
        for i in range(len(args)):
            if i == len(args) - 1:
                print(f"{args[i]}: {type(args[i])}", end=")\n")
            else:
                print(f"{args[i]}: {type(args[i])}", end=", ")
        return fn(*args)
    return wrapper


@type_logger
def calc_cube(x):
    return x**3


@type_logger
def calc_sum(x, y):
    return x + y


a = calc_cube(5)
print(f"resul = {a}")

z = calc_sum(3, 7)
print(f"result= {z}")
