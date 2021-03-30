#manejadores de contexto
#se utilizan para asignar recursos solo cuando se necesitan
#para operaciones que requieran crear -> operar -> cerrar algo
#muy común por ejemplo al manejar archivos
#el manejador de contexto más común es el WITH

#cuando se abre un archivo como lectura, éste debe existir
try:
    with open("texto.txt", "r") as file:
        for line in file.readlines():
            print(line.strip())

    print(file.readlines())
except:
    print("el archivo no existe")

#entrada y salida de archivos:
#para abrir archivos usamos el método open
#este método requiere 3 parámetros, de los cuales dos son opcional
#open(archivo, metodo_de_apertura, codificacion)
#archivo: ruta relativa o completa al archivo a abrir - requerido
#metodo_de_apertura: lectura("r"), escritura("w"), actualizar("a"), leer_y_escribir("r+") - opcional, si se omite, se abre como lectura
#codificación: siendo uft-8 el mas comun - opcional
#el método de apertura también acepta abrir archivos en binario combinándolo con los metodos "r", "w" o "a" quedando "rb", "wb", "ab"
#"w": crea un archivo y si este archivo ya existía, todo su contenido será borrado
#"a": abre un archivo y coloca el cursor al final del mismo para seguir escribiendo, si no existe, crea el archivo
#"r": solo lectura, si el archivo no existe, una excepción ocurre

#ejemplo de abrir archivo para leer
archivo = open("texto.txt","r") #open busca el archivo y lo abre a solo lectura
print(archivo.read()) #read, muestra todo el contenido del archivo en una sola corrida
archivo.close() #close, cierra el archivo, si se abrió con "w" o "a", toda la información escrita se guarda sobre el archivo

#leer archivo linea por linea:
archivo = open("mbox-short.txt", "r")
print(archivo.readline())#readline, lee el archivo una linea a la vez
print(archivo.readline())#si se ejecuta en secuencia continúa línea
print(archivo.tell())#tell, nos indica la posición donde se encuentra el cursor
print(archivo.readline())
archivo.close()

#leyendo archivo línea a línea en un ciclo:
archivo = open("texto.txt", "r")
print(archivo.readlines())#readlines, crea una lista donde cada línea del archivo es un elemento
#readlines() recorre todo el archivo y deja el cursor al final, si queremos volver al inicio podemos usar
archivo.seek(0)#seek recibe un parámetro, el índice de un caracter del archivo, por tanto, el primer caracter de un archivo es 0

#ahora si, ubicados en el primer caracter y por tanto primera línea, podemos volver a usar readlines
for linea in archivo.readlines():
    print(linea.strip()) #readlines muestra también el salto de línea, por eso usamos strip para quitarlo de nuestra lectura
archivo.close()

#otra característica interesante es saber si el archivo está cerrado o si podemos operar sobre el:
if archivo.closed:
    print("no podemos leerlo")
else:
    print("A leer!")

#escribiendo un archivo nuevo:
archivo = open("noexiste.txt", "w")
texto_a_escribir = "nuevo contenido\n"
archivo.write(texto_a_escribir)
archivo.write(texto_a_escribir)
archivo.write(texto_a_escribir)#escribimos 3 lineas
archivo.close()

#actualizando un archivo:
archivo = open("actualizado.txt", "a")
#muy importante, todo lo que vayamos a escribir en un archivo, debe ser una cadena, de otro modo errores pueden ocurrir
actualizar_con = "linea actualizada\n"
archivo.write(actualizar_con)
archivo.write(actualizar_con)
archivo.write(actualizar_con)#cada que corremos el programa, nuestro archivo tendrá 3 líneas adicionales
archivo.close()

#en todo esto, hemos visto que la estructura básica para operar con archivos es
#open() -> operaciones -> close()
#para escenarios como estos, podemos utilizar los denominados manejadores de contexto
#de los cuales, el más común es WITH

with open("texto.txt", "r") as archivo:
    print(archivo.read())

#si después del with consultamos si el archivo se ha cerrado, vemos que así ha sido:
print(archivo.closed)

#mas detalles:
#https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files