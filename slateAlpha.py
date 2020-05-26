#SLATE is a Eureka
#SLATE text editor
#Version 0.3.x. 
#In early development, but has rare updates.
#setup
from sys import exit
print("Going to save files in current working directory (typically ~/slate). If you want to exit, type exit,!")
print("Loading................")
from time import *
import os
def wait():
    sleep(1.5)

def append():
    print(chr(27)+'[2j') #First attempt at clearing the screen with ANSI escape codes.
    print('\033c') #Second attempt at clearing the screen with ANSI escape codes.
    print('\x1bc') #Third attempt at clearing the screen with ANSI escape codes.
    print("Mode: Append (a)")
    file = input("Filename?")
    if file.lower() == "exit,!":
    	exit()
    else:
        my_file = open(file, "a+") #open user file as append or, if it doesn't exist, create it
        print(chr(27)+'[2j') #First attempt at clearing the screen with ANSI escape codes.
        print('\033c') #Second attempt at clearing the screen with ANSI escape codes.
        print('\x1bc') #Third attempt at clearing the screen with ANSI escape codes.
        my_file.write(input("Type a line. ")) #Append to the file
    print()

def overwrite():
    print(chr(27)+'[2j') #First attempt at clearing the screen with ANSI escape codes.
    print('\033c') #Second attempt at clearing the screen with ANSI escape codes.
    print('\x1bc') #Third attempt at clearing the screen with ANSI escape codes.
    print("Mode: Overwrite or newfile (w)")
    file = input("Enter filename: ")
    if file.lower() == "exit,!":
        exit()
    else:
        my_file = open(file, "w+")  #open user-chosen file as readwrite
        my_file.write(input("Type a line. ")) #Write to the file
		
def newline():
    print(chr(27)+'[2j') #First attempt at clearing the screen with ANSI escape codes.
    print('\033c') #Second attempt at clearing the screen with ANSI escape codes.
    print('\x1bc') #Third attempt at clearing the screen with ANSI escape codes.
    print("Mode: Newline (l)")
    file = input("Filename?")
    if file.lower() == "exit,!":
        exit()
    else:
        my_file = open(file, "a+") #open user file as append
        my_file.write('''
        ''') # Add new line? to the file
wait()
print("Done.")
while True:
    print(chr(27)+'[2j') #First attempt at clearing the screen with ANSI escape codes.
    print('\033c') #Second attempt at clearing the screen with ANSI escape codes.
    print('\x1bc') #Third attempt at clearing the screen with ANSI escape codes.
    mode = input("Mode: a for append, w for overwrite (or newfile), l for newline, exit,! for exit. ")
    mode = mode.lower()
	#APPEND
    if mode == "a":
	    append()
#OVERWRITE.
    if mode == "w":
        overwrite()
#NEWLINE
    if mode == "l":
        newline()
#EXITING
    if mode == "exit,!":
        exit()
#OTHERWISE......
    else: 
        print(chr(27)+'[2j') #First attempt at clearing the screen with ANSI escape codes.
        print('\033c') #Second attempt at clearing the screen with ANSI escape codes.
        print('\x1bc') #Third attempt at clearing the screen with ANSI escape codes.
        print("Command not found; you need to type a(ppend), or (over)w(rite), or (new)l(ine) To exit, exit,!. Sorry for the inconvenience")
        print("Please wait...")
        wait()
# No More If Statements
    print(chr(27)+'[2j') #First attempt at clearing the screen with ANSI escape codes.
    print('\033c') #Second attempt at clearing the screen with ANSI escape codes.
    print('\x1bc') #Third attempt at clearing the screen with ANSI escape codes.
    print("Please wait...")
    wait()
