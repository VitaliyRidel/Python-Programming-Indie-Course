# На вход программе поступает слово. Вам необходимо воспроизвести процесс, в котором каждый раз у этого слово будет пропадать первая и последняя буква.
# Этот процесс необходимо закончить, когда в слове останется только одна буква или слово  станет пустой строкой.
# При этом результат каждого этапа нужно выводить.


s = input()
print(s)
while len(s)>1:
    s = s[1:-1]
    print(s)
