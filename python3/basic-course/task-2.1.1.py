"""
Напишите программу, которая считывает со стандартного ввода целые числа, по одному числу в строке,
и после первого введенного нуля выводит сумму полученных на вход чисел.

Sample Input 1:
5
-3
8
4
0

Sample Output 1:
14
"""

total = 0
while True:
    x = int(input())
    if x == 0:
        break
    total += x
print(total)
