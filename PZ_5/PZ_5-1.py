# Составить функцию решения задачи: из заданного числа вычли
# сумму его цифр. Из результата вновь вычли сумму его цифр и т. д.
# Через сколько таких действий получится нуль?

# Создаём функцию
def operation11():
    nums = int(input("Введите число: "))
    a = 0
    # Пока nums > 0
    while nums > 0:
        # Создаём переменную в которую поместим сумму цифр nums
        sum_digits = 0
        # Создаём цикл выполняющий операцию вычитания
        for i in str(nums):
            # К переменной прибавляем получившийся результат
            sum_digits += int(i)
        # Отнимаем от числа сумму его цифр
        nums -= sum_digits
        # Считаем количество проведённых операций
        a += 1

    # Вывести результат
    print("Конечный результат:", nums)
    print("Сколько операций потребовалось:", a)

# Вызвать функцию
operation11()
