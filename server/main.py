from flask import Flask, send_file, jsonify

app = Flask(__name__, static_folder="./dist/", static_url_path="/")

@app.route("/")
def index():
    return send_file("dist/index.html")

@app.route("/api/test")
def test():
    return jsonify({""})

if __name__ == '__main__':
    app.run("0.0.0.0", 8000, True)