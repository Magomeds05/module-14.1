import sqlite3

connection = sqlite3.connect("not_telegram.db")
curs = connection.cursor()

curs.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMACY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

#Заполните её 10 записями:

for i in range(1, 11):
    curs.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)", (f"User{i}", f"example{i}@gmail.com", f"{i * 10}", "1000"))

#Обновите balance у каждой 2ой записи начиная с 1ой на 500:
for j in range(1, 11, 2):
    curs.execute("UPDATE Users SET balance = ? WHERE age = ? ", (500, j*10))

#Удалите каждую 3ую запись в таблице начиная с 1ой:
for k in range(1, 11, 3):
    curs.execute("DELETE FROM Users WHERE username = ?", (k,))

#Сделайте выборку всех записей при помощи fetchall(), где возраст не равен 60 и выведите их в консоль в следующем формате (без id):
curs.execute("SELECT * FROM Users WHERE age != 60")
users = curs.fetchall()
for l in users:
    print(f'Имя: {l[1]} | Почта: {l[2]} | Возраст: {l[3]} | Баланс: {l[4]}')

connection.commit()
connection.close()

#Имя: User2 | Почта: example2@gmail.com | Возраст: 20 | Баланс: 1000
#Имя: User3 | Почта: example3@gmail.com | Возраст: 30 | Баланс: 500
#Имя: User5 | Почта: example5@gmail.com | Возраст: 50 | Баланс: 500
#Имя: User8 | Почта: example8@gmail.com | Возраст: 80 | Баланс: 1000
#Имя: User9 | Почта: example9@gmail.com | Возраст: 90 | Баланс: 500
