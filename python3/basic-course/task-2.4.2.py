"""
Узнав, что ДНК не является случайной строкой, только что поступившие в Институт биоинформатики
студенты группы информатиков предложили использовать алгоритм сжатия, который сжимает повторяющиеся символы в строке.

Кодирование осуществляется следующим образом:
s = 'aaaabbсaa' преобразуется в 'a4b2с1a2', то есть группы одинаковых символов исходной строки заменяются
на этот символ и количество его повторений в этой позиции строки.

Напишите программу, которая считывает строку, кодирует её предложенным алгоритмом
и выводит закодированную последовательность на стандартный вывод. Кодирование должно учитывать регистр символов.

Sample Input 1:
aaaabbcaa

Sample Output 1:
a4b2c1a2
"""

s = input()
i = 0
current = s[0:1]
res = ''
for x in s:
    if current == x:
        i += 1
        continue
    res += current + str(i)
    i = 1
    current = x
else:
    res += current + str(i)
print(res)
