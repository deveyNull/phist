import Tkinter as tk


def text_update(animal):
    text.delete(0, tk.END)
    text.insert(0, animal)


root = tk.Tk()
# text = tk.Entry(root)
# text.pack()
btn_dict = {}
words = ["Small/Eo-W_SME.jpg: d798312b77ccb0e9cf5d2a64af05133b02b8  Small/Eo-W_SME.jpg  18:04 26/01/2016",
         "Small/EAEVwaQS.jpg:	d798312b77ccb0e9cf5d2a64af05133b02b8  Small/Eo-W_SME.jpg  18:04 26/01/2016",
         "Small/FullSizeRender-300x150.jpg:  979f96623b8fcc5466269565366b882695ac  Small/FullSizeRender-300x150.jpg  18:00 26/01/2016  \n\t\t\t\t\t\t\tSmall/FullSizeRender-300x150.jpg  18:04 26/01/2016"]

for animal in words:
    # pass each button's text to a function
    action = lambda x=animal: text_update(x)
    # create the buttons and assign to animal:button-object dict pair
    btn_dict[animal] = tk.Button(root, text=animal, command=action)
    btn_dict[animal].pack(side='top')

# run the GUI event loop
root.mainloop()
