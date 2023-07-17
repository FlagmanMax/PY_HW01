# Программа загадывает число от 0 до 1000.
# Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randint num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint
LOWER_LIMIT = 0
UPPER_LIMIT = 1000
TRY_COUNTER = 10

num = randint(LOWER_LIMIT, UPPER_LIMIT)
print(f"Угадайте число от {LOWER_LIMIT} до {UPPER_LIMIT}. У вас {TRY_COUNTER} попыток ")

result = "Вы не угадали"
for i in range(1,TRY_COUNTER+1):
    a = int(input(f"Попытка {i}: "))
    if a==num:
        result = "Вы угадали"
        break
    elif a>num:
        print("Меньше")
    else:
        print("Больше")
print(result + f" число {num}")





