import os
import mysql.connector

# Get server name from environment variable or default to 'localhost'
server_name = os.getenv('SERVER_NAME', 'localhost')

# Database configuration dictionary with default values from environment variables
db_config = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASS', ''),
    'database': os.getenv('DB_NAME', 'test'),
}

# Create a connection string for informational purposes
connection_string = f"mysql://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['database']}"

# Establish a connection to the MySQL database using mysql.connector
db = mysql.connector.connect(
    host=db_config['host'],
    user=db_config['user'],
    password=db_config['password'],
    database=db_config['database']
)