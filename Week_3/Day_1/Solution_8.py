# Программа принимает на вход натуральное число N.
# Ваша задача вывести на экран все числа от N до 1 в сторону уменьшения каждое число на отдельной строке.


n = int(input())
for n in range(n, 0, -1):
    print(n)
