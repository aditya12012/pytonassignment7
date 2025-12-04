import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        database="testdb",
        user="postgres",
        password="your_password"
    )
    print("Connection successful!")
except Exception as e:
    print("Error:", e)
finally:
    if 'conn' in locals():
        conn.close()
        print("Connection closed.")
