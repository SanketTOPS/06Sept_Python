try:
    a=int(input("Enter value of A:"))
    b=int(input("Enter value of B:"))
    print("Sum:",a+b)
except:
    print("Error!")
finally:
#else:
    print("This is finally block.")
    x=int(input("Enter value of A:"))
    y=int(input("Enter value of B:"))
    print("Mul:",x*y)