def getdata(id,name,sub='Python',city='Rajkot'):
    print("Student ID:",id)
    print("Student Name:",name)
    print("Student Subject:",sub)
    print("Student City:",city)

#getdata(101,'Sanket')
#getdata(101,'Nirav','iOS') #positional arguments

getdata(city='Baroda',id=101,name='Sanket') # keyword arguments
