# Дано целое число N (>0) и символ C.
# Вывести строку длины N, которая состоит из символов C.

# Вводим длинну строки
n = int(input("Введите число: "))
# Вводим число
c = input("Введите символ: ")

# Если число меньше 0, то попросить
# ввести корректное значение
while n < 0:
    print("Введите число больше 0")
    n = int(input("Введите число: "))
    c = input("Введите символ: ")
else:
    # Вывести результат
    print(c * n)
