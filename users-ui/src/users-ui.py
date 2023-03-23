import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def users():
    page = request.args.get('page', default=1, type=int)
    res = requests.get(f"http://users-api:8000/users?page={page}")

    users_json = res.json()

    return render_template('users.html', users=users_json, page=page)

