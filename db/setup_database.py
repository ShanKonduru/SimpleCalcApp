import sqlite3

def create_table():
    # Connect to the database or create it if it doesn't exist
    conn = sqlite3.connect('calculator.db')
    c = conn.cursor()

    # Create the table (you can modify this as per your data schema)
    c.execute('''CREATE TABLE IF NOT EXISTS calculations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    num1 REAL NOT NULL,
                    num2 REAL NOT NULL,
                    operation TEXT NOT NULL,
                    result REAL NOT NULL
                )''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_table()
