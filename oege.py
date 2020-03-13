import mysql.connector
from mysql.connector import Error

def connect():
    conn = None
    try:
        conn = mysql.connector.connect(option_files='my.conf')
        if conn.is_connected():
            return conn
    except Error as e:
        print(e)

def store(tableName,record,conn):
    cursor = conn.cursor()
    seperator = ""
    query = ""
    if record['id']:
        query += "UPDATE " + tableName + " SET "
        for key in record:
            if key != 'id':
                query += seperator + str(key) + ' = "' + str(record[key]) + '"'
                seperator = ", "

        query += ' WHERE id  = "' + str(record['id']) + '"'
        cursor.execute(query)
        conn.commit()
        return record
    else:
        keys = ""
        values = ""
        for key in record:
            if key != 'id':
                keys += seperator + '`' + str(key) + '`'
                values += seperator + '"' + str(record[key]) + '"'
                seperator = ", "

        query += "INSERT INTO `" + tableName + "`(" + keys + ") VALUES (" + values + ")"
        cursor.execute(query)
        conn.commit()
        cursor.execute("SELECT LAST_INSERT_ID();")
        record['id'] = cursor.fetchone()[0]
        return record

def fetch_by_id(tableName,value,conn):
    return fetch_by_key_value(tableName,"id",value,conn)

def fetch_by_key_value(tableName,key,value,conn):
    cursor = conn.cursor()
    cursor.execute("SELECT column_name FROM information_schema.COLUMNS WHERE table_name LIKE '%s'" % tableName)
    columns = cursor.fetchall()
    cursor.execute("SELECT * FROM %s WHERE %s = '%s'" % (tableName,key,value))
    values = cursor.fetchone()
    dict = {}
    if values:
        for i in range(0, len(columns)):
            dict[columns[i][0]] = values[i]
        return dict
    else:
        # AKA None
        return values

def delete_by_id(tableName,value,conn):
    cursor = conn.cursor()
    record = fetch_by_id(tableName,value,conn)
    if record:
        cursor.execute("DELETE FROM %s WHERE id = %s" % (tableName,value))
        conn.commit()
        print("Succesfully Deleted!")
    else:
        print("There is no %s with that id." % tableName )
    return record
