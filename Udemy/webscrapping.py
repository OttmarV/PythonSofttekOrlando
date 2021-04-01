import webbrowser, sys, pyperclip

sys.argv #son los argumentos que se pasan al programa al momento de ejecucion, los muestra en forma de lista

#Revisar si se mandaron argumentos
if len(sys.argv) > 1:
    #el primer elemento de la lista sys.argv es el nombre del archivo, los demás componen el address, por lo que tenemos que unir en un string el address.
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

#https://www.google.com/maps/place/<ADDRESS>
webbrowser.open("https://www.google.com/maps/place/" + address)

