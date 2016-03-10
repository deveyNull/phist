from PIL import ImageTk
from tkinter import *

try:
    # Python2
    import Tkinter as tk
except ImportError:
    # Python3
    import tkinter as tk

# create the root window
root = tk.Tk()
root.geometry("+{}+{}".format(7, 10))
# set ULC (x, y) position of root window
frame1 = Frame(root)
frame1.pack()

# pick image files you have in your working directory
# or use full path
# PIL's ImageTk allows .gif  .jpg  .png  .bmp formats
imageFile1 = "A.jpg"
imageFile2 = "B.jpg"
data1 = "A.jpg"
data2 = "B.jpg"

# PIL's ImageTk converts to an image object that Tkinter can handle
photo1 = ImageTk.PhotoImage(file=imageFile1)
photo2 = ImageTk.PhotoImage(file=imageFile2)

# put the image objects on labels in a grid layout
tk.Label(frame1, image=photo1).grid(row=0, column=0)
tk.Label(frame1, image=photo2).grid(row=0, column=1)
tk.Label(frame1, text=data1).grid(row=1, column=0)
tk.Label(frame1, text=data2).grid(row=1, column=1)

frame2 = Frame(root)
frame2.pack()

# pick image files you have in your working directory
# or use full path
# PIL's ImageTk allows .gif  .jpg  .png  .bmp formats
imageFile1 = "A.jpg"
imageFile2 = "B.jpg"
data1 = "A.jpg"
data2 = "B.jpg"

# PIL's ImageTk converts to an image object that Tkinter can handle
photo1 = ImageTk.PhotoImage(file=imageFile1)
photo2 = ImageTk.PhotoImage(file=imageFile2)

# put the image objects on labels in a grid layout
tk.Label(frame2, image=photo1).grid(row=0, column=0)
tk.Label(frame2, image=photo2).grid(row=0, column=1)
tk.Label(frame2, text=data1).grid(row=1, column=0)
tk.Label(frame2, text=data2).grid(row=1, column=1)
# execute the event loop
root.mainloop()
