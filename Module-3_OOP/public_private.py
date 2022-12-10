class student:
    __stid=23
    __stnm='Nirav'

    def __getdata(self,sub):
        print("Subject:",sub)
        print("Student ID:",st.__stid)
        print("Student Name:",st.__stnm)
    
    def alldata(self):
        self.__getdata("Python")


st=student()
#st.getdata('Python')
st.alldata()