import sqlite3


connection = sqlite3.connect('test.db')
curosr = connection.cursor()

sql = '''CREATE TABLE IF NOT EXISTS Person
                (PID INTEGER PRIMARY KEY AUTOINCREMENT,
                NAME VARCHAR(100),
                HEIGHT INT)'''
curosr.execute(sql)

# sql = "UPDATE Person SET NAME = 'iphone x ', HEIGHT = 849 WHERE NAME = 'dor ingber'"


# sql ="DELETE FROM Person WHERE HEIGHT = '849' "

# sql = "INSERT INTO Person (NAME, HEIGHT) VALUES('redmi 6',7499)"
# curosr.execute(sql)
# connection.commit()

sql = 'SELECT * FROM Person'
curosr.execute(sql)

rows = curosr.fetchall()

# for row in rows:
#     print(row)

connection.close()
