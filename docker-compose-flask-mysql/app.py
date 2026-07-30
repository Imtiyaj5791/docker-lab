from flask import Flask
import os
import mysql.connector

app = Flask(__name__)

@app.route("/")
def home():
    db = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

    cursor = db.cursor()
    cursor.execute("SELECT 'Flask connected successfully with MySQL'")
    message = cursor.fetchone()[0]

    cursor.close()
    db.close()

    return message

app.run(host="0.0.0.0", port=5000)
