
from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)

# Database connection configuration
db_config = {
    'user': 'root',
    'password': os.getenv('MYSQL_PASSWORD'),
    'host': os.getenv('MYSQL_HOST'),
    'database': os.getenv('MYSQL_DB')
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
