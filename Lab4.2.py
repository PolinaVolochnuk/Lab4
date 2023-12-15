"""
Задача 2.
2.Напишіть програму, яка виводить число в стилі LCD-калькулятора. На вхід
програми подається послідовність цифр, яку потрібно вивести на екран в
спеціальному стилі. Розмір всіх цифр 4 символу в ширину і 7 символів у висоту.
Між цифрами повинен бути один порожній стовпець. Перед першою цифрою не повинно
бути пропусків. Виведені цифри повинні бути обведені рамочкою, в кутах якої
знаходиться символ x, горизонтальна лінія створюється з символу -, а вертикальна
- з символу вертикальної риски |. Користувач вводить рядок - послідовність цифр,
а програма має вивести 9 рядків, що містять цифри, записані в зазначеному
форматі.

Автор: Волочнюк Поліна
"""

inp = list(map(lambda x: int(x), ''.join(input("Введіть число: ").split())))

aha = '    '
ahb = ' -- '
avb = '|   '
avc = '   |'
avd = '|  |'

d = {
     0:(ahb, avd, avd, aha, avd, avd, ahb),
     1:(aha, avc, avc, aha, avc, avc, aha),
     2:(ahb, avc, avc, ahb, avb, avb, ahb),
     3:(ahb, avc, avc, ahb, avc, avc, ahb),
     4:(aha, avd, avd, ahb, avc, avc, aha),
     5:(ahb, avb, avb, ahb, avc, avc, ahb),
     6:(ahb, avb, avb, ahb, avd, avd, ahb),
     7:(ahb, avc, avc, aha, avc, avc, aha),
     8:(ahb, avd, avd, ahb, avd, avd, ahb),
     9:(ahb, avd, avd, ahb, avc, avc, ahb)
    }

def print_border(l = len(inp)):
    print('x', end = '')
    print('-' * l * 5, end = '')
    print('x')

print_border()

for i in range(7):
    first = True
    for e in inp:
        if first: print ('|', end = '')
        print(d[e][i], end = ' ')
        first = False
    print('|')

print_border()
