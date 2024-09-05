import mysql.connector
from flask import Flask, jsonify

app = Flask(__name__)
"""
Reads the secret from the file at the given path and returns it.
"""
def read_secret(secret_path):
    with open(secret_path, 'r') as secret_file:
        return secret_file.read().strip()


# Database connection configuration
db_config = {
    'user': 'root',
    'password': read_secret(r'/etc/secrets/MYSQL_PASSWORD'),
    'host': read_secret(r'/etc/secrets/MYSQL_HOST'),
    'database': read_secret(r'/etc/secrets/MYSQL_DB')
}


@app.route('/customers', methods=['GET'])
def get_customers():
    try:
        # Connect to the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)

        # Execute the query
        cursor.execute("SELECT * FROM customers")

        # Fetch all rows
        customers = cursor.fetchall()

        # Close the connection
        cursor.close()
        conn.close()

        return jsonify(customers)
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
