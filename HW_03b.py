# Вы загадываете число от 0 до 1000.
# программа угадает число за 10 попыток.
# Вы подсказываете «больше» или «меньше» после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randint num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint
LOWER_LIMIT = 0
UPPER_LIMIT = 1000
TRY_COUNTER = 10

print(f"Загадайте число от {LOWER_LIMIT} до {UPPER_LIMIT}. Программа угадает его за {TRY_COUNTER} попыток: ")
num = randint(LOWER_LIMIT, UPPER_LIMIT)

ul = UPPER_LIMIT
ll = LOWER_LIMIT
for i in range(1,TRY_COUNTER+1):
    value = ll + (ul-ll)//2
    print(f"Попытка {i}: {value}")

    answer = int(input("Введите 1 если программа угадала. 2 если число больше, а 3 если число меньше загаданного "))
    if answer == 1:
        print("Число угадано")
        break
    elif answer == 2:
        ul = value
    else:
        ll = value

print (f"Результат поиска = {value}")
