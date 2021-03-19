print("c:\desktop\november") #Existe un salto de linea
print("c:\\desktop\\november") #Para evitar el salto de linea, se debe de hacer un escape al backslash
print(r"c:\desktop\november") #No existe un salto de linea porque es un raw string

import os #es una libreria que maneja funciones que se adecúan al sistema operativo donde se ejecute el programa
path = os.path.join("folder1", "folder2", "folder3", "book.png")
print(path)

print(os.sep) # muestra el separador utilizado para el path del archivo
print(os.getcwd()) # muestra el current working directory
#os.chdir("C:\\") # cambia el working directory  

'''
Path absoluto: siempre comienza desde el root "/" para linux y "C:\" para Windows
Path relativo: siempre es el path relativo al current working directory, puedes utilizar un "." para referirte al directorio actual, o ".." para referirte al parent folder.

'''

print(os.path.abspath("Hello World.py")) #muestra el path absoluto del archivo que le pasemos
print(os.path.isabs("..\\..\\")) #te dice si un path es absoluto, es decir, si comienza desde el root folder
#print(os.path.relpath("some path", "some other path")) #muestra lo que necesita el segundo path para llegar al primer path
print(os.path.dirname("c:\\desktop\\november.png")) #extrae todo el path antes del nombre del archivo
print(os.path.basename("c:\\desktop\\november")) #Extrae el nombre del archivo o carpeta en el ultimo lugar del path
print(os.path.exists("c:\\desktop\\november")) #muestra si un path existe o no
print(os.path.isfile("c:\\desktop\\november.png")) #muestra si el ultimo elemento del path es un archivo
print(os.path.isdir("c:\\desktop\\november")) #muestra si el ultimo elemento del path es un directorio
print(os.path.getsize("c:\\desktop\\november")) #muestra el tamaño del archivo en bytes
print(os.listdir("c:\\desktop\\")) #muestra una lista de strings, con los elementos que contiene el path, ya sea un directorio o archivo
#os.mkdir("c:\\desktop\\november\\weeks") #crea todos los directorios mencionados si no existen




