import sqlite3

def create_table():
    connection = sqlite3.connect('calculator.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS calculations 
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       num1 REAL NOT NULL,
                       num2 REAL NOT NULL,
                       operation TEXT NOT NULL,
                       result REAL NOT NULL)''')
    connection.commit()
    connection.close()

def insert_calculation(num1, num2, operation, result):
    connection = sqlite3.connect('calculator.db')
    cursor = connection.cursor()
    cursor.execute('''INSERT INTO calculations (num1, num2, operation, result) 
                      VALUES (?, ?, ?, ?)''', (num1, num2, operation, result))
    connection.commit()
    connection.close()
