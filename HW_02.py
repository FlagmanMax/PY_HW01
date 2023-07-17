# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: «Число является простым,
# если делится нацело только на единицу и на себя».
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

while True:
    n = int(input("Введите положительное число до 100000 для проверки: "))
    if n>0 and n<100000:
        break
    print("Ошибка ввода!")

result = "число простое"
for i in range(2,int(n/2)+1):
    if n%i == 0:
        result = "число не простое"
        break
print(result)