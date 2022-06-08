# В архитектуре компьютера важную роль играют числа, являющиеся степенями двойки: 1, 2, 4, 8 и так далее.
# Напишите программу, которая проверяет, является ли введённое натуральное число степенью двойки.
# Если да, то выводится сама эта степень; если нет, выводится «НЕТ»


a = int(input())
b = 0
while a != 1:
    if a % 2 != 0:
        print('НЕТ')
        break
    a //= 2
    b += 1
else:
    print(b)