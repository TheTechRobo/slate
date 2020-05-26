from tkinter import *
from tkinter import filedialog #https://pythonspot.com/tk-file-dialogs/
def save():
    from os.path import expanduser
    home = expanduser("~")
    filename = filedialog.asksaveasfilename(initialdir=home, title="Saving file")
    print("Saved to  %s" % filename)
    theText = text.get(0.0, "end-1c") #https://stackoverflow.com/a/14824164/9654083
    with open(filename, "w") as theFile:
        theFile.write(theText)
def openFile():
    from os.path import expanduser
    home = expanduser("~")
    filename = filedialog.askopenfilename(initialdir=home, title="Select file to open")
    with open(filename, "r") as theFile:
        theText = theFile.read()
        text.delete(0.0, END)
        text.insert(END, theText)
def deleteAll():
    text.delete(0.0, END)
def hello():
    msg.info("About", "slate is a decent plain-text editor. Thanks for using!")
    Label(slate, text="To-Dos: - add \"staying on file\" (instead of having to type the filename over and over again; - copy-paste functions; - and more!").pack()

slate = Tk() #set up window. `slate' is now the name of the window, internally
slate.title("slate") #set up window. `slate' is now the word in the title bar
scrollbar = Scrollbar(slate, orient=VERTICAL) #set up scrollbar
scrollbar.pack( side = RIGHT, fill = Y ) #vertical

text = Text(slate, yscrollcommand=scrollbar.set)
text.pack()
scrollbar.config( command = text.yview )
w = Button(slate, text="Save", command=save)
w2 = Button(slate, text="Open", command=openFile)

w.pack(padx=5, pady=10, side=LEFT)
w2.pack(padx=5, pady=10, side=LEFT)

#set up menubar
menubar = Menu(main) #add menubar
slenu = Menu(menubar, tearoff=0) #add "slenu" cascade
slenu.add_command(label="About...", command=hello) #add command
slenu.add_separator() #add separator
slenu.add_command(label="Exit slate", command=slate.quit)
menubar.add_cascade(label="slate", menu=slenu) #finalize
#second menu
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=deleteAll)
filemenu.add_command(label="Open...", command=openFile)
filemenu.add_command(label="Save...", command=save)
filemenu.add_separator()
filemenu.add_command(label="Exit slate", command=slate.quit)
menubar.add_cascade(label="File", menu=filemenu)

mainloop()
