import pymysql

db = pymysql.connect("localhost", "root", "123456", "mt")

cursor = db.cursor()

table = cursor.execute("SELECT * FROM mtdb")
data = cursor.fetchone()
print(data)
# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")
# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("Database version : %s " % data)

db.close()
