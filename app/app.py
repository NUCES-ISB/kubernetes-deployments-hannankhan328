from flask import Flask
import os
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get("DB_HOST"),
        database=os.environ.get("DB_NAME"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASSWORD")
    )
    return conn

@app.route("/")
def index():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT 1;")
        result = cur.fetchone()
        cur.close()
        conn.close()
        return f"Database connection successful: {result}"
    except Exception as e:
        return f"Error connecting to database: {str(e)}", 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
