
from tkinter import *

root = Tk()
#Ablak címe
root.title("Mértékegység átváltó")

#Címsor
címsor = Label( root , text = "HOSSZ MÉRTÉKEGYSÉG ÁTVÁLTÓ ",  fg="blue", borderwidth=10, font=('Comic Sans', 26, 'bold') ) 
címsor.grid(row=0, column=0, columnspan=2, pady=10)

#Bemutató szöveg
bemutatas = Label( root , text = "(Ezzel az alkalmazással mértékegységeket tud, tetszés szerint átváltani) ", borderwidth=5,  font=('Comic Sans', 10, 'bold')) 
bemutatas.grid(row=1, column=0, columnspan=2, pady=5)

#Megmutatja hová kell írni a számot
ertekiras = Label( root , text = "Ide írja a számot:", bg="blue", fg="white", borderwidth=5,  font=('Comic Sans', 13, 'bold')) 
ertekiras.grid(row=2, column=0, padx=7, pady=10)

#Mértékegységek kiválasztására figyelem felhívó szöveg
elsoleirasa = Label( root , text = "Válassza ki az első mértékegységet ", bg="blue",fg="white", borderwidth=5,  font=('Comic Sans', 10, 'bold')) 

masodikleirasa = Label( root , text = "Válassza ki a második mértékegységet ",bg="blue",fg="white", borderwidth=5, font=('Comic Sans', 10, 'bold') ) 


#bekeres
ertek = Entry(root, width=30, borderwidth=4)
ertek.grid(row=2, column=1, padx=10, pady=10)

#Mertekegysegek felvétele + listában átváltóérték tárolása
mertekegysegek = ["Milliméter", "Centiméter", "Deciméter", "Méter", "Kilóméter"]
mertekegyseg_valtoszam = [["Milliméter", 1], ["Centiméter", 10], ["Deciméte", 100], ["Méter", 1000], ["Kilóméter", 1000000]]

#Hozzárendelni az első legördűlő menün kiválasztott mértékegységet az értékhez
clicked = StringVar()
clicked.set(mertekegysegek[0])

legordulo1 = OptionMenu(root, clicked, *mertekegysegek)

#Hozzárendelni az második legördűlő menün kiválasztott mértékegységet az átváltáshoz
clicked2 = StringVar()
clicked2.set(mertekegysegek[0])
legordulo2 = OptionMenu(root, clicked2, *mertekegysegek)

#Bekeres
def bekeres():
    bekert_ertek = ertek.get()
    bekert_ertek = int(bekert_ertek)


    mertekegyseg_elso = clicked.get()
    mertekegyseg_masodik = clicked2.get()

    for i in range(len(mertekegysegek)):
        if mertekegysegek[i] == mertekegyseg_elso:
            index = i

    for i in range(len(mertekegysegek)):
        if mertekegysegek[i] == mertekegyseg_masodik:
            index2 = i

    valtoszam = float(mertekegyseg_valtoszam[index][1] / mertekegyseg_valtoszam[index2][1])
    veg_info = Label(root, text=f"Az átváltott érték: {bekert_ertek} {mertekegysegek[index]} = {(bekert_ertek * valtoszam)} {mertekegysegek[index2]}",font=('Comic Sans', 14, 'bold')).grid(row=6, column=0, columnspan=2, pady=20)


#Meghívások, Gomb az átváltáshoz, leírások a felhasználó könnyebb tájékozódásához 
myButton = Button(root, text="Bevitel", command=bekeres, padx=40, pady=10, fg="white", bg="blue")
elsoleirasa.grid(row=3, column=0, padx=10, pady=10)
legordulo1.grid(row=3, column=1, padx=10, pady=10)
masodikleirasa.grid(row=4, column=0, padx=10, pady=10)
legordulo2.grid(row=4, column=1, padx=10, pady=10)

#Végeredmény kiiratása!
myButton.grid(row=5, column=0, columnspan=2, pady=20)

root.mainloop()