# _*_ coding：utf-8 _*_
# @Author   :cjj
# @time		:2018/6/27 14:10
# @File 	:Mysql.py
# @Software :PyCharm

import pymysql

# connection 用于数据库连接，获取数据库对象，cursor，数据库交互对象，exception数据库异常类

# 流程：创建connection,创建数据库连接对象，然后调用cursor方法，返回cursor对象，对数据库进行操作，cursor调用##方法，
#       执行命令，获取数据处理出数据，然后关闭cursor，关闭cnnection（否则占用资源）,结束。

# connection对象的方法：cursor()：使用该链接并返回游标，commit()提交当前事务,rollback()回滚当前事务，##close()关闭连接 。

# 游标对象，由于执行查询和获取结果。excute(),执行数据库查询和命令，将数据库语句送到数据库执行，
# 数据库将对象返回客户端缓冲池。fetchone()去的结果集的下一行。##fetchmany(size)获取结果集的下几行，
# fetchall()：获取结果##集中的剩下所有行,rowcount()：最近一次execute返回数##据的行数或者影响的行数。close()：
# 关闭是游标对象。##fetch*()方法，通过rownumber指针返回数据，比如开始时候，rownumber=0，
# 调用fetchone，ruwnumber+1,返回第一条数据。

conn = pymysql.Connect(
    host='192.168.6.71',   # mysql服务器地址
    port=3306,  # mysql服务器端口号
    user='root',    # 用户名
    passwd='NvGHHsQvo3!90YS@',  ##密码
    db='dezzal_db',    # 数据库名
    charset='utf8'  # 连接编码
     )

# 获取游标
cursor = conn.cursor()
print(conn)
print(cursor)

# TODO 　1、从数据库中查询
# sql="INSERT INTO login(user_name,pass_word)"
sql = "SELECT *  FROM  eload_admin_department WHERE department_id='40';"
# cursor执行sql语句
cursor.execute(sql)
# 打印执行结果的条数
print(cursor.rowcount)
# 将所有的结果放入rr中,遍历集合
rr = cursor.fetchall()
for row in rr:
    print(row)

# TODO　2、修改数据库中的内容
sql_update = "UPDATE eload_admin_department SET de_name='hello22 dezzal' WHERE department_id=40"
print(sql_update)
cursor.execute(sql_update)
conn.commit()
# print("SELECT *  FROM  eload_admin_department WHERE department_id='40';".format())

# TODO  3、删除数据库中的内容，并利用try catch语句进行事务回滚
try:
    sql_delete = "DELETE FROM eload_admin_department WHERE department_id=50"
    cursor.execute(sql_delete)
    conn.commit()
except Exception as e:
    print(e)
    # 事务回滚，即出现错误后，不会继续执行，而是回到程序未执行的状态，原先执行的也不算了
    conn.rollback()

# TODO  4、数据库中插入数据
sql_insert = "INSERT INTO eload_affilate_stat VALUES ('3','50.20','600')"
cursor.execute(sql_insert)
# 事务提交，否则数据库得不到更新
conn.commit()
print(cursor.rowcount)
print()


# 数据库连接和游标的关闭
# conn.close()
# cursor.close()




