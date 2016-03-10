from tkinter import *
from tkinter import ttk
from phash import *
import Image
from PIL import ImageTk
import tkinter as tk
import Image
import ImageTk

"""
To Do List:

	logo in top corner
	figure out how to do file select and set location as that
	
	
	figure out how to make button stick
	figure out how to do button click, double image pop up for comparison
		thatd be wicked sexy

"""


class tkGui:
    def __init__(self, root):

        root.title("p.h.i.s.t. Image Checker")
        root.minsize(width=900, height=600)
        root.maxsize(width=900, height=666)

        mainframe = ttk.Frame(root, padding="10 10 10 10")
        mainframe.grid(column=0, row=0, rowspan="3", columnspan="1", sticky=W + E + N + S)
        # mainframe.columnconfigure(0, weight=1)
        # mainframe.rowconfigure(0, weight=1)

        self.filePath = StringVar()
        self.Location = StringVar()
        self.image = StringVar()
        self.check = StringVar()
        self.match = StringVar()

        feet_entry = ttk.Entry(mainframe, width=10, textvariable=self.filePath)
        feet_entry.grid(column=2, row=1, sticky=(W, E))

        ttk.Button(mainframe, text="Check", command=self.checker).grid(column=4, row=1, sticky=(E, W))
        ttk.Label(mainframe, text="File Path").grid(column=1, row=1, sticky=W)
        ttk.Label(mainframe, textvariable=self.check).grid(column=5, row=10)
        """
        frame1 = Frame(root)



        # pick image files you have in your working directory
        # or use full path
        # PIL's ImageTk allows .gif  .jpg  .png  .bmp formats
        imageFile1 = "A.jpg"
        imageFile2 = "B.jpg"
        data1 = "A.jpg"
        data2 = "B.jpg"

        # PIL's ImageTk converts to an image object that Tkinter can handle
        self.image1 = ImageTk.PhotoImage(Image.open(imageFile1))
        self.image2 = ImageTk.PhotoImage(Image.open(imageFile2))

        # put the image objects on labels in a grid layout
        tk.Label(frame1,image=self.image1).grid(row=0, column=0)
        tk.Label(frame1,image=self.image2).grid(row=0, column=1)
        tk.Label(frame1,text=data1).grid(row=1, column=0)
        tk.Label(frame1,text=data2).grid(row=1, column=1)
        """
        for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

        feet_entry.focus()
        root.bind('<Return>', self.checker)

        root.mainloop()

    @staticmethod
    def imageDisplay(data):
        print(data)

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
tkGui(root)
