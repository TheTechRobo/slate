#SLATE is a Eureka
#SLATE text editor
#Version 0.3.1
#setup
print("Going to save files in current working directory (typically ~). If you want to exit, type exit,!")
print("slate version 0.3.1 (alpha)")
print("Loading................")
from time import *
import os
def append():
    os.system('clear')
    print("Mode: Append (a)")
    file = input("Filename?")
    if file == "exit,!":
    	exit()
    elif file == "EXIT,!":
        exit()
    else:
        my_file = open(file, "a") #open user file as append
        os.system('clear')
        my_file.write(input("Type a line. ")) #Append to the file
    print()


def overwrite():
    os.system('clear')
    print("Mode: Overwrite or newfile (w)")
    file = input("Enter filename: ")
    if file == "exit,!":
        exit()
    elif file == "EXIT,!":
        exit()
    else:
        my_file = open(file, "w")  #open user-chosen file as readwrite
        my_file.write(input("Type a line. ")) #Write to the file
		
def newline():
    os.system('clear')
    print("Mode: Newline (l)")
    file = input("Filename?")
    if file == "exit,!":
        exit()
    else:
        my_file = open(file, "a") #open user file as append
        my_file.write('''
        ''') # Add new line? to the file
def nothing():
	pass
print("Done.")
while True:
    os.system('clear')
    mode = input("Mode: a for append, w for overwrite (or newfile), l for newline, exit,! for exit. ")
	#APPEND
    if mode == "a":
	    append()
    elif mode == "A":
        append()
#OVERWRITE.
    if mode == "w":
        overwrite()
    elif mode == "W":
        overwrite()
#NEWLINE
    if mode == "l":
        newline()
    elif mode == "L":
        newline()
#EXITING
    if mode == "exit,!":
        exit()
    elif mode == "EXIT,!":
        exit()
#OTHERWISE......
    else: 
        os.system('clear')
        print("Command not found; you need to type a(ppend), or (over)w(rite), or (new)l(ine) To exit, exit,!. Sorry for the inconvenience")
        print("Please wait...")
        sleep(1.5)
# No More If Statements
    os.system('clear')
    print("Please Wait")
    sleep(1.5)
