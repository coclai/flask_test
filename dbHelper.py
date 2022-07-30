from dbutils.pooled_db import PooledDB
import pymysql


class DbHelper():
    def __init__(self):
        self.pool = PooledDB(
            creator=pymysql,
            maxconnections=6,
            mincached=2,
            maxcached=5,
            maxshared=3,
            blocking=True,
            maxusage=None,
            setsession=[],
            ping=0,
            host='192.168.174.130',
            port=3306,
            user='fanta',
            password='1551',
            database='python',
            charset='utf8')

    def open(self):
        conn = self.pool.connection()
        cursor = conn.cursor()
        return conn, cursor

    def close(self, conn, cursor):
        cursor.close()
        conn.close()

    def fetchAll(self, sql, *args):
        conn, cursor = self.open()
        cursor.execute(sql, args)
        result = cursor.fetchall()
        self.close(conn, cursor)
        return result

    def fetchOne(self, sql, *args):
        conn, cursor = self.open()
        cursor.execute(sql, args)
        result = cursor.fetchone()
        self.close(conn, cursor)
        return result


db = DbHelper()
