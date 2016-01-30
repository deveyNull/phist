from phash import *
from Tkinter import *
import Tkinter as Tk
from tkinter import ttk
# from phash import *
from PIL import ImageTk
# import tkinter as tk
import Image
import ImageTk


########################################################################
class OtherFrame(Tk.Toplevel):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self, queried, data):
        """Constructor"""
        Tk.Toplevel.__init__(self)
        # self.geometry("400x300")
        self.title("Image Comparison")
        self.center_window(1000, 600)
        Frame3 = Frame(self)
        queried = str(queried.get())
        data2 = str(data.get())
        returnImg = data2.split(" ")[0]
        returnData = data2.split(" ")[1:]

        Frame4 = Frame(self)

        Frame3.pack(side=LEFT)
        Frame4.pack(side=LEFT)

        imageFile = queried
        self.image1 = ImageTk.PhotoImage(Image.open(imageFile))
        panel1 = Tk.Label(Frame3, image=self.image1)
        panel1.pack(side=TOP, fill='both', expand='yes')
        Tk.Label(Frame3, text=queried.strip()).pack(side=BOTTOM)

        imageFile2 = returnImg
        self.image2 = ImageTk.PhotoImage(Image.open(imageFile2))
        panel2 = Tk.Label(Frame4, image=self.image2)
        panel2.pack(side=TOP, fill='both', expand='yes')
        Tk.Label(Frame4, text=data2.strip()).pack(side=BOTTOM)

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
        self.filePath = StringVar()
        self.Location = StringVar()
        self.image = StringVar()
        self.check = StringVar()
        self.match = StringVar()
        self.checker = StringVar()
        self.flag = 0
        self.buttonDisplay = StringVar()

        ttk.Label(self.frame, text="File Path").pack(side=LEFT)

        ttk.Button(self, text='askdirectory', command=self.askdirectory).pack(**button_opt)

        aaa = Tk.Button(self.frame, text="Check", command=self.openFrame2).pack(side=LEFT)
        text = "Small/Eo-W_SME.jpg: d798312b77ccb0e9cf5d2a64af05133b02b8    Small/Eo-W_SME.jpg  18:04 26/01/2016\nSmall/EAEVwaQS.jpg:	d798312b77ccb0e9cf5d2a64af05133b02b8    Small/Eo-W_SME.jpg  18:04 26/01/2016\nSmall/FullSizeRender-300x150.jpg:	979f96623b8fcc5466269565366b882695ac	Small/FullSizeRender-300x150.jpg  18:00 26/01/2016  Small/FullSizeRender-300x150.jpg  18:04 26/01/2016\n"

        def askdirectory(self):
            return tkFileDialog.askdirectory(**self.dir_opt)

    # ----------------------------------------------------------------------
    def hide(self):
        """"""
        self.root.withdraw()

    # ----------------------------------------------------------------------
    def openFrame(self):
        """"""
        # self.hide()
        subFrame = OtherFrame(self.filePath, self.check)
        handler = lambda: self.onCloseOtherFrame(subFrame)
        # btn = Tk.Button(subFrame, text="Close", command=handler)
        # btn.pack(side = BOTTOM)

    # ----------------------------------------------------------------------
    def openFrame2(self):
        value = str(self.filePath.get())
        devin = list(cImage(value, "hashes.txt"))
        x = ""
        for i in devin[2]:

            for j in i:
                x += j + " "
        x += "\n"
        self.check.set(x)
        self.toggle()

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

        def checker(self):
            value = self.filePath
            devin = list(cImage(value, "hashes.txt"))
            x = ""
            for i in devin[2]:

                for j in i:
                    x += j + " "
            x += "\n"
            self.check.set(x)

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
