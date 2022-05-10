# Программа запрашивает у пользователя курс доллара - вещественное число,  и также количество долларов(целое число),
# которое пользователь хочет приобрести. В итоге программа должна вывести следующее сообщение:

# "Current dollar rate is <курс доллара>. You want buy <количество долларов> dollars
# You must pay <стоимость>"


a,b = float(input()),int(input())
text1 = f"""Current dollar rate is {a}. You want buy {b} dollars"""
text2 = f"""You must pay {a*b}"""
print(text1,text2,sep='\n')
