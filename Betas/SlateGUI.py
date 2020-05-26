from tkinter import *

slate = Tk() #set up window. `slate' is now the name of the window, internally
scrollbar = Scrollbar(slate) #set up scrollbar
scrollbarX = Scrollbar(slate) #set up horizontal scrollbar
scrollbar.pack( side = RIGHT, fill = Y ) #vertical
scrollbarX.pack(side=RIGHT, fill=Y) #horizontal

mylist = Listbox(slate, yscrollcommand=scrollbar.set, xscrollcommand=scrollbarX.set)
for line in range(100):
   mylist.insert(END, "This is line number " + str(line))

mylist.pack( side = LEFT, fill = BOTH )
scrollbar.config( command = mylist.yview )

mainloop()
