from Tkinter import *
import Tkinter as Tk
# from tkinter import ttk
# from phash import *
from PIL import ImageTk
# import tkinter as tk
import Image
import ImageTk


########################################################################
class OtherFrame(Tk.Toplevel):
    """"""

    # ----------------------------------------------------------------------
    def __init__(self, original):
        """Constructor"""
        self.original_frame = original
        Tk.Toplevel.__init__(self)
        self.title("Image Comparison")
        imageFile = "A.jpg"
        self.image1 = ImageTk.PhotoImage(Image.open(imageFile))

        panel1 = Tk.Label(self, image=self.image1)
        panel1.pack(side='left', fill='both', expand='yes')
        btn = Tk.Button(self, text="Close", command=self.onClose)
        btn.pack()

    # ----------------------------------------------------------------------
    def onClose(self):
        """"""
        self.destroy()
        self.original_frame.show()


########################################################################
class MyApp(object):
    # ----------------------------------------------------------------------
    def __init__(self, parent):
        self.root = parent
        self.root.title("Main frame")
        self.frame = Tk.Frame(parent)
        self.frame.pack()
        Frame3 = Frame(self.root)

        imageFile = "A.jpg"
        self.image1 = ImageTk.PhotoImage(Image.open(imageFile))

        Frame3.pack(side=TOP)
        panel1 = Tk.Label(Frame3, image=self.image1)
        panel1.pack(side='left', fill='both', expand='yes')
        btn = Tk.Button(self.frame, text="Open Frame", command=self.openFrame)
        btn.pack()

    # ----------------------------------------------------------------------
    def hide(self):
        """"""
        self.root.withdraw()

    # ----------------------------------------------------------------------
    def openFrame(self):
        """"""
        # self.hide()
        subFrame = OtherFrame(self)

    # ----------------------------------------------------------------------
    def show(self):
        """"""
        self.root.update()
        self.root.deiconify()


# ----------------------------------------------------------------------
if __name__ == "__main__":
    root = Tk.Tk()
    root.geometry("800x600")
    app = MyApp(root)
    root.mainloop()

    """import Tkinter as Tk
from tkinter import *
from tkinter import *
from tkinter import ttk
from phash import *
from PIL import ImageTk
import Image
import ImageTk
#http://www.blog.pythonlibrary.org/2012/07/26/tkinter-how-to-show-hide-a-window/

########################################################################
class OtherFrame(Tk.Toplevel):
	#----------------------------------------------------------------------
	def __init__(self):

		Tk.Toplevel.__init__(self)
		self.geometry("400x300")
		self.title("otherFrame")
		
		imageFile = "A.jpg"
		self.image1 = ImageTk.PhotoImage(Image.open(imageFile))
		Frame3.pack(side = TOP)
		panel1 = tk.Label(Frame3, image=self.image1)
		panel1.pack(side='left', fill='both', expand='yes')
		imageFile2 = "B.jpg"
		self.image2 = ImageTk.PhotoImage(Image.open(imageFile2))

		panel2 = tk.Label(Frame3, image=self.image2)
		panel2.pack(side='left', fill='both', expand='yes')

 
########################################################################
class MyApp(object):
    """"""
 
    #----------------------------------------------------------------------
    def __init__(self, parent):

        self.root = parent
        self.root.title("Main frame")
        self.frame = Tk.Frame(parent)
        self.frame.pack()
 
        btn = Tk.Button(self.frame, text="Open Frame", command=self.openFrame)
        btn.pack()
 
    #----------------------------------------------------------------------
    def openFrame(self):
        """"""
        subFrame = OtherFrame()
        handler = lambda: self.onCloseOtherFrame(subFrame)
        btn = Tk.Button(subFrame, text="Close", command=handler)
        btn.pack()
 
    #----------------------------------------------------------------------
    def onCloseOtherFrame(self, otherFrame):
        """"""
        otherFrame.destroy()
        self.show()
 
    #----------------------------------------------------------------------
    def show(self):
        """"""
        self.root.update()
        self.root.deiconify()
 
 
#----------------------------------------------------------------------
if __name__ == "__main__":
    root = Tk.Tk()
    root.geometry("800x600")
    app = MyApp(root)
    root.mainloop()"""
