"""
The Requests module is a third-party module for downloading web pages and files.
requests.get() returns a Response object.
The raise_for_status() Response method will raise an exception if the download failed.
You can save a downloaded file to your hard drive with calls to the iter_content() method.
"""

import requests

res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
print(res.status_code) #200 es que fue exitoso
print(len(res.text)) #cantidad de caracteres
print(res.text[:500])
print(res.raise_for_status()) #si hay algun problema descargando el archivo, arroja una excepcion



playFile = open("Udemy\\Romeo and Juliet.txt", "wb") # crea el archivo y escribe 100000 bytes en 10000 bytes por iteracion el contenido que se descargo
for chunk in res.iter_content(100000):
    playFile.write(chunk)

