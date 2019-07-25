#Experimento!  
#SLATE text editor
#Version 0.2.5
#setup
import time
print("Going to save files in directory slateAlpha.py is in. If you want to exit, type exit,!")
print("slate version 0.2.5 (alpha)")
print("Loading................")
time.sleep(8)
print("Done.")
while True:
    for i in range(0, 11):
            print()
    mode = input("Mode: a for append, w for overwrite (or newfile), l for newline, exit,! for exit. Case-sensitive. ")
    if mode == "a":
        for i in range(0, 11):
            print()
        print("Mode: Append (a)")
        file = input("Filename?")
        if file == "exit,!":
            exit()
        else:
            my_file = open(file, "a") #open user file as append
            for i in range(0, 11):
            print()
            my_file.write(input("Type a line. ")) #Append to the file
    elif mode == "w":
        for i in range(0, 11):
            print()
        print("Mode: Overwrite or newfile (w)")
        file = input("Enter filename: ")
        if file == "exit,!":
            exit()
        else:
                my_file = open(file, "W")  #open user-chosen file as readwrite
                my_file.write(input("Type a line. ")) #Write to the file
    elif mode == "l":
        for i in range(0, 11):
            print()
        print("Mode: Newline (l)")
        file = input("Filename?")
        if file == "exit,!":
            exit()
        else:
            my_file = open(file, "a") #open user file as append
            my_file.write('''
            ''')) # Add new line? to the file
    elif mode == "exit,!":
        exit()
    else: 
        for i in range(0, 11):
            print()
        print("Command not found; you need to type a(ppend), or (over)w(rite), or (new)l(ine) To exit, exit,!. Sorry for the inconvenience")
