'''
import Tkinter as tk
import time

def update_timeText():
    # Get the current time, note you can change the format as you wish
    current = time.strftime("%H:%M:%S")
    # Update the timeText Label box with the current time 
    timeText.configure(text=current)
    # Call the update_timeText() function after 1 second
    root.after(1000, update_timeText)

root = tk.Tk()
root.wm_title("Simple Clock Example")

#Create a timeText Label (a text box)
timeText=tk.Label(root, text="", font=("Helvetica", 150))
timeText.pack()
update_timeText()
root.mainloop()
'''

from Tkinter import *
from random import random

def montecarlo():
    all=int(E1.get()) #string to integer
    inside=0
    for i in range(all):
        x,y=random(),random()
        if(x**2+y**2)**(0.5)<1:inside=inside+1
    mypi=4.0*(float(inside)/all)
    print("The value of pi for %d points is %f"%(all,mypi))

top = Tk()
L1=Label(top, text="Number of point")
L1.pack(side=LEFT)
E1=Entry(top, bd=5)
E1.pack(side=LEFT)
B1=Button(top,text="FIND MY PI", width=10, command=montecarlo)
B1.pack(side=RIGHT)
mainloop()
