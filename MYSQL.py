import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='0')
conn.autocommit=True
if conn.is_connected():
    print('\n Connected Succesfully')
else:
    print('\n Not Connected')

def where():
    