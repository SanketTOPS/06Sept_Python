class father:
    car=0
    bal=0

    def getdata(self):
        self.car=input("Enter car details:")
        self.bal=input("Enter bank balance details:")

class son(father):
    def printdata(self):
        print("Car:",self.car)
        print("Bank Balance:",self.bal)

# Object
sn=son()
sn.getdata()
sn.printdata()
