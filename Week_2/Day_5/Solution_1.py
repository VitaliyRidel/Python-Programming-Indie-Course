# В данной задаче необходимо сравнить два целых числа A и B. Они поступают на вход программе отдельно в каждой строке.

# Ваша задача вывести символ "<", если A меньше B, ">", если A больше B и "=", если A=B.


A = int(input())
B = int(input())
if A<B:
    print('<')
else:
    if A>B:
        print('>')
    else:
        if A==B:
            print('=')
