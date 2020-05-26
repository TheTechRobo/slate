from tkinter import *
from tkinter import filedialog
def save():
    filename = filedialog.askopenfilename(initialdir="/", title="Saving file", filetypes=("all files", "*.*"))
    print("WIP %s" % filename)

slate = Tk() #set up window. `slate' is now the name of the window, internally
scrollbar = Scrollbar(slate, orient=VERTICAL) #set up scrollbar
scrollbar.pack( side = RIGHT, fill = Y ) #vertical

text = Text(slate, yscrollcommand=scrollbar.set)
text.pack()
scrollbar.config( command = text.yview )
Button(slate, text="Save", command=save).pack()

mainloop()
