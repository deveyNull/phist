from tkinter import ttk

import Tkinter as Tk
from Tkinter import *

from phash import *
# from phash import *
from PIL import ImageTk
import tkFileDialog
import Image
import ImageTk


########################################################################
class OtherFrame(Tk.Toplevel):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self, name, data):
        """Constructor"""
        Tk.Toplevel.__init__(self)
        # self.geometry("400x300")
        self.title("Image Comparison")
        self.center_window(1000, 600)
        Frame3 = Frame(self)

        data0 = data[0]
        data1 = data[1]
        Frame4 = Frame(self)

        Frame3.pack(side=LEFT)
        Frame4.pack(side=LEFT)

        imageFile = name
        self.image1 = ImageTk.PhotoImage(Image.open(imageFile))
        panel1 = Tk.Label(Frame3, image=self.image1)
        panel1.pack(side=TOP, fill='both', expand='yes')
        Tk.Label(Frame3, text=data0).pack(side=BOTTOM)

        imageFile2 = data[1][0]
        self.image2 = ImageTk.PhotoImage(Image.open(imageFile2))
        panel2 = Tk.Label(Frame4, image=self.image2)
        panel2.pack(side=TOP, fill='both', expand='yes')
        Tk.Label(Frame4, text=data1).pack(side=BOTTOM)

    def center_window(self, width=300, height=200):
        # get screen width and height
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # calculate position x and y coordinates
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.geometry('%dx%d+%d+%d' % (width, height, x, y))


########################################################################
class MyApp(object):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self, parent):
        """Constructor"""
        self.root = parent
        self.root.title("p.h.i.s.t. Image Checker")
        self.center_window(500, 400)
        self.frame = Tk.Frame(parent)
        self.frame2 = Tk.Frame(parent)
        self.frame.pack(side=TOP, padx=5, pady=15)
        self.frame2.pack(side=TOP, padx=5, pady=15)
        # mainframe = ttk.Frame(root, padding="10 10 10 10")
        # mainframe.grid(column=0, row=0, rowspan = "3", columnspan = "1", sticky = W+E+N+S)
        # mainframe.columnconfigure(0, weight=1)
        # mainframe.rowconfigure(0, weight=1)
        self.dirPath = StringVar()
        self.Location = StringVar()
        self.image = StringVar()
        self.check = []
        self.match = StringVar()
        self.checker = StringVar()
        self.flag = 0
        self.buttonDisplay = StringVar()
        self.dir_opt = options = {}
        options['initialdir'] = 'C:\\'
        options['mustexist'] = False
        options['parent'] = root
        options['title'] = 'This is a title'

        ttk.Label(self.frame, text="File Path:     ").pack(side=LEFT)

        # ttk.Entry(self.frame, width=10, textvariable=self.filePath).pack(side = LEFT)
        Tk.Button(self.frame, text='askdirectory', command=self.askdirectory).pack(side=LEFT)

        aaa = Tk.Button(self.frame, text="Check", command=self.openFrame2).pack(side=LEFT)
        # self.btn = Tk.Button(self.frame2, textvariable=self.check, command=self.openFrame).pack(side = TOP)

    def buttonAppear(self):
        matches = self.check

        for match in matches:
            # pass each button's text to a function
            action = lambda x=match: text_update(x)
            # create the buttons and assign to animal:button-object dict pair
            self.check[match] = Tk.Button(self.frame2, text=match, command=self.opener(match))
            self.check[match].pack(side=TOP)

    def opener(self, match):
        self.openFrame(match)

    def askdirectory(self):
        dirPath = tkFileDialog.askdirectory(**self.dir_opt)
        value = dirPath.split("/")[-1]
        self.dirPath.set(value)

    # ----------------------------------------------------------------------
    def hide(self):
        """"""
        self.root.withdraw()

    # ----------------------------------------------------------------------
    def openFrame(self, match):
        """
        :param match:
        """
        # self.hide()
        subFrame = OtherFrame(match, self.check[match])
        handler = lambda: self.onCloseOtherFrame(subFrame)
        # btn = Tk.Button(subFrame, text="Close", command=handler)
        # btn.pack(side = BOTTOM)

    # ----------------------------------------------------------------------
    def openFrame2(self):
        value = str(self.dirPath.get())
        devin = cDirectory(value, "hashes.txt")
        x = {}

        for i in devin:

            s = [i[0] + ":    " + i[1][1]]

            for j in i[1][2]:
                l = []
                for k in j:
                    l.append(k)
                s.append(l)
            x[i[0]] = s

        self.check = x
        self.buttonAppear()

    # ----------------------------------------------------------------------
    def onCloseOtherFrame(self, otherFrame):
        """
        :param otherFrame:
        """
        otherFrame.destroy()
        self.show()

    # ----------------------------------------------------------------------
    def show(self):
        """"""
        self.root.update()
        self.root.deiconify()

    def toggle(self):
        self.btn.pack(side=TOP)

    @staticmethod
    def center_window(width=300, height=200):
        # get screen width and height
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # calculate position x and y coordinates
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        root.geometry('%dx%d+%d+%d' % (width, height, x, y))


# ----------------------------------------------------------------------
if __name__ == "__main__":
    root = Tk.Tk()
    root.geometry("800x600")
    app = MyApp(root)
    root.mainloop()
