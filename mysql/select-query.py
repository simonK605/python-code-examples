import mysql.connector

try:
    # Establish a connection to the MySQL database
    connection = mysql.connector.connect(
        host='localhost',
        database='test',
        user=username,  # Replace with your username
        password=password  # Replace with your password
    )

    cursor = connection.cursor()

    # Execute the SELECT query with a parameterized value
    query = 'SELECT * FROM users WHERE id = %s'
    cursor.execute(query, (userId,))

    # Fetch the first row
    row = cursor.fetchone()

    if row:
        print(row[1])  # Assuming 'username' is the second column in the table
    else:
        print("No user found with the specified ID.")

except mysql.connector.Error as e:
    # Handle MySQL errors
    raise Exception(f"MySQL Error: {e}")

finally:
    # Close the cursor and connection in the finally block
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()