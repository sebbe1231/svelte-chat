from flask import Flask, render_template, session, request, jsonify, redirect, url_for, send_file
from os import environ
import database.database as database
import bcrypt


app = Flask(__name__, static_folder="./dist/", static_url_path="/")
app.secret_key = environ["APP_SECRET"]

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

@app.route("/message/<id>")
def message(id):
    return send_file("dist/index.html")

# Check if login details are valid
@app.post("/logincheck")
def logincheck():
    query = request.json.get("details")

    res = database.db_login(query[0], query[1])

    if res["status"] == False:
        return jsonify({"status": False, "message": "Wrong login"})
    
    session["loggedin"] = {
        "id": res["data"][0],
        "username": res["data"][1]
    }

    return jsonify({"status": True, "data": session["loggedin"]})

# Logout
@app.get("/logout")
def logout():
    return session.pop('loggedin', None)

# Register account if not exists in database
@app.post("/register")
def register():
    query = request.json.get("details")

    if database.db_search_user(query[0]) != None:
        return jsonify({"status": False, "message": "Account with username already exists"})

    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(query[1].encode('utf8'), salt)

    res = database.db_register(query[0], hashed)
    session["loggedin"] = {
        "id": res["data"][0],
        "username": res["data"][1]
    }
    session["loggedin"] = query[0]
    return jsonify({"status": True, "data": session["loggedin"]})

# Updates user in store.js on new build
# i know its pretty cursed, BUT, cope
@app.get("/me")
def me():
    if not "loggedin" in session:
        return jsonify({"status": False, "message": "No user in session"})

    return jsonify({"status": True, "data": session["loggedin"]})

@app.post("/sendmessage")
def sendmessage():
    query = request.json.get("details")

    if not "loggedin" in session:
        return jsonify({"status": False, "message": "No user in session"})
    
    database.db_add_msg(session["loggedin"], query[0], query[1])

    return jsonify({"status": True})

@app.post("/getmessage")
def getmessage():
    query = request.json.get("details")

    if not "loggedin" in session:
        return jsonify({"status": False, "message": "No user in session"})
    
    res = database.db_get_msg(session["loggedin"], query[0], query[1])

    return jsonify({"status": True, "data": res})

@app.post("/getuser")
def getuser():
    query = request.json.get("details")

    if database.db_search_user(query[0]) == None:
        return jsonify({"status": False, "message": "Account does not exist"})
    
    res = database.db_search_user(query[0])

    print("resp")
    print(res)

    return jsonify({"status": True, "data": res})

if __name__ == '__main__':
    app.run("0.0.0.0", 8000, True)