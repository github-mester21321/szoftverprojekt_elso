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
    címsor.config( text = clicked1.get() ) 
  
# Dropdown menu options
clicked1 = StringVar() 
clicked2 = StringVar()
mertekegysegek = ["Miliméter","Centiméter","Deciméter","Méter", "Kilóméter"]
clicked1.set(mertekegysegek[0])
clicked2.set(mertekegysegek[0]) 
dropelso = OptionMenu( root , clicked1 , *mertekegysegek )  
drop2 = OptionMenu( root , clicked2 , *mertekegysegek ) 
  
# datatype of menu text 

  
# initial menu text 
clicked1.set( "Mértékegységek1" ) 
clicked2.set( "Mértékegységek2" ) 
# datatype of menu text 
clickedit = StringVar() 
clickedit = StringVar()

  
# initial menu text 


  
# Create Dropdown menu 
atvaltani = Label(root, text="Írja ide az átváltani kívánt hosszt: ", width=150, font=('Times New Roman', 15, 'bold') )
atvaltani.pack()

e = Entry(root, width=50, borderwidth=2)
e.pack()




atvaltok = [0.0001,  0.01  ,0.1  ,1  ,1000  ]

dropelso.pack()


# def szamolo():
#     vegsoosszeg = 0
#     egyseg = dropelso.pack()
#     for i in mertekegysegek:
#         if 
       
    
# szamolo():


masodik = clicked1.get()

egyseg = drop2
def myClick():
    # a begépelt szöveg tartalma jelenik meg
    myLabel = Label(root, text=e.get()).pack()
    mymertekegyseg = Label(root, text=masodik).pack()
    
    

atvalott = Label(root, text="Válassza ki azt a mértékegységet amibe átváltani szeretné:", width=150, font=('Times New Roman', 15, 'bold') )
atvalott.pack()




drop2.pack()

atvalto = Button(root, text="Átváltás!", padx=40, pady=10,
                  command=myClick, fg="black", bg="lightblue")
atvalto.pack()


atvalott = Label(root, text="Az Átváltott hossz: ", width=200, font=('Comic Sans', 15, 'bold') )
atvalott.pack()

# gomb -> Button() függvény, hova tesszük, mi a szöveg, padx=belső margó - vízszintes, pady=belső margó - függőleges, mi az állapota,pl state=DISABLED, eseményt társítani-zárójel nélkül!!, szöveg és háttérszín(HEX is)

  
# Execute tkinter 
root.mainloop() 