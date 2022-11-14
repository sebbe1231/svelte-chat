from flask import Flask, render_template, session, request, jsonify, redirect, url_for, send_file
from os import environ

app = Flask(__name__, static_folder="./dist/", static_url_path="/")
app.secret_key = "oiusdfghoisbfkjlasbfæiauhsfdlais"

users = [
    ["admin", "password"],
    ["hej", "test"],
    ["sebbe1231", "lol"]
]

@app.route("/")
def index():
    if not "loggedin" in session:
        return redirect(url_for("login"))
    
    return send_file("dist/index.html")

@app.route("/login")
def login():
    return send_file("dist/index.html")

@app.post("/logincheck")
def logincheck():
    query = request.json.get("details")

    print(query)

    if not query in users:
        return jsonify({"status": False, "message": "An error occured"})
    
    session["loggedin"] = query
    return jsonify({"status": True})

@app.get("/logout")
def logout():
    return session.pop('loggedin', None)

@app.get("/getuser")
def getuser():
    if not "loggedin" in session:
        return jsonify({"status": False, "message": "No user logged in on session"})
    
    return jsonify({"status": True, "data": session["loggedin"]})

if __name__ == '__main__':
    app.run("0.0.0.0", 8000, True)