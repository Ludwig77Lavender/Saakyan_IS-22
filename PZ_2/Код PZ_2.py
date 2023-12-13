def calculate_rectangle_area(a, b):
    return a * b


def calculate_square_quantity(a, b, c):
    return (a // c) * (b // c)


def calculate_unused_area(a, b, c):
    rectangle_area = calculate_rectangle_area(a, b)
    square_quantity = calculate_square_quantity(a, b, c)
    square_area = square_quantity * c ** 2
    unused_area = rectangle_area - square_area
    return unused_area


a = int(input("Введите значение A: "))
b = int(input("Введите значение B: "))
c = int(input("Введите значение C: "))

rectangle_area = calculate_rectangle_area(a, b)
square_quantity = calculate_square_quantity(a, b, c)
unused_area = calculate_unused_area(a, b, c)

print("Площадь прямоугольника: ", rectangle_area)
print("Количество возможных квадратов: ", square_quantity)
print("Площадь не занятой части: ", unused_area)
