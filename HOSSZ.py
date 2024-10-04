# Import module 
from tkinter import *
  
# Create object 
root = Tk() 

# Adjust size 
root.geometry( "800x400" ) 
címsor = Label( root , text = "HOSSZ MÉRTÉKEGYSÉG ÁTVÁLTÓ ", width=200, bg="lightblue", borderwidth=30, font=('Times New Roman', 25, 'bold') ) 
címsor.pack() 
bemutatas = Label( root , text = "Ezzel az alkalmazással mértékegységeket tud, tetszés szerint átváltani ", width=200, bg="lightblue", borderwidth=6 ) 
bemutatas.pack()


# Change the label text 
def show(): 
    címsor.config( text = clicked.get() ) 
  
# Dropdown menu options 
options = [ 
    "inch",
    "yard",
    "méter", 
    "centiméter", 
    "kilóméter"
] 
  
# datatype of menu text 
clicked = StringVar() 
  
# initial menu text 
clicked.set( "Mértékegységek" ) 
  
# Create Dropdown menu 
atvaltani = Label(root, text="Írja ide az átváltani kívánt hosszt: ", width=150, font=('Times New Roman', 15, 'bold') )
atvaltani.pack()
drop1 = OptionMenu( root , clicked , *options ) 
drop1.pack() 

atvalott = Label(root, text="Az Átváltott hossz: ", width=150, font=('Times New Roman', 15, 'bold') )
atvalott.pack()
drop2 = OptionMenu( root , clicked , *options ) 
drop2.pack()

def myClick():
    # a begépelt szöveg tartalma jelenik meg
    hello = "Szia Dávid pro"
    myLabel = Label(root, text=hello)
    myLabel.pack()



# gomb -> Button() függvény, hova tesszük, mi a szöveg, padx=belső margó - vízszintes, pady=belső margó - függőleges, mi az állapota,pl state=DISABLED, eseményt társítani-zárójel nélkül!!, szöveg és háttérszín(HEX is)
myButton = Button(root, text="Átváltás!", padx=40, pady=10,
                  command=myClick, fg="black", bg="lightblue")

myButton.pack()

  
# Execute tkinter 
root.mainloop() 