from dbutils.pooled_db import PooledDB
import pymysql

POOL = PooledDB(
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
    charset='utf8'
)


def fetchAll(sql, *args):
    conn = POOL.connection()
    cursor = conn.cursor()
    cursor.execute(sql, args)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


def fetchOne(sql, *args):
    conn = POOL.connection()
    cursor = conn.cursor()
    cursor.execute(sql, args)
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result
