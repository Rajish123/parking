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

def get_record(catagory,registration):
    my_list = []
    sqlcommand = "SELECT * FROM parking_record WHERE (category,registration_num) = (%s,%s)" 
    mycursor.execute(sqlcommand,(catagory,registration, ))
    myresult = mycursor.fetchone()
    return myresult

def update_record(id,newcategory,newmodel,newregnum,newcolour):
    command="UPDATE parking_record SET category = %s,model=%s,registration_num=%s,colour=%s WHERE id=%s"
    value = (newcategory,newmodel,newregnum,newcolour,id)
    mycursor.execute(command,value)
    mydb.commit() 

# def update_record(model,new_model):
#     command = "UPDATE parking_record SET model = %s WHERE model = %s"
#     value = (new_model, model)
#     mycursor.execute(command, value)
#     mydb.commit()

# def update_record(model,reg_num,new_model,new_registration):
#     sqlcommand = "UPDATE parking_record SET (model,registration_num) = ('%s','%s') WHERE (model,registration_num) = ('%s','%s')"
#     value_to_set = ((new_model,new_registration, ),(model,reg_num, ))
#     # records_to_update = ()
#     mycursor.execute(sqlcommand,value_to_set)
#     # sqlcommand = "UPDATE parking_record SET category = , model = '{}',registration_num = {},colour = '{}' WHERE category = '{}',registration_num = {}".format(new_category,new_model,new_registration,new_colour,category,reg_num)
#     # mycursor.execute(sqlcommand)
#     mydb.commit()
#     print("Update successfull")

# def query(model):
#     sqlcommand = "SELECT * FROM parking_record WHERE (model) LIKE (%s)", ('%' + model + '%',)
#     mycursor.execute(sqlcommand)
#     result = mycursor.fetchall()
#     for i in result:
#         print(i)
    
