import mysql.connector

conn = mysql.connector.connect(option_files='my.conf')

cursor = conn.cursor()
cursor.execute("DROP TABLE user,nurse")
conn.commit()
