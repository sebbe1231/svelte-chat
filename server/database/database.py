import sqlite3
import bcrypt
from datetime import datetime

con = sqlite3.connect("database.db")
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS [users] (id integer NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,name text NOT NULL UNIQUE,password text NOT NULL)")
cur.execute("""
    CREATE TABLE IF NOT EXISTS [messages] 
    (id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    user integer NOT NULL,
    receiver integer NOT NULL,
    content text NOT NULL,
    sent_date date NOT NULL)
    """)

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

    res = cur.execute("SELECT id, name, password FROM users WHERE name = :username", {"username": username}).fetchone()
    con.commit()
    con.close()
    return {"status": True, "data": res}

# Search for user in database via username
# Userfull for checking if user exists under registration
def db_search_user(username, id):
    con = sqlite3.connect("database.db")
    cur = con.cursor()

    if username is not None:
        res = cur.execute(f"SELECT id, name FROM users WHERE name = :name", {"name": username}).fetchone()
    
    if id is not None:
        res = cur.execute(f"SELECT id, name FROM users WHERE id = :id", {"id": id}).fetchone()

    con.close()
    return res

# Check if login details are in database
def db_login(username, password):
    con = sqlite3.connect("database.db")
    cur = con.cursor()

    try:
        hashPasswrd = cur.execute(f"SELECT * FROM users WHERE name = :username", {"username": username}).fetchone()
    except TypeError:
        con.close()
        return False
    
    if hashPasswrd is None:
        return {"status": False}

    if bcrypt.checkpw(password.encode('utf8'), hashPasswrd[2]):
        con.close()
        return {"status": True, "data": hashPasswrd}
    else:
        con.close()
        return {"status": False}
    
    
def db_add_msg(user, reciver, content):
    con = sqlite3.connect("database.db")
    cur = con.cursor()

    date = datetime.now()

    cur.execute(f"INSERT INTO messages(user, receiver, content, sent_date) VALUES(?, ?, ?, ?)", (user, reciver, content, date))

    con.commit()
    con.close()

def db_get_msg(user, receiver, amount: int):
    con = sqlite3.connect("database.db")
    cur = con.cursor()

    if receiver is None:
        res = cur.execute("SELECT * FROM messages WHERE user = :user OR receiver = :user", {"user": user}).fetchmany(amount)
        cur.close()
        return res

    res = cur.execute("SELECT * FROM messages WHERE (user = :user AND receiver = :receiver) OR (user = :receiver AND receiver = :user)", {"user": user, "receiver": receiver}).fetchmany(amount)
    con.close()
    return res

    