# На вход программе поступает строка, ваша задача удалить из нее все символы "w" и "z".

# Учитываем только маленькие буквы.


a = str(input())
n = a.replace('w','').replace('z','')
print(n)