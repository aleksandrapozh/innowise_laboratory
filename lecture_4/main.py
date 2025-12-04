import sqlite3

# Подключаемся к базе данных
connection = sqlite3.connect('school.db')

# Закрываем соединение
connection.close()