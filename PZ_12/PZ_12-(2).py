"""
Из списка: ['Валентин', 'Петр', 'Анна', 'Евгений', 'Константин',
'Валерия', 'Юлия'] получить новый список, в котором длина слов
не превышает 5 символов
"""

names_list = ["Валентин", "Петр", "Анна", "Евгений",
              "Константин", "Валерия", "Юлия"]

print(names_list)
print(list(filter(lambda i: len(i) <= 5, names_list)))
