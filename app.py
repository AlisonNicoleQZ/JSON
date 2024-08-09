from flask import Flask, jsonify
import pyodbc

app = Flask(__name__)

def get_db_connection():
    connection = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=LAPTOPHP\SQLEXPRESS;"  
        "DATABASE=CompanyDB;"
        "Trusted_Connection=yes;"
    )
    return connection

@app.route('/employees', methods=['GET'])
def get_employees():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("EXEC GetEmployees")
    result = cursor.fetchone()[0]  # JSON
    
    cursor.close()
    connection.close()
    return jsonify({'employees_json': result})

if __name__ == '__main__':
    app.run(debug=True)
