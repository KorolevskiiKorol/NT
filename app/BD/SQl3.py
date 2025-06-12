import sqlite3

# db = sqlite3.connect('users.db')
# c = db.cursor()
#
# c.execute("""CREATE TABLE IF NOT EXISTS users (
# username TEXT NOT NULL,
# password TEXT NOT NULL,
# number INTEGER NOT NULL)"""
# )
# db.commit()
# db.close()




def reg_users(name, password, number):
    db = sqlite3.connect('users.db')
    c = db.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS users (
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    number INTEGER NOT NULL)"""
              )

    c.execute('INSERT INTO users (username, password, number) VALUES (?, ?, ?)', (name, password, number))

    db.commit()
    db.close()

def out_data():
    db = sqlite3.connect('users.db')
    c = db.cursor()

    c.execute('SELECT * FROM users')
    data = c.fetchall()

    for row in data:
        print(row)

    c.close()