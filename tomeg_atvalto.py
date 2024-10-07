#kiegeszito/bovitmeny importalasa
from tkinter import *


def mainFunction():
    #a fo ablak letrehozasa
    root = Tk()


    #a cim megadasa/az ablak nevenek megadasa
    root.title("Tömeg átváltó")


    #az ablak meretenek megadasa
    root.geometry("300x350")


    #a szam/szoveg bekeromezojenek letrehozasa es megjelenitese
    ertek = Entry(root, width=30, borderwidth=4)
    # ertek.grid(row= 0, column=1)
    ertek.place(relx=0.5, y=15, anchor=CENTER)


    #az atvaltando adatok atvaltasahoz szukseges adatokat tartalmazo valtozok letrehozasa
    felsorolas = ["gramm", "dekagramm", "kilogramm", "mázsa", "tonna"]
    mertekegyseg_valtoszam = [["gramm", 1], ["dekagramm", 10], ["kilogramm", 1000], ["mázsa", 100000], ["tonna", 1000000]]

    #dropdown menu 1
    clicked = StringVar()
    clicked.set("---------")
    drop = OptionMenu(root, clicked, *felsorolas)


    #dropdown menu 2
    clicked2 = StringVar()
    clicked2.set("---------")
    drop2 = OptionMenu(root, clicked2, *felsorolas)


    #adatbekero fuggveny (mertekegysegek, atvaltando szam)
    def bekeres():
        #a beolvasott ertek megszerzese es vizsgalata
        bekert_ertek = ertek.get()
        try:
            bekert_ertek = float(bekert_ertek)
            
            
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
            veglegesKiiratas = Label(root, text=f"Az átváltás eredménye:\n {bekert_ertek} {felsorolas[index]} = {(bekert_ertek * valtoszam)} {felsorolas[index2]}", font=("Rubik", 10, "bold")).place(relx=0.5, y=120, anchor=CENTER)
        except:
            szoveg = Label(root, text="Nem jól adtad meg a számot.", font=("Rubik", 16, "bold")).place(relx=0.5, y=121, anchor=CENTER)
            root.after(2000, lambda:root.destroy())
        

    #a bekeres gomb letrehozasa
    myButton = Button(root, text="Bevitel", fg="white", bg="green", font="sans 10 bold", command=bekeres)


    # # kicsomagolás, kibontás, kiiratás
    # #a ket legordulo menu megjelenitese
    forrasertek = Label(root, text="Forrásérték:", font="Rubik 10 bold").place(relx=0.2, y=50, anchor=CENTER) 
    celertek = Label(root, text="Célérték:", font="Rubik 10 bold").place(relx=0.8, y=50, anchor=CENTER) 
    drop.place(relx=0.2, y=80, anchor=CENTER)
    drop2.place(relx=0.80, y=80, anchor=CENTER)


    #a gomb megjelenitese
    myButton.place(relx=0.5, y=80, anchor=CENTER)


    #Bezaro gomb
    gomb = Button(root, text="Bezárás", fg="white", bg="red", font="sans 10 bold", command=root.destroy).place(relx=0.5, y=334, anchor=CENTER) 
    

    #a fo ablak megjelenitese
    root.mainloop()


#fuggveny meghivasa ami a futtatas miatt kell
# mainFunction()