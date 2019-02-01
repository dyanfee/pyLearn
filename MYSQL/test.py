import pymysql

db = pymysql.connect("localhost", "root", "123456", "mt")

cursor = db.cursor()

# table = cursor.execute("SELECT * FROM mtdb")
# data = cursor.fetchone()
# print(data)
# 使用 execute()  方法执行 SQL 查询
# cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()

# print("Database version : %s " % data)

create_table_sql = """
CREATE TABLE `userinfo`(
`uid` INT unsigned auto_increment,
`username` varchar(20) not null,
`userid` INT not null,
`pwd` varchar(50) not null,
`date` DATE,
primary key(`uid`)
);
"""
insert_data_sql = """
insert into userinfo (userid,username,pwd,date)
values
(%s,%s,%s,NOW());
"""
data = ["33442", "freeme", "hehe22"]

delete_data_sql = """
delete from userinfo where uid = %s; 
"""
delete_data = ["4"]

result = cursor.execute(delete_data_sql, delete_data)
print(result)
db.commit()

cursor.close()
db.close()
