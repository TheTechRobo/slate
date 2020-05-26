from tkinter import *
from tkinter import messagebox as msg
from tkinter import filedialog #https://pythonspot.com/tk-file-dialogs/
def save():
    try: #here, if variable `filename' does not exist, we will ask for a filename. if it does exist, we'll use it. kind of like how a normal text editor makes you save as the same file until you click "New".
        yolo = filename
        del yolo
        keepTheFilename = True
    except:
        keepTheFilename = False
    if not keepTheFilename:
        from os.path import expanduser
        home = expanduser("~")
        filename = filedialog.asksaveasfilename(initialdir=home, title="Saving file")
    print("Saving to  %s" % filename, end="\r")
    theText = text.get(0.0, "end-1c") #https://stackoverflow.com/a/14824164/9654083
    with open(filename, "w") as theFile:
        theFile.write(theText)
    slate.title(filename)
def openFile():
    from os.path import expanduser
    home = expanduser("~")
    filename = filedialog.askopenfilename(initialdir=home, title="Select file to open")
    with open(filename, "r") as theFile:
        theText = theFile.read()
        text.delete(0.0, END)
        text.insert(END, theText)
    slate.title(filename)
def deleteAll():
    text.delete(0.0, END)
    slate.title("slate")
    del filename
def hello():
    msg.showinfo("About", "slate is a decent plain-text editor. Thanks for using!")
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
menubar = Menu(slate) #add menubar
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
slate.config(menu=menubar) #add menubar to window

mainloop()
