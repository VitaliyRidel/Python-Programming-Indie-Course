# a,s,d=map(str,input().split())
# print('Simvol code',a,'is',str(ord(a))+'.')
# print('Simvol code',s,'is',str(ord(s))+'.')
# print('Simvol code',d,'is',str(ord(d))+'.')


# print((1+2)*('4'+'5'))


# a = str(input())
# print(a[-1:-2])


# a = str(input())
# print(a.count('e'))


# a = str(input())
# n = a.split('A','O','Y','E','U','I')
# print(n)


a = input()
n = a.upper().replace('O','').replace('E','').lower()
print(n)


# a = str(input())
# n = a.replace(' ',',')
# print(n)