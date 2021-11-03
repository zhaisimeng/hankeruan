import pymysql

host="localhost"
user="root"
password=""
database="中国工商银行数据库"

#修改功能
def update(sql,param):

    con=pymysql.connect(host=host,user=user,password=password,database=database)

    curses=con.cursor()
    curses.execute(sql,param)

    con.commit()
    curses.close()
    con.close()

#新增数据功能
def insert_into(sql,param):

    con=pymysql.connect(host=host,user=user,password=password,database=database)

    curses=con.cursor()
    curses.execute(sql,param)

    con.commit()
    curses.close()
    con.close()

#删除数据功能
def delete(sql,param):

    con=pymysql.connect(host=host,user=user,password=password,database=database)

    curses=con.cursor()
    curses.execute(sql,param)

    con.commit()
    curses.close()
    con.close()

#查询功能
def select(sql,param,mode="all",size=0):
    con = pymysql.connect(host=host,user=user,password=password,database=database)

    cursor = con.cursor()
    cursor.execute(sql,param)

    if mode == "all":
        return cursor.fetchall()
    elif mode == "one":
        return cursor.fetchone()
    elif mode == "many":
        return cursor.fetchmany(size)

    con.commit()
    cursor.close()
    con.close()
