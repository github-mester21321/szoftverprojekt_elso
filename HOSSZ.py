# Import module 
from tkinter import *
  
# Create object 
root = Tk() 

# Adjust size 
root.geometry( "800x400" ) 
címsor = Label( root , text = "HOSSZ MÉRTÉKEGYSÉG ÁTVÁLTÓ ", width=200, bg="lightblue", borderwidth=10, font=('Comic Sans', 20, 'bold') ) 
címsor.pack() 
bemutatas = Label( root , text = "(Ezzel az alkalmazással mértékegységeket tud, tetszés szerint átváltani) ", width=200, bg="lightblue", borderwidth=3 ) 
bemutatas.pack()


# Change the label text 
def show(): 
    címsor.config( text = clicked.get() ) 
  
# Dropdown menu options 
options = [ 
    "Miliméter",
    "Centiméter",
    "Deciméter", 
    "Méter", 
    "Kilóméter"
] 
options2 = [ 
    "Miliméter",
    "Centiméter",
    "Deciméter", 
    "Méter", 
    "Kilóméter"
] 
  
# datatype of menu text 
clicked = StringVar() 
  
# initial menu text 
clicked.set( "Mértékegységek" ) 
  
# Create Dropdown menu 
atvaltani = Label(root, text="Írja ide az átváltani kívánt hosszt: ", width=150, font=('Times New Roman', 15, 'bold') )
atvaltani.pack()

e = Entry(root, width=50, borderwidth=2)
e.pack()

dropelso = OptionMenu( root , clicked , *options2 ) 
dropelso.pack()

megadottertek = e.get()
def szamolo():
    print(megadottertek)
    
szamolo()
    
 
def myClick():
    # a begépelt szöveg tartalma jelenik meg
    kiiras = e.get()
    myLabel = Label(root, text=kiiras)
    myLabel.pack()
    

atvalott = Label(root, text="Válassza ki azt a mértékegységet amibe átváltani szeretné:", width=150, font=('Times New Roman', 15, 'bold') )
atvalott.pack()


drop2 = OptionMenu( root , clicked , *options ) 
drop2.pack()

myButton = Button(root, text="Átváltás!", padx=40, pady=10,
                  command=myClick, fg="black", bg="lightblue")
myButton.pack()


atvalott = Label(root, text="Az Átváltott hossz: ", width=200, font=('Comic Sans', 15, 'bold') )
atvalott.pack()

# gomb -> Button() függvény, hova tesszük, mi a szöveg, padx=belső margó - vízszintes, pady=belső margó - függőleges, mi az állapota,pl state=DISABLED, eseményt társítani-zárójel nélkül!!, szöveg és háttérszín(HEX is)

  
# Execute tkinter 
root.mainloop() 