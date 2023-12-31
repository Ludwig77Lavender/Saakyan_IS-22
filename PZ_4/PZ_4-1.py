# Пользователь вводит два целых числа A и B. Выводятся
# все целые числа, расположенные между A и B, включая
# сами числа A и B, а так же количество N этих чисел

# Ввод целых чисел A и B
A = int(input("Введите число A: "))
B = int(input("Введите число B: "))

# Создание переменной для добавления неё диапазона
num = 0

# Если A <= B, то перечисление будет начинаться с числа A
if A <= B:
    # Перебор чисел от A до B создавая порядковое исчисление
    # прибавляя к A + 1 до тех пор, пока конечное число не будет равно B
    for n in range(A, B + 1):
        # Вывести порядковое исчисление
        print(n)
        # Прибавить к num + 1 за каждое число в цепочке
        num += 1
# Если B >= A, то развернуть список (Вывести числа начиная
# с B до A, отнимая от B - 1 до тех пор, пока не дойдёт до значения A)
else:
    for n in range(A, B - 1, -1):
        print(n)
        num += 1

print(f"Количество чисел: {num}")
