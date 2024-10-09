# This will import all the widgets and modules which are available in
# tkinter and ttk module
from tkinter import *
# from tkinter.ttk import * # tkinter and ttk module
import tomeg_atvalto
import HOSSZ


master = Tk()


# sets the geometry and the title of the main root window
master.geometry("288x200")
master.title("Főoldal")


# function to open a new window 
# on a button click
def openNewWindow():
    tomeg_atvalto.mainFunction()
    
    
def openNewWindow2():
    HOSSZ.foFuggveny()


label = Label(master, text ="Válaszd ki, hogy melyik átváltót szeretnéd használni!").grid(row= 0, columnspan=3, pady=10, padx=5)


# a button widget which will open a 
# new window on button click
btn = Button(master, text ="Tömeg átváltó", fg="white", bg="green", font="sans 10 bold", command = openNewWindow).grid(row= 1, column=0)
btn2 = Button(master, text ="Hossz átváltó", fg="white", bg="green", font="sans 10 bold", command = openNewWindow2).grid(row= 1, column=2)


#quit button
bezaro_gomb = Button(master, text="Bezárás", fg="white", bg="red", font="sans 10 bold", command=master.destroy).grid(row=1, column=1)


# mainloop, runs infinitely
mainloop()