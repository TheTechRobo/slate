#SLATE is a Eureka
#SLATE text editor
#Version 0.3
#setup
import time
print("Going to save files in current working directory (typically ~). If you want to exit, type exit,!")
print("slate version 0.3 (alpha)")
print("Loading................")
time.sleep(2)
print("Done.")
while True:
    os.system('clear')
    mode = input("Mode: a for append, w for overwrite (or newfile), l for newline, exit,! for exit. ")
    
#APPEND
	if mode == "a":
        os.system('clear')
        print("Mode: Append (a)")
        file = input("Filename?")
        if file == "exit,!":
            exit()
		elif file == "EXIT,!"
			exit()
        else:
            my_file = open(file, "a") #open user file as append
            for i in range(0, 11):
            print()
            my_file.write(input("Type a line. ")) #Append to the file
    elif mode == "A":
        os.system('clear')
        print("Mode: Append (a)")
        file = input("Filename?")
        if file == "exit,!":
            exit()
		elif file == "EXIT,!"
			exit()
        else:
            my_file = open(file, "a") #open user file as append
            for i in range(0, 11):
            print()
            my_file.write(input("Type a line. ")) #Append to the file
#OVERWRITE.
	elif mode == "w":
        os.system('clear')
        print("Mode: Overwrite or newfile (w)")
        file = input("Enter filename: ")
        if file == "exit,!":
            exit()
        else:
                my_file = open(file, "W")  #open user-chosen file as readwrite
                my_file.write(input("Type a line. ")) #Write to the file
	elif mode == "W":
        os.system('clear')
        print("Mode: Overwrite or newfile (w)")
        file = input("Enter filename: ")
        if file == "exit,!":
            exit()
        else:
                my_file = open(file, "W")  #open user-chosen file as readwrite
                my_file.write(input("Type a line. ")) #Write to the file
    
#NEWLINE
	elif mode == "l":
        os.system('clear')
        print("Mode: Newline (l)")
        file = input("Filename?")
        if file == "exit,!":
            exit()		
	elif mode == "L":
		os.system('clear')
        print("Mode: Newline (l)")
        file = input("Filename?")
        if file == "exit,!":
            exit()
        else:
            my_file = open(file, "a") #open user file as append
            my_file.write('''
            ''')) # Add new line? to the file
#EXITING
    elif mode == "exit,!":
        exit()
	elif mode == "EXIT,!":
		exit()
#OTHERWISE...
    else: 
        os.system('clear')
        print("Command not found; you need to type a(ppend), or (over)w(rite), or (new)l(ine) To exit, exit,!. Sorry for the inconvenience")
        print("Please Wait")
        time.sleep(1.5)
