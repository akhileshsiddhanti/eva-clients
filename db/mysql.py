import pymysql

def get_conn():
    conn = pymysql.connect(host='localhost',
                           port=3306,
                           user='root',
                           passwd='Hscjeremylin214',
                           db='company',
                           charset='utf8',
                           use_unicode=True)
    return conn
