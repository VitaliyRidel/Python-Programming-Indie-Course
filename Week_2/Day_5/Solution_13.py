# Напишите программу, которая имитирует проверку пароля, придуманного пользователем.
# Пользователь сперва вводит пароль, потом вводит подтверждение пароля. Вам нужно обработать следующие ситуации:

# если пароль, который ввёл пользователь (в первый раз) короче 7 символов, программа выводит "Short"
# если пароль достаточно длинный, но введённый во второй раз пароль не совпадает с первым, программа выводит "Difference"
# если же и эта проверка пройдена успешно, программа выводит "OK" (латинскими буквами).


a = input()
b = input()
if len(a)<7:
    print('Short')
elif len(a)>=7 and len(a)!=len(b):
    print('Difference')
else:
    print('OK')
