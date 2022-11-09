import json
import os
import psycopg
import time

retries=0
while retries < 3:
    try:
        retries += 1
        print(f"Attempt {retries} to connect to database")
        conn = psycopg.connect(
            host="db",
            dbname="postgres",
            user=os.environ['DB_USERNAME'],
            password=os.environ['DB_PASSWORD'])
        break
    except psycopg.OperationalError as error:
        print("Waiting on database.")
        time.sleep(5)

cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS users;')

cur.execute('CREATE TABLE IF NOT EXISTS users (user_id int NOT NULL UNIQUE,'
                                                'first_name varchar(255),'
                                                'last_name varchar(255),'
                                                'phone varchar(15),'
                                                'city varchar(255),'
                                                'state varchar(30),'
                                                'zip varchar(12),'
                                                'age int,'
                                                'gender varchar(10)'
                                                ');'
                                                )

with open('users.json') as users_json:
    users_data = json.load(users_json)
    insert_sql = """ insert into users
        select * from json_populate_recordset(NULL::users, %s) """
    cur.execute(insert_sql, (json.dumps(users_data),))

conn.commit()

cur.close()
conn.close()

print("Done loading")
