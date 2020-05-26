from tkinter import *
from tkinter import filedialog #https://pythonspot.com/tk-file-dialogs/
def save():
    from os.path import expanduser
    home = expanduser("~")
    filename = filedialog.asksaveasfilename(initialdir=home, title="Saving file")
    print("WIP %s" % filename)
    theText = get(0.0)
    with open(filename, "w") as theFile:
        theFile.write("WIP")

slate = Tk() #set up window. `slate' is now the name of the window, internally
scrollbar = Scrollbar(slate, orient=VERTICAL) #set up scrollbar
scrollbar.pack( side = RIGHT, fill = Y ) #vertical

text = Text(slate, yscrollcommand=scrollbar.set)
text.pack()
scrollbar.config( command = text.yview )
Button(slate, text="Save", command=save).pack()

mainloop()
