##############################################################
##File Name: Dog Age Calculator                             ##
##File Type: Python 3                                       ##
##                                                          ##
##Author: Joseph Brown                                      ##
##Project Type: Independent Project                         ##
##Creation Date: 28 May 2021                                ##
##Last Modification Date:                                   ##
##                                                          ##
##Description:                                              ##
##A Calculator made for helping create a Dog's Age          ##
##                                                          ##
##Version: 2.0                                              ##
##                                                          ##
##Version History:                                          ##
## 2.0 - Changed to a Basic Graphical Interface             ##
##1.2 - Made the Program More User Friendly                 ##
##1.11 - Tidied Up Sleeps and Added More to the Results     ##
##1.1 - Added Use of Sleep to Make Program Last for Longer  ##
##1.0 - Basic Calculations of the Age using Input Variables ## 
##############################################################

#Imports
import tkinter
import os
from tkinter.constants import BOTTOM

##Version 2 Code##

#Application
name_window = tkinter.Tk()
name_window.title("Dog Calculator")
name_window.geometry("400x350")
name_window.columnconfigure(0, weight=1)
name_window.columnconfigure(1, weight=1)
name_window.columnconfigure(2, weight=1)

#Variables
name_var = tkinter.StringVar()
age_var = tkinter.StringVar()

#Functions
def donothing():
    filewin = tkinter.Toplevel()
    button = tkinter.Button(filewin, text="Do Nothing Button")
    button.pack()

def program_info():
    sysinfo = tkinter.Toplevel()
    sysinfo.title("Dog Calculator - Program Info")
    sysinfo.geometry("400x100")
    info_name = tkinter.Label(sysinfo, text="Dog Calculator")
    info_name.pack()
    info_ver = tkinter.Label(sysinfo, text="Version 2.0")
    info_ver.pack()
    info_auth = tkinter.Label(sysinfo, text="By Joseph Brown")
    info_auth.pack()
    info_exit = tkinter.Button(sysinfo, text="Close", command=sysinfo.destroy)
    info_exit.pack()

def name_submit():
    dog_name = name_var.get()
    name_var.set("")
    print(dog_name)

def age_submit():
    age = age_var.get()
    age_var.set("")
    print(age)

#Application Menu
menubar = tkinter.Menu()
filemenu = tkinter.Menu(menubar, tearoff=0)
filemenu.add_command(label="Restart", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = tkinter.Menu(menubar, tearoff=0)
helpmenu.add_command(label="Options", command=donothing)
helpmenu.add_command(label="Program Help", command=donothing)

helpmenu.add_separator()

helpmenu.add_command(label="Program Info", command=program_info)
menubar.add_cascade(label="Help", menu=helpmenu)

#Application Workings
dog_name_entry = tkinter.Label(text="What is Your Dog's Name? ")
dog_name_entry2 = tkinter.Entry(textvariable=name_var)
dog_name_entry_button = tkinter.Button(text="Submit", width=10, height=2, background="White", command=name_submit)

age_entry = tkinter.Label(text="What is Your Dog's Age in Human Years? ")
age_entry2 = tkinter.Entry(textvariable=age_var)
age_entry_button = tkinter.Button(text="Submit", width=10, height=2, background="White", command=age_submit)

result = tkinter.Label(text = "Your Dog: ")
result_name = tkinter.Label(text="DogName")
result2 = tkinter.Label(text = "Is: ")
result2_name = tkinter.Label(text="Age")
result3 = tkinter.Label(text="That's: ")
result3_age = tkinter.Label(text="DogAge")
result3_final = tkinter.Label(text=" In Dog Years!")

dog_name_entry.grid(column=1, row=0)
dog_name_entry2.grid(column=1, row=1)
dog_name_entry_button.grid(column=1, row=2)

space1 = tkinter.Label(text=" ")
space1.grid(column=1, row=3)
space2 = tkinter.Label(text=" ")
space2.grid(column=1, row=4)

age_entry.grid(column=1, row=5)
age_entry2.grid(column=1, row=6)
age_entry_button.grid(column=1, row=7)

space = tkinter.Label(text=" ")
space.grid(column=1, row=8)
space1 = tkinter.Label(text=" ")
space1.grid(column=1, row=9)

result.grid(column=0, row=10)
result_name.grid(column=0, row=11)
result2.grid(column=1, row=10)
result2_name.grid(column=1, row=11)
result3.grid(column=2, row=10)
result3_age.grid(column=2, row=11)
result3_final.grid(column=2, row=12)

#Packing Overall Application
name_window.config(menu=menubar)
name_window.mainloop()

