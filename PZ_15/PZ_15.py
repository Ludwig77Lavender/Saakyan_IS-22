import sqlite3

# Функция для создания базы данных и таблицы, если они не существуют
def create_table():
    conn = sqlite3.connect('opt_base.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Товары
                 (Код INTEGER PRIMARY KEY,
                 Наименование_товара TEXT,
                 Наименование_магазина TEXT,
                 Заявки_магазина INTEGER,
                 Количество_товара INTEGER,
                 Единицы_измерения TEXT,
                 Оптовая_цена REAL)''')
    conn.commit()
    conn.close()

# Функция для добавления нового товара
def add_item(код, наименование, магазин, заявки, количество, единицы, цена):
    conn = sqlite3.connect('opt_base.db')
    c = conn.cursor()
    c.execute("INSERT INTO Товары VALUES (?, ?, ?, ?, ?, ?, ?)",
              (код, наименование, магазин, заявки, количество, единицы, цена))
    conn.commit()
    conn.close()

# Функция для поиска товара по наименованию магазина
def find_item_by_shop(магазин):
    conn = sqlite3.connect('opt_base.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Товары WHERE Наименование_магазина=?", (магазин,))
    items = c.fetchall()
    conn.close()
    return items

# Функция для удаления товара по коду
def delete_item(код):
    conn = sqlite3.connect('opt_base.db')
    c = conn.cursor()
    c.execute("DELETE FROM Товары WHERE Код=?", (код,))
    conn.commit()
    conn.close()

# Функция для редактирования информации о товаре
def edit_item(код, новые_данные):
    conn = sqlite3.connect('opt_base.db')
    c = conn.cursor()
    c.execute("UPDATE Товары SET Наименование_товара=?, Наименование_магазина=?, Заявки_магазина=?, "
              "Количество_товара=?, Единицы_измерения=?, Оптовая_цена=? WHERE Код=?", (новые_данные[0],
              новые_данные[1], новые_данные[2], новые_данные[3], новые_данные[4], новые_данные[5], код))
    conn.commit()
    conn.close()

# Создаем таблицу, если она еще не создана
create_table()

# Пример использования функций
add_item(1, "Шоколад", "Магазин 1", 5, 100, "шт", 50.0)
add_item(2, "Чай", "Магазин 2", 10, 200, "пакет", 30.0)

print(find_item_by_shop("Магазин 1"))

edit_item(1, ("Шоколад", "Новый магазин", 8, 150, "шт", 55.0))

print(find_item_by_shop("Новый магазин"))

delete_item(2)

print(find_item_by_shop("Магазин 2"))
