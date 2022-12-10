import tkinter
from tkinter import ttk,messagebox

screen=tkinter.Tk()
screen.title("FirstApp")
screen.geometry('500x500')
screen.config(bg="lightblue")

#tkinter.Label(text="Firstname:",bg='lightblue',font='Calibri 15 bold',fg="red").pack()
#tkinter.Label(text="Lastname:",bg='lightblue',font='Calibri 15 bold',fg="red").pack()

#tkinter.Label(text="Firstname:",bg='lightblue',font='Calibri 15 bold',fg="red").place(x=0,y=0)
#tkinter.Label(text="Lastname:",bg='lightblue',font='Calibri 15 bold',fg="red").place(x=0,y=30)

tkinter.Label(text="Firstname:",bg='lightblue',font='Calibri 15 bold',fg="red").grid(row=0,column=0,sticky='W')
tkinter.Label(text="Lastname:",bg='lightblue',font='Calibri 15 bold',fg="red").grid(row=1,column=0,sticky='W')

tkinter.Entry().grid(row=0,column=1,sticky='W')
tkinter.Entry().grid(row=1,column=1,sticky='W')

tkinter.Radiobutton(value=0,text="Male",bg='lightblue',font='Calibri 15 bold',fg="red").grid(row=2,column=0,sticky='W')
tkinter.Radiobutton(value=1,text="Female",bg='lightblue',font='Calibri 15 bold',fg="red").grid(row=2,column=1,sticky='W')

tkinter.Checkbutton(text="Python",bg='lightblue',font='Calibri 15 bold',fg="red").grid(row=3,column=0,sticky='W')
tkinter.Checkbutton(text="JAVA",bg='lightblue',font='Calibri 15 bold',fg="red").grid(row=4,column=0,sticky='W')
tkinter.Checkbutton(text="PHP",bg='lightblue',font='Calibri 15 bold',fg="red").grid(row=5,column=0,sticky='W')
tkinter.Checkbutton(text="iOS",bg='lightblue',font='Calibri 15 bold',fg="red").grid(row=6,column=0,sticky='W')

city=['Ahmedabad','Rajkot','Surat','Baroda','Jamnagar']
ttk.Combobox(values=city).grid(row=7,column=0)

def btnclick():
    #print("Button Clicked!")
    #messagebox.showerror("Error","Something went wrong...Try again!")
    #messagebox.showinfo("Success","Your data has been submitted!")
    messagebox.showwarning("Warning","Your disk is full!")

tkinter.Button(text='Submit',font='Calibri 15 bold',command=btnclick).place(x=210,y=300)

tkinter.mainloop()


