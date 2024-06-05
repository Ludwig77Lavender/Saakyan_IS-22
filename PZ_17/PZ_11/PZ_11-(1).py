"""
Средствами языка Python сформировать текстовый файл (.txt),
содержащий последовательность из целых положительных и
отрицательных чисел. Сформировать новый текстовый файл (.txt)
следующего вида, предварительно выполнив требуемую обработку
элементов:
1) Исходные данные
2) Количество элементов
3) Отрицательные нечетные элементы
4) Сумма отрицательных нечетных элементов
5) Среднее арифметическое отрицательных нечетных элементов
"""

# Запишем список в файл numbers_1.txt
nums = ["-99 6 12 -36 20 45 100 -15"]

"""
Создать файл с доступом к записи и записать
в него наш список "nums"
"""
f1 = open("file_1.txt", "w")
f1.writelines(nums)
f1.close()

# Дублируем список в новый файл file_2.txt
f2 = open("file_2.txt", "w")
f2.write("Исходные данные: ")
f2.writelines(nums)
f2.close()

# Строку преобразуем в числа
f1 = open("file_1.txt")
n = f1.read()
n = n.split()
for i in range(len(n)):
    n[i] = int(n[i])
f1.close()

"""
Находим нечётные отрицательные числа и прибавляем их,
попутно находим среднее арифметическое значение
"""
ii = []
k = 0
for i in range(len(n)):
    if n[i] < 0 and n[i] % 2 != 0:
        ii.append(n[i])
        k += n[i]
gg = k // len(ii)

# Открываем файл для дозаписи
f2 = open("file_2.txt", "a", encoding="cp1251")
f2.write("\n")
# Выводим результат
print(f"Количество элементов: {len(n)}", file=f2)
print("Отрицательные нечётные элементы:", *ii, file=f2)
print(f"Сумма отрицательных нечётных чисел: {k}", file=f2)
print(f"Среднее арифметическое отрицательных нечётных чисел: {gg}", file=f2)
f2.close()