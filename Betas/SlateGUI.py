from tkinter import *

def save():
    print("WIP")
slate = Tk() #set up window. `slate' is now the name of the window, internally
scrollbar = Scrollbar(slate, orient=VERTICAL) #set up scrollbar
scrollbarX = Scrollbar(slate, orient=HORIZONTAL) #set up horizontal scrollbar
scrollbar.pack( side = RIGHT, fill = Y ) #vertical
scrollbarX.pack(side=BOTTOM, fill=X) #horizontal

#mylist = Listbox(slate, yscrollcommand=scrollbar.set, xscrollcommand=scrollbarX.set)
#for line in range(100000):
#   mylist.insert(END, "This is line number:::::::::::::::: " + str(line))

#mylist.pack( side = LEFT, fill = BOTH )
text = Text(slate)
text.pack()
scrollbar.config( command = text.yview )
scrollbarX.config(command=text.xview)
Button(slate, text="Save", command=save).pack()

mainloop()
