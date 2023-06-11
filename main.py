# 1.
# Дана строчка, представляющая собой набор цифр.И дано
# число от 0 до 19(не включая).Определить, присутсвуют
# ли в строчке 2 цифры, такие, что сумма их равна введённому
# Вами числу? Если да, то вывести эти цифры и их
# индексы.
string = int(input('dann'))
numbers = int(input('vvod '))
str1 = str(string)
stringlen = len(str1)
a = 1
b = 100
c = 10
while stringlen > 0:
    str = stringlen + 5
    str2 = str - 2
    str3 = str - 3
    num1 = string // str % 10
    num2 = string // b % 10
    num3 = string // c % 10
    str -= 1
    stringlen -= 1
    a *= 10
    b *= 10
    c *= 10
    if num1 + num2 == numbers:
        print(num1)
    if num2 + num3 == numbers:
        print(num2)
    if num1 + num3 == numbers:
        print(num1,num3)
else:
    print('otvet')



# 2.
# Даны две строки.Эти  строки  между собой отличаются только одним
# символом.Вторая строка получена путём добавления слуайного символа
# в случайную позицию в первой строке.Вывести данный символ и его
# индекс.


string1 = input('vvod dann\n')  # abcde вводим данные
string2 = input('vvod dann2\n')  # abcdex вводим вторые даные
stringlen = len(string1) # определяем длинну первой строки
stringlen1 = len(string2) # определяем длинну второй строки
while stringlen1 > -1: # пока у нас вторая строка длиннее певой
    str = int(stringlen)  # определяем длинну первой строки целыми числами
    str2 =int(stringlen1) # определяем вторую строку целыми числами
    s = string1[str:1] # определяем индекс первого числа
    a = string2[str2:1] # определяем индек второго числа
    stringlen -= 1
    stringlen1 -= 1
    if s != a:
        print(a)
    print(stringlen1 + 1)
    break
else:
    print('vvod')


