import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def users():
    res = requests.get("http://users-api:8000/users")

    users_json = res.json()

    return render_template('users.html', users=users_json)

