import pymysql.cursors

def conn():
    connection = pymysql.connect(
    host='localhost',
    user='root',
    password='Prer1423*123',
    database='ecommerce',  
    cursorclass=pymysql.cursors.DictCursor
)
    return(connection)