# Программа получает на вход список из целых чисел. Ваша задача найти среднее арифметическое введенного списка чисел.


list_numbers = list(map(int,input().split()))
print(sum(list_numbers)/len(list_numbers))
