import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

dataBase = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST", "localhost"),
    user=os.getenv("MYSQL_USER", "root"),
    passwd=os.getenv("MYSQL_PASSWORD", ""),
)

cursorObject = dataBase.cursor()
cursorObject.execute("CREATE DATABASE IF NOT EXISTS corecrm")

print("Database corecrm created successfully!")
