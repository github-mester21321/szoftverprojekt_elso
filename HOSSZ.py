
from tkinter import *

root = Tk()
root.title("Mértékegység átváltó")
root.geometry("700x700")
címsor = Label( root , text = "HOSSZ MÉRTÉKEGYSÉG ÁTVÁLTÓ ", width=200, bg="darkorange", borderwidth=10, font=('Comic Sans', 20, 'bold') ) 
címsor.pack()
bemutatas = Label( root , text = "(Ezzel az alkalmazással mértékegységeket tud, tetszés szerint átváltani) ", width=200, bg="darkorange", borderwidth=3 ) 
bemutatas.pack()
ertekiras = Label( root , text = "Ide írja a számot:", fg="darkorange",  font=('Comic Sans', 10, 'bold')) 
ertekiras.pack()
elsoleirasa = Label( root , text = "Válassza ki az első mértékegységet ", fg="darkorange",  font=('Comic Sans', 10, 'bold')) 

masodikleirasa = Label( root , text = "Válassza ki a második mértékegységet ",fg="darkorange", font=('Comic Sans', 10, 'bold') ) 



ertek = Entry(root, width=30, borderwidth=4)
ertek.pack()

mertekegysegek = ["Milliméter", "Centiméter", "Deciméter", "Méter", "Kilóméter"]
mertekegyseg_valtoszam = [["Milliméter", 1], ["Centiméter", 10], ["Deciméte", 100], ["Méter", 1000], ["Kilóméter", 100000]]

clicked = StringVar()
clicked.set(mertekegysegek[0])

legordulo1 = OptionMenu(root, clicked, *mertekegysegek)

clicked2 = StringVar()
clicked2.set(mertekegysegek[0])
legordulo2 = OptionMenu(root, clicked2, *mertekegysegek)


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
    veg_info = Label(root, text=f"{bekert_ertek} {mertekegysegek[index]} = {(bekert_ertek * valtoszam)} {mertekegysegek[index2]}").pack()


myButton = Button(root, text="Bevitel", command=bekeres, padx=40, pady=10, fg="black", bg="darkorange")
elsoleirasa.pack()
legordulo1.pack()
masodikleirasa.pack()
legordulo2.pack()

myButton.pack()

root.mainloop()