from flask import Flask, render_template, session, request, jsonify, redirect, url_for, send_file
from os import environ
import database.database as database
import bcrypt


app = Flask(__name__, static_folder="./dist/", static_url_path="/")
app.secret_key = "oiusdfghoisbfkjlasbfæiauhsfdlais"

users = [
    ["admin", "password"],
    ["hej", "test"],
    ["sebbe1231", "lol"]
]

# Root
@app.route("/")
def index():
    if not "loggedin" in session:
        return redirect(url_for("login"))
    
    return send_file("dist/index.html")

# Route to /login
@app.route("/login")
def login():
    return send_file("dist/index.html")

# Check if login details are valid
@app.post("/logincheck")
def logincheck():
    # [Username, Password]
    query = request.json.get("details")

    res = database.db_login(query[0], query[1])

    if res == False:
        return jsonify({"status": False, "message": "Wrong login"})
    
    session["loggedin"] = query
    return jsonify({"status": True})

# Logout
@app.get("/logout")
def logout():
    return session.pop('loggedin', None)

# Get the current session user, im not sure im gonna need this but eh ill keep it for now
@app.get("/getuser")
def getuser():
    if not "loggedin" in session:
        return jsonify({"status": False, "message": "No user logged in on session"})
    
    return jsonify({"status": True, "data": session["loggedin"]})

# Register account if not exists in database
@app.post("/register")
def register():
    query = request.json.get("details")

    if database.db_search_user(query[0]) != None:
        return jsonify({"status": False, "message": "Account with username already exists"})

    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(query[1].encode('utf8'), salt)

    database.db_register(query[0], hashed)
    session["loggedin"] = [query[0], hashed]
    return jsonify({"status": True})

if __name__ == '__main__':
    app.run("0.0.0.0", 8000, True)