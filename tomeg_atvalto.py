from tkinter import *

root = Tk()
root.title("Választék")

ertek = Entry(root, width=30, borderwidth=4)
ertek.pack()

#valtozok letrehozasa
felsorolas = ["gramm", "dekagramm", "kilogramm", "mázsa", "tonna"]
mertekegyseg_valtoszam = [["gramm", 1], ["dekagramm", 10], ["kilogramm", 1000], ["mázsa", 100000], ["tonna", 1000000]]

#dropdown menu
clicked = StringVar()
# clicked.set(felsorolas[0])
drop = OptionMenu(root, clicked, *felsorolas)


def bekeres():
    bekert_ertek = ertek.get()
    # myLabel = Label(root, text=bekert_ertek)
    # myLabel.pack()
    if float(bekert_ertek) % 1 == 0:
        bekert_ertek = int(bekert_ertek)
    else:
        bekert_ertek = "Nem jól adtad meg a számot."
    
    myLabel = Label(root, text=bekert_ertek).pack()
    myLabel2 = Label(root, text=clicked.get()).pack() #ez a verzió (.pack()) a parancs végén ugyanaz mintha külön sorban odaírnáh, hogy myLabel.pack()



myButton = Button(root, text="Bevitel",command=bekeres)

# kicsomagolás, kibontás, kiiratás
drop.pack()
myButton.pack()

root.mainloop()
