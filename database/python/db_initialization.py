import sqlite3

# database connection, if the database does not exist a new one will be created.
conn = sqlite3.connect("..\sqlite\database_seguridad.db")
cursor = conn.cursor()

# table creation.
cursor.execute("CREATE TABLE USERS (USER_ID INTEGER PRIMARY KEY AUTOINCREMENT, \
USERNAME TEXT NOT NULL, PASSWORD TEXT NOT NULL);")
cursor.execute('CREATE TABLE ALERT_TYPE (ALERT_ID INTEGER PRIMARY KEY AUTOINCREMENT, DESCRIPTION TEXT NOT NULL);')
cursor.execute("CREATE TABLE ALERTS_REGISTRY (AR_ID INTEGER PRIMARY KEY AUTOINCREMENT, ALERT_ID INTEGER NOT NULL, \
SENSOR TEXT NOT NULL, ALERT_DATE TEXT NOT NULL, ALERT_TIME TEXT NOT NULL, \
FOREIGN KEY(ALERT_ID) REFERENCES ALERT_TYPE(ALERT_ID) );")
cursor.execute("CREATE TABLE CONNECTIONS (CONNECTION_ID INTEGER PRIMARY KEY AUTOINCREMENT, \
CONNECTION_DATE TEXT, CONNECTION_TIME TEXT);")

# inserting tuples into tables USERS and ALERT_TYPE.
n = (("NIVEL 1",), ("NIVEL 2",), ("NIVEL 3",), ("NIVEL 4",))
cursor.execute('INSERT INTO USERS(USERNAME, PASSWORD)VALUES (?,?)', ("admin", "12345"))
cursor.execute("INSERT INTO ALERT_TYPE(DESCRIPTION)VALUES (?)", n[0])
cursor.execute("INSERT INTO ALERT_TYPE(DESCRIPTION)VALUES (?)", n[1])
cursor.execute("INSERT INTO ALERT_TYPE(DESCRIPTION)VALUES (?)", n[2])
cursor.execute("INSERT INTO ALERT_TYPE(DESCRIPTION)VALUES (?)", n[3])

# commit changes.
conn.commit()

# closing connection.
conn.close()
