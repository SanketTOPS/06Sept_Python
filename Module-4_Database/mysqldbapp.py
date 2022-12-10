import pymysql

try:
    dbcon=pymysql.connect(host='localhost',user='root',password='',database='06sepdb')
    print("Database connected!")
except Exception as e:
    print(e)

cur=dbcon.cursor()

# Create Table
create_tbl="create table studinfo(id int primary key auto_increment, name text, sub text)"
try:
    cur.execute(create_tbl)
    print("Table created!")
except Exception as e:
    print(e)
    

# Insert Data
"""insert_data="insert into studinfo (name,sub) values('mitesh','python'),('hitesh','java'),('sanket','iOS'),('ashok','php'),('mahesh','html')"

try:
    cur.execute(insert_data)
    dbcon.commit()
    print("Record inserted!")
except Exception as e:
    print(e)"""

# Update Data
"""update_data="update studinfo set sub='node' where id=5"
try:
    cur.execute(update_data)
    dbcon.commit()
    print("Record updated!")
except Exception as e:
    print(e)"""

# Delete Data
"""delete_data="delete from studinfo where id=2"
try:
    cur.execute(delete_data)
    dbcon.commit()
    print("Record deleted!")
except Exception as e:
    print(e)"""

# Select Data
select_data="select * from studinfo"
try:
    cur.execute(select_data)
    data=cur.fetchall()
    #data=cur.fetchmany(3)
    #data=cur.fetchone()
    #print(data)

    for i in data:
        print(i[1])
except Exception as e:
    print(e)


