from tkinter import *
from tkinter import ttk
from phash import *
import Image

"""
To Do List:

	logo in top corner
	figure out how to make button stick
	figure out how to do button click, double image pop up for comparison
		thatd be wicked sexy

"""


class tkGui:
    def __init__(self, root):

        root.title("p.h.i.s.t. Directory Checker")
        root.minsize(width=900, height=600)
        root.maxsize(width=900, height=666)

        mainframe = ttk.Frame(root, padding="10 10 10 10")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)

        self.dirPath = StringVar()
        self.Location = StringVar()
        self.image = StringVar()
        self.check = StringVar()
        self.match = StringVar()

        feet_entry = ttk.Entry(mainframe, width=10, textvariable=self.dirPath)
        feet_entry.grid(column=2, row=1, sticky=(W, E))

        ttk.Button(mainframe, text="Check", command=self.checker).grid(column=4, row=1, sticky=(E, W))
        ttk.Label(mainframe, text="Directory Path").grid(column=1, row=1, sticky=W)
        ttk.Label(mainframe, textvariable=self.check).grid(column=1, row=100)

        for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

        feet_entry.focus()
        root.bind('<Return>', self.checker)

        root.mainloop()

    def checker(self, *args):

        value = str(self.dirPath.get())
        # print(value)
        devin = list(cDirectory(value, "hashes.txt"))

        x = ""
        for i in devin:
            x += i[0] + ":\t" + str(i[1][1]) + "\t"
            for j in i[1][2]:
                for k in j:
                    x += str(k) + "  "
            x += "\n\n"
        self.check.set(x)


root = Tk()
tkGui(root)
