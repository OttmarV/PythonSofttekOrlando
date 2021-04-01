"""
os.unlink() will delete a file.
os.rmdir() will delete a folder (but the folder must be empty).
shutil.rmtree() will delete a folder and all its contents.
Deleting can be dangerous, so do a "dry run" first.
send2trash.send2trash() will send a file or folder to the recycling bin.
"""
import shutil #Este modulo permite copiar, mover, renombrar o borrar archivos 
import os

shutil.copy("C:\\Users\\VargasO\\OneDrive - HP Inc\\archivos_practice.txt", "C:\\Users\\VargasO\\OneDrive - HP Inc\\Python Softtek\\PythonSofttekOrlando\\Udemy\\") #permite copiar archivos

shutil.copytree(src, dst) #permite copiar todo un folderr con todo lo de adentro
shutil.move(src, dst) # permite mover un archivo, si se quiere renombrar un archivo, se puede mover al mismo directorio pero con otro nombre, como en linux
shutil.rmtree(path) #permite remover un folder con todo lo de adentro


os.unlink(path) #borra permanentemente este archivo
os.getcwd()

print(os.listdir())
#############################
"""
Programa para borrar un archivos que terminen en .txt del directorio actual

"""
os.chdir(path)
for filename in os.listdir():
    if filename.endswith(suffix):
        os.unlink(path)
        #print(filename)

import send2trash #En vez de eliminar una archivo para siempre como lo hace el os.unlink, lo manda al trash bin del sistema operativo
send2trash.send2trash(path)

#############################

"""
Programa para recorrer todo un directory tree, entra a cada carpeta que exista y enlista folders, subfolders y nombre de los archivos.
"""
print(os.walk('C:\\Users\\VargasO\\OneDrive - HP Inc\\Python Softtek\\PythonSofttekOrlando\\Udemy'))
for folderName, subFolders, fileNames in os.walk('C:\\Users\\VargasO\\OneDrive - HP Inc\\Python Softtek\\PythonSofttekOrlando'):
    print("The folder is " + folderName)
    print("The subfolder in " + folderName + " are " + str(subFolders))
    print("The filenames in " + folderName + " are: " + str(fileNames) + "\n")

    for subFolder in subFolders:
        if 'fish' in subFolder:
            pass
            #os.rmdir(subfolder)

    for file in fileNames:
        if file.endswith('.py'):
            pass
            #shutil.copy(os.path.join(folderName, file), os.path.join(folderName, file + '.backup'))
