from tkinter import ttk #, messagebox
import tkinter as tk

def selection_changed(event):
    mertekegyseg_1 = combo.get()
    hany_index = int(mertekegyseg_valtoszam.index(mertekegyseg_1))
    valto_csomag_1 = [mertekegyseg_1, hany_index]


main_window = tk.Tk()
main_window.config(width=500, height=300)
main_window.title("Választék")
combo = ttk.Combobox(values=["gramm", "dekagramm", "kilogramm", "mázsa", "tonna"])
mertekegyseg_valtoszam = [1, 10, 1000, 100_000, 1000_000]
combo.bind(selection_changed)
combo.place(x=5, y=5)
main_window.mainloop()
