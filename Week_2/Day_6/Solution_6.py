# Выведите все точные квадраты натуральных чисел, не превосходящие данного числа N.

# Задано единственное целое число N.

# Необходимо вывести  все точные квадраты натуральных чисел, не превосходящие данного числа N.


N = int(input())
b = 1
while b**2<=N:
    print(b**2)
    b+=1
