year = int(input('Введите год:'))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("%d високосный" % year)
else:
    print("%d не високосный" % year)

input()

name = input('Введите имя\n')
age = int(input('Введите возраст\n'))
male = input('Введите пол муж или жен \n')

if male in ['муж']:
    print('Значит, его зовут:' + name)
    if age % 10 in [5, 6, 7, 8, 9, 0]:
        print('Значит ему:', age, 'лет')
    if age % 10 in [1]:
        print('Значит ему:', age, 'год')
    if age % 10 in [2, 3, 4]:
        print('Значит ему:', age, 'года')
if male in ['жен']:
    print('Значит, ее зовут:' + name)
    if age % 10 in [5, 6, 7, 8, 9, 0]:
        print('Значит ей:', age, 'лет')
    if age % 10 in [1]:
        print('Значит ей:', age, 'год')
    if age % 10 in [2, 3, 4]:
        print('Значит ей:', age, 'года')

n = int(input('Введите целое число:'))


def fac(n):
    if n == 0:
        return 1
    return fac(n - 1) * n


print('Факториал равен: ', fac(n))

import random
m = random.randrange(1000, 9999)
print(m)
b = map(int, str(m))
unique_numbers = set(b)
print(unique_numbers)
if len(unique_numbers) == 4:
	print('уникальное число - ', m)

N = int(input('Введите N: '))

for k in range(2, N + 1):
    prime = True
    for i in range(2, k):
        if k % i == 0:
            prime = False
            break
    if prime:
        print('{} - простое число'.format(k))


