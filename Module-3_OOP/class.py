class student:
    stid=1
    stnm='Nirav'

    def getdata(self):
        print("This is Getdata from Student.")

# Object
st=student()
print(st.stid)
print(st.stnm)
st.getdata()