import sqlite3

try:
    dbcon=sqlite3.connect('mydb.db')
    print("Database connected!")
except Exception as e:
    print(e)

# Create Table
create_tbl="create table studinfo (id integer primary key autoincrement, name text, sub text, city text)"
try:
    dbcon.execute(create_tbl)
    print("Table created!")
except Exception as e:
    print(e)

# Insert data
"""insert_data="insert into studinfo (name,sub,city) values ('sanket','python','rajkot'),('mitesh','php','baroda'),('nirav','java','surat'),('hitesh','html','rajkot'),('ashok','react','ahmedabad')"
try:
    dbcon.execute(insert_data)
    dbcon.commit()
    print("Record inserted!")
except Exception as e:
    print(e)
"""

# Update data
"""update_data="update studinfo set city='navsari' where name='ashok'"
try:
    dbcon.execute(update_data)
    dbcon.commit()
    print("Record updated!")
except Exception as e:
    print(e)"""

# Delete data
"""delete_data="delete from studinfo where id=9"
try:
    dbcon.execute(delete_data)
    dbcon.commit()
    print("Record deleted!")
except Exception as e:
    print(e)"""

# Select data

cur=dbcon.cursor()
select_data="select * from studinfo"
try: 
    cur.execute(select_data)
    data=cur.fetchall()
    #data=cur.fetchmany(5)
    #data=cur.fetchone()
    #print(data)

    for i in data:
        print(i[3])

except Exception as e:
    print(e)