import mysql.connector
import os
from sha1 import calculateHash
conn = mysql.connector.connect(option_files='my.conf')
salt = os.urandom(32).hex()
user = "testUser"
password = "test"
hash = calculateHash(salt,password)

cursor = conn.cursor()
cursor.execute("CREATE TABLE user ( `id` INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, `username` VARCHAR(30) NOT NULL, `hash` VARCHAR(1000) NOT NULL, `salt` VARCHAR(1000) NOT NULL )")
conn.commit()
cursor.execute("INSERT INTO `user` (`username`,`hash`,`salt`) VALUES ('%s','%s','%s')" % (user,hash,salt) )
conn.commit()
cursor.execute("CREATE TABLE nurse ( `id` INT UNSIGNED AUTO_INCREMENT PRIMARY KEY, `uniformColor` VARCHAR(30) NOT NULL)")
conn.commit()
cursor.execute("INSERT INTO nurse (`id`,`uniformColor`) VALUES ('1','White')")
conn.commit()
