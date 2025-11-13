import sqlite3
import pymysql


def read_db():
    # 连接到SQLite数据库
    # 如果文件不存在，会自动在当前目录创建一个名为example.db的数据库文件
    conn = sqlite3.connect('example.db')

    # 创建一个cursor对象，用于执行SQL命令
    cursor = conn.cursor()

    # 创建一个表
    cursor.execute('''CREATE TABLE IF NOT EXISTS stocks
                   (date text, trans text, symbol text, qty real, price real)''')

    # 插入数据
    cursor.execute("INSERT INTO stocks VALUES ('2023-04-01','BUY','RHAT',100,35.14)")

    # 提交事务
    conn.commit()

    # 查询数据
    cursor.execute("SELECT * FROM stocks")
    print(cursor.fetchall())

    # 关闭连接
    conn.close()


from datetime import datetime


def start():
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='888888', database='test_db',
                           charset='utf8')
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor = conn.cursor()
    team_list = [
        ("默认销售团队", 101, now_str, now_str, "T", "T"),
        ("默认服务团队", 102, now_str, now_str, "T", "T"),
    ]
    sql_insert = "insert into team(team_name,team_leader_id,create_time,update_time,is_default,is_active) values(%s,%s,%s,%s,%s,%s)"  # 省略主键id
    try:
        cursor.execute("truncate team;")  # 删除原有数据
        cursor.executemany(sql_insert, team_list)
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(e)
    finally:
        cursor.close()
        conn.close()


def read_pg():
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='88888218', database='test_db',
                           charset='utf8')
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor = conn.cursor()


if __name__ == '__main__':
    read_db()
