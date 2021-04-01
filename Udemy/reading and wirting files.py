"""
The open() function will return a file object which has reading and writing –related methods.
Pass ‘r' (or nothing) to open() to open the file in read mode. Pass ‘w' for write mode. Pass ‘a' for append mode.
Opening a nonexistent filename in write or append mode will create that file.
Call read() or write() to read the contents of a file or write a string to a file.
Call readlines() to return a list of strings of the file's content.
Call close() when you are done with the file.
The shelve module can store Python values in a binary file.
The shelve.open() function returns a dictionary-like shelf value.
"""

import os
import shelve #ayuda a crear un objeto tipo diccionario, no utilizarlo, crea los arhcivos .dat, .bak y .dir

helloFile = open("Udemy\\text.txt", "a")
#print(helloFile.read())
helloFile.write("HUEHEUEUHEHE\n")
#print(helloFile.read())
helloFile.close()

print(os.getcwd())

shelfFile = shelve.open("Udemy\\mydata") 
shelfFile['cats'] = ['ruben', 'monica', 'sergio']
print(shelfFile['cats'])
shelfFile.close()

