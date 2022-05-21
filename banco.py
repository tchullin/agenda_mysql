import mysql.connector

# con = None
def ConexaoBanco():
    con = None
    try:
        con = mysql.connector.connect(
            host='localhost',
            user='root',
            password='lotus123',
            database='agenda',
        )
    except Exception as ex:
        print(ex)
    return con

def dql(query): #select
    vcon=ConexaoBanco()
    c=vcon.cursor()
    c.execute(query)
    res=c.fetchall()
    vcon.close()
    return res

def dml(query):#insert , update, delete
    try:
        vcon = ConexaoBanco()
        c=vcon.cursor()
        c.execute(query)
        vcon.commit()
        vcon.close()
        vcon=ConexaoBanco()
    except Exception as ex:
        print(ex)
