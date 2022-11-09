import os
import psycopg
from flask import Flask, jsonify

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route("/")
def hello():
    return "Hello, World!\n"

@app.route("/users", methods = ['GET'])
def all_users():
    conn = psycopg.connect(
        host="db",
        dbname="postgres",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD']
        )

    cur = conn.cursor()
    cur.execute("SELECT * FROM users")

    data = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]

    return jsonify(data)

