# Программа принимает на вход одно натуральное число и выводит его цифры в столбик в обратном порядке.



n = int(input())
while n:
    print(n%10)
    n //= 10
