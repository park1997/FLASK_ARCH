import pymysql

MYSQL_HOST = "localhost"
MYSQL_CONN = pymysql.connect(
    host = MYSQL_HOST,
    port = 3306,
    user = "byeonghyeon",
    passwd = "qudgus97",
    db = "blog_db",
    charset = "utf8"
)

def conn_mysqldb():
    # conn이 안되어있다면
    if not MYSQL_CONN.open:
        MYSQL_CONN.ping(reconnect = True)
    return MYSQL_CONN