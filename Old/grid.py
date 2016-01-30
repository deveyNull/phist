from tkinter import *
from tkinter import *
from tkinter import ttk
from phash import *
from PIL import ImageTk
import tkinter as tk
import Image
import ImageTk


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.master.title("Grid Manager")

        self.filePath = StringVar()
        self.Location = StringVar()
        self.image = StringVar()
        self.check = StringVar()
        self.match = StringVar()

        Frame1 = Frame(master)
        Frame1.pack(fill=X)
        Frame2 = Frame(master)
        Frame2.pack(side=BOTTOM)

        ttk.Label(Frame1, text="File Path").pack(side=LEFT)

        filepath_entry = ttk.Entry(Frame1, width=10, textvariable=self.filePath)
        filepath_entry.pack(side=LEFT)
        ttk.Button(Frame1, text="Check", command=self.checker).pack(side=LEFT)

        Frame3 = Frame(Frame2)

        imageFile = "A.jpg"
        self.image1 = ImageTk.PhotoImage(Image.open(imageFile))

        Frame3.pack(side=TOP)
        panel1 = tk.Label(Frame3, image=self.image1)
        panel1.pack(side='left', fill='both', expand='yes')

        imageFile2 = "B.jpg"
        self.image2 = ImageTk.PhotoImage(Image.open(imageFile2))

        panel2 = tk.Label(Frame3, image=self.image2)
        panel2.pack(side='left', fill='both', expand='yes')

        ttk.Label(Frame2, textvariable=self.check).pack(side=BOTTOM)

    def checker(self, *args):
        value = str(self.filePath.get())
        devin = list(cImage(value, "hashes.txt"))
        x = ""
        for i in devin[2]:

            for j in i:
                x += j + " "
        x += "\n"
        self.check.set(x)


root = Tk()
app = Application(master=root)
app.mainloop()
