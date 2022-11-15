import sqlite3
import bcrypt

con = sqlite3.connect("database.db")
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS [users] (id integer NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,name text NOT NULL UNIQUE,password text NOT NULL)")
cur.execute("CREATE TABLE IF NOT EXISTS [messages] (id integer NOT NULL PRIMARY KEY AUTOINCREMENT,user_id integer NOT NULL,receiver_id integer NOT NULL,content text NOT NULL,sent_date date NOT NULL)")

con.commit()
con.close()

# Regsiter user in database
def db_register(username, password):
    con = sqlite3.connect("database.db")
    cur = con.cursor()

    cur.execute(f"""
        INSERT INTO users(name, password) VALUES
            (?, ?)
    """, (username, password))

    con.commit()
    con.close()

# Search for user in database via username
# Userfull for checking if user exists under registration
def db_search_user(username):
    con = sqlite3.connect("database.db")
    cur = con.cursor()

    res = cur.execute(f"SELECT * FROM users WHERE name = '{username}'").fetchone()

    con.close()

    return res

# Check if login details are in database
def db_login(username, password):
    con = sqlite3.connect("database.db")
    cur = con.cursor()

    hashPasswrd = cur.execute(f"SELECT password FROM users WHERE name = '{username}'")

    if bcrypt.checkpw(password.encode('utf8'), hashPasswrd):
        con.close()
        return True
    else:
        con.close()
        return False 