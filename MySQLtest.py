from pymysql import Connection
conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='mysql',
)
print(conn.get_server_info())