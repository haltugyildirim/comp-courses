from Tkinter import *
import tkMessageBox

def hypo():
    x=int(E1.get())
    y=int(E2.get())
    if (x>0 and y>0):
        a=str("Hypotenuse= ")+str((x**2+y**2)**(0.5))
        tkMessageBox.showinfo("Calculated Hypotenuse:",a)
    else:
        tkMessageBox.showinfo("Error!!","no triangle")

master=Tk()

w = Label(master, text="Calculate the Hypotenuse")
w.pack(side=TOP)


B=Button(master,text="Calculate",command = hypo)
B.pack(side=BOTTOM)

L1=Label(master, text="\n" "Enter x:" "\n" "\n" "Enter y: ")
L1.pack(side=LEFT)
E1=Entry(master, bd=5)
E1.pack(side=BOTTOM)
E2=Entry(master, bd=5)
E2.pack(side=BOTTOM)


master.mainloop()
