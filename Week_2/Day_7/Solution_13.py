# Программа принимает на вход одно натуральное число и выводит его цифры в двоичной системе в столбик в обратном порядке.


n = int(input())
while n > 0:
    print(n%2)
    n = n//2
