class student:
    stid=1
    stnm='Mitesh'

    def getdata(self):
        print("Student ID:",self.stid)
        print("Student Name:",self.stnm)
    
st=student()
st.getdata()