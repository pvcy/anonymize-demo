import os
import psycopg
from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route("/")
def hello():
    return "Hello, World!\n"

@app.route("/users", methods=['GET'])
def get_users():
    page = request.args.get('page', default=1, type=int)
    page_size = 100

    conn = psycopg.connect(
        host="db",
        dbname="postgres",
        user=os.environ['DB_USERNAME'],
        password=os.environ['DB_PASSWORD']
        )

    offset = (page - 1) * page_size

    cur = conn.cursor()
    cur.execute("SELECT * FROM users ORDER BY user_id LIMIT %s OFFSET %s", (page_size, offset))

    data = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]

    return jsonify(data)

