#Experimento!  
#SLATE text editor
#Version 0.2
print("HELLLLLLLLLO GitHub! ")
print("Going to save files in directory _shell.py is in. If you want to exit, type exit,!")
print("slate version 0.2.3 (ALPHA)")
while True:
    mode = input("Mode: a for append, w for overwrite (or newfile), l for newline. Case-sensitive. ")
    if mode == "a":
        print("Mode: Append (A)")
        file = input("Filename?")
        if file == "exit,!":
            print("Not developed yet")
            #Shell()
        else:
            my_file = open(file, "a") #open user file as append
            my_file.write(input("Type a line. ")) #Append to the file
                

    elif mode == "w":
        print("Mode: Overwrite or newfile (W)")
        file = input("Enter filename: ")
        if file == "exit,!":
            print("If you did this in the actual version it would restart the shell.")
            #Shell()
        else:
                my_file = open(file, "w")  #open user-chosen file as readwrite
                my_file.write(input("Type a line. ")) #Write to the file
    elif mode == "l":
        print("Mode: Newline (L)")
        file = input("Filename?")
        if file == "exit,!":
            print("Not developed yet")
            #Shell()
        else:
            my_file = open(file, "a") #open user file as append
            my_file.write('''
            ''')) #Add new line?  to the file
    else: 
        print("Well... you need to type a(ppend), or (over)w(rite), or (new)l(ine) To exit, type either a, w, or l. Then type exit,!")
