#kiegeszito/bovitmeny importalasa
from tkinter import *


#a fo ablak letrehozasa
root = Tk()


#a cim megadasa/az ablak nevenek megadasa
root.title("Mértékegység átváltó")


#az ablak meretenek megadasa
root.geometry("700x700")


#a szam/szoveg bekeromezojenek letrehozasa es megjelenitese
ertek = Entry(root, width=30, borderwidth=4)
ertek.pack()


#az atvaltando adatok atvaltasahoz szukseges adatokat tartalmazo valtozok letrehozasa
felsorolas = ["gramm", "dekagramm", "kilogramm", "mázsa", "tonna"]
mertekegyseg_valtoszam = [["gramm", 1], ["dekagramm", 10], ["kilogramm", 1000], ["mázsa", 100000], ["tonna", 1000000]]

#dropdown menu 1
clicked = StringVar()
clicked.set(felsorolas[0])
drop = OptionMenu(root, clicked, *felsorolas)


#dropdown menu 2
clicked2 = StringVar()
clicked2.set(felsorolas[0])
drop2 = OptionMenu(root, clicked2, *felsorolas)




#adatbekero fuggveny (mertekegysegek, atvaltando szam)
def bekeres():
    #a beolvasott ertek megszerzese es vizsgalata
    bekert_ertek = ertek.get()
    try:
        if float(bekert_ertek) % 1 == 0:
            bekert_ertek = int(bekert_ertek)
    except:
        bekert_ertek = "Nem jól adtad meg a számot."
    

    #proba kiiratas
    mertekegyseg_szoveg = clicked.get()
    mertekegyseg_szoveg2 = clicked2.get()
    # print(bekert_ertek, mertekegyseg_szoveg)


    #az indexek kikeresese
    for i in range(len(felsorolas)):
        if felsorolas[i] == mertekegyseg_szoveg:
            index = i

    for i in range(len(felsorolas)):
        if felsorolas[i] == mertekegyseg_szoveg2:
            index2 = i


    #index ellenorzese
    # print(index, index2)
            

    # a valtoszam letrehizasa es ellenorzees
    valtoszam = float(mertekegyseg_valtoszam[index][1] / mertekegyseg_valtoszam[index2][1])
    # print(valtoszam)


    #a vegeredmeny kiirasa
    veglegesKiiratas = Label(root, text=f"Az átváltás eredménye: {bekert_ertek} {felsorolas[index]} = {(bekert_ertek * valtoszam)} {felsorolas[index2]}").pack()
    # #a kiirando ertekek kiiratasa egyesevel az ellenorzes miatt
    # myLabel = Label(root, text=bekert_ertek).pack()
    # myLabel2 = Label(root, text=clicked.get()).pack() #ez a verzió (.pack()) a parancs végén ugyanaz mintha külön sorban odaírnáh, hogy myLabel.pack()
    # myLabel3 = Label(root, text=clicked2.get()).pack() #ez a verzió (.pack()) a parancs végén ugyanaz mintha külön sorban odaírnáh, hogy myLabel.pack()
    # mykiiratas = Label(root, text=bekert_ertek * valtoszam).pack()


#a bekeres gomb letrehozasa
myButton = Button(root, text="Bevitel", command=bekeres)


# kicsomagolás, kibontás, kiiratás
#a ket legordulo menu megjelenitese
drop.pack()
drop2.pack()


#a gomb megjelenitese
myButton.pack()


#a fo ablak megjelenitese
root.mainloop()