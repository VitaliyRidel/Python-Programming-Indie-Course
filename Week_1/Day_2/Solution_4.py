# Напишите программу, которая находит наилучшую оценку ученика за решение пяти контрольных работ.

# Оценки всех пяти работ вводятся в одну строку, могут быть только целые числа от 1 до 100


a,b,c,d,e = map(int,input().split())
print(abs(max(a,b,c,d,e)))
