# Задание 2 *(вместо 1)
# *(вместо 1) Решить воспроизведение нечетных чисел от 1 до n (включительно),
# не используя ключевое слово yield.
n = 15

generator = (num for num in range(1, n+1, 2))
for _ in range(1, n + 1, 2):
    print(next(generator))
# next(generator)   # если раскомментировать, то должно падать в traceback по StopIteration
