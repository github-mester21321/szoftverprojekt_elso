from tkinter import *

root = Tk()
root.title("Mértékegység átváltó")
root.geometry("700x700")

ertek = Entry(root, width=30, borderwidth=4)
ertek.pack()


#valtozok letrehozasa
felsorolas = ["gramm", "dekagramm", "kilogramm", "mázsa", "tonna"]
mertekegyseg_valtoszam = [["gramm", 1], ["dekagramm", 10], ["kilogramm", 1000], ["mázsa", 100000], ["tonna", 1000000]]

#dropdown menu
clicked = StringVar()
clicked2 = StringVar()
clicked.set(felsorolas[0])
clicked2.set(felsorolas[0])
drop = OptionMenu(root, clicked, *felsorolas)
drop2 = OptionMenu(root, clicked2, *felsorolas)





def bekeres():
    bekert_ertek = ertek.get()
    # myLabel = Label(root, text=bekert_ertek)
    # myLabel.pack()
    try:
        if float(bekert_ertek) % 1 == 0:
            bekert_ertek = int(bekert_ertek)
    except:
        bekert_ertek = "Nem jól adtad meg a számot."
    
    myLabel = Label(root, text=bekert_ertek).pack()
    myLabel2 = Label(root, text=clicked.get()).pack() #ez a verzió (.pack()) a parancs végén ugyanaz mintha külön sorban odaírnáh, hogy myLabel.pack()
    myLabel3 = Label(root, text=clicked2.get()).pack() #ez a verzió (.pack()) a parancs végén ugyanaz mintha külön sorban odaírnáh, hogy myLabel.pack()

    #proba kiiratas
    mertekegyseg_szoveg = clicked.get()
    mertekegyseg_szoveg2 = clicked2.get()
    # print(bekert_ertek, mertekegyseg_szoveg)

    index = 0
    index2 = 0

    for i in range(len(felsorolas)):
        if felsorolas[i] == mertekegyseg_szoveg:
            index = i

    for i in range(len(felsorolas)):
        if felsorolas[i] == mertekegyseg_szoveg2:
            index2 = i

    #index ellenorzese
    # print(index)
            
    valto_csomag = [index, bekert_ertek, index2]
    vegeredmeny = []

    valtoszam = int(mertekegyseg_valtoszam[index][1] / mertekegyseg_valtoszam[index2][1])

    print(valtoszam)

    mykiiratas = Label(bekert_ertek * valtoszam).pack()




myButton = Button(root, text="Bevitel", command=bekeres)

# kicsomagolás, kibontás, kiiratás
# drop.grid(row=1, )
# drop2.grid(row=4, )
drop.pack()
drop2.pack()
myButton.pack()

root.mainloop()