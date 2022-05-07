# Программа принимает на вход три символа через пробел в одну строку.
# Необходимо вывести код каждого символа при помощи функции ord в определенном формате.


a,b,c = map(str,input().split())
print('Simvol code %s is'%(a),ord(a),end='.\n')
print('Simvol code %s is'%(b),ord(b),end='.\n')
print('Simvol code %s is'%(c),ord(c),end='.\n')