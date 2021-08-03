import pymysql

mydb = pymysql.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "parkingrecord"
    )

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE parking_recordsdb")

# print(mydb)

# mycursor.execute("""CREATE TABLE parking_record(
#             id int AUTO_INCREMENT primary key,
#             category varchar(100) NOT NULL,
#             model varchar(100) NOT NULL,
#             registration_num int NOT NULL,
#             colour varchar(100),
#             parking_slot int NOT NULL,
#             date_time varchar(50) NOT NULL
#             )""")

# mydb.commit()
# mydb.close()

# mycursor.execute("SHOW TABLES")
# for db in mycursor:

# mycursor.execute("ALTER TABLE parking_record DROP parked_date")
#     print(db)

# sqlcommand = "DROP TABLE parking_records"
# mycursor.execute(sqlcommand)

def add_record(category,model,registration,colour,slot,date_time):
    sqlcommand = "INSERT INTO parking_record (category,model,registration_num,colour,parking_slot,date_time) values (%s,%s,%s,%s,%s,%s)"
    data = (category,model,registration,colour,slot,date_time)
    mycursor.execute(sqlcommand,data)
    mydb.commit()

def get_record(registration):
    my_list = []
    sqlcommand = "SELECT * FROM parking_record WHERE registration_num = %s" 
    mycursor.execute(sqlcommand,(registration, ))
    myresult = mycursor.fetchone()
    return myresult

def update_record(id,newcategory,newmodel,newregnum,newcolour):
    command="UPDATE parking_record SET category = %s,model=%s,registration_num=%s,colour=%s WHERE id=%s"
    value = (newcategory,newmodel,newregnum,newcolour,id)
    mycursor.execute(command,value)
    mydb.commit() 

def query(model):
    param = '{}%'.format(model)
    sqlcommand = "SELECT * FROM parking_record WHERE model like %s ORDER BY date_time"
    mycursor.execute(sqlcommand,(param, ))
    result = mycursor.fetchall()
    for i in result:
        print(i)

def delete_record(id,reg_num):
    sqlcommand = "DELETE FROM parking_record where (id,registration_num) = (%s,%s)"
    value = (id,reg_num, )
    mycursor.execute(sqlcommand,value)
    mydb.commit()