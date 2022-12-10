class student:
    def getdata(self,id,name):
        print("ID:",id)
        print("Name:",name)

class othetstudent(student):
    def getdata(self, id, name):
        return super().getdata(id, name)

st=student()
st.getdata(1,'Sanket')

ot=othetstudent()
ot.getdata(2,'Mitesh')

