# Напишите программу, которая вычисляет среднее арифметическое четырех введенных целых чисел.

# Числа вводятся в одну строку через пробел.


a,b,c,d = map(int,input("Введите числа: ").split())
sum = (a+b+c+d)/4
print(int(sum))
