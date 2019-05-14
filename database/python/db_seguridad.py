import sqlite3

db_seguridad = '..\sqlite\database_seguridad.db'


def insert_alert(aid, s, ad, atm):
    conn = sqlite3.connect(db_seguridad)
    cursor = conn.cursor()

    cursor.execute("INSERT INTO ALERT_REGISTRY (ALERT_ID, SENSOR, ALERT_DATE, ALERT_TIME)VALUES (?,?,?,?);",
                   (aid, s, ad, atm))

    conn.commit()
    conn.close()


def insert_connection(cd, ct):
    conn = sqlite3.connect(db_seguridad)
    cursor = conn.cursor()

    cursor.execute("INSERT INTO ALERT_REGISTRY (CONNECTION_DATE, CONNECTION_TIME)VALUES (?,?);", (cd, ct))

    conn.commit()
    conn.close()


def get_connections():
    con_lst = []
    conn = sqlite3.connect(db_seguridad)
    cursor = conn.cursor()

    for row in cursor.execute("SELECT * from CONNECTIONS"):
        con_lst.append([row[1], row[2]])

    conn.commit()
    conn.close()
    return con_lst


def get_alerts_by_type(ty):
    ale_lst = []
    conn = sqlite3.connect(db_seguridad)
    cursor = conn.cursor()

    for row in cursor.execute(
            "SELECT * from (SELECT * from ALERT_REGISTRY CROSS JOIN ALERT_TYPE) where ALERT_ID=?", (str(ty),)):
        ale_lst.append([row[1], row[2]])

    conn.commit()
    conn.close()
    return ale_lst


def authentication(u, p):
    conn = sqlite3.connect(db_seguridad)
    cursor = conn.cursor()

    (user, pwd) = cursor.execute("SELECT * from USERS")

    conn.commit()
    conn.close()

    if user == u and pwd == p:
        return True
    else:
        return False
