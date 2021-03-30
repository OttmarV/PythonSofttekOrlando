#Generadores: generan una secuencia de iterables (solo pueden iterar 1 vez)
#Iterador: secuencia de iterables (solo pueden iterar 1 vez)
#Listas, tuplas, sets y diccionarios no son iteradores, pero son iterables. Los puedes convertir a iteradores mediante la funcion iter()
#Todos los iteradores son iterables, pero no todos los iterables son iteradores
#Todos los generadores son iteradores, pero no todos los iteradores son generadores
#¿Como saber si es iterador? - utilizando la funcion next() en el iterable, si da error es que no es iterable, ó revisando su clase si tiene __next__()
#Diferencias entre generador e iterador:
    #Generador: Se declaran mediante una funcion y utilizando la palabra yield. Guarda el estado de la variable local. Codigo rapido y compacto.
    #Iterador: Se puede customizar para mayor funcionalidad mediante __iter__ y __next__, se pueden crear utilizando iter(), mas memory efficient (Revisar esto)

#cuando utilizamos listas muy grandes, podemos tener errores de memoria
lista = [x for x in range(1000000000000)]

for numero in lista:
    print(numero) 

"""
el objeto range, es un tipo de generador
que es un generador?, es una función especial que en lugar de regresar un solo valor
genera un listado de valores uno a la vez, con el objetivo de ahorrar memoria y solo
brindar el valor que se va a utilizar en la siguiente iteración
"""
rango = range(100000000000000000000000)
print(type(rango))# -> <class 'range'>
print(rango)# -> range(0, 100000000000000000000000)

#para crear un generador, lo hacemos de la siguiente manera
def generadora(desde, hasta):
    for numero in range(desde, hasta + 1):
        yield numero

#como podemos ver, noparece nada especial
#solo la palabra yield resalta
#pero con esta forma, podemos generar iteradores condicionados, por ejemplo, solo números pares, impares,
#primos, o si fuesen palabras, solo palabras que empiecen o contengan un substring, etc

#qué pasa si llamamos a la función asignándolo a una variable?

generador = generadora(0,3)
print(type(generador))# -> <class 'generator'>
print(generador)# -> <generator object generadora at 0x000001410BC3FBA0>

"""
pero que es un objeto generador?
un objeto generador es una secuencia iterable, un iterador
los iteradores pueden ser utilizados en una función integrada llamada next
que nos servirá para leer en secuencia cada uno de los elementos del iterador

"""
print(next(generador))# -> 0
print(next(generador))# -> 1
print(next(generador))# -> 2
print(next(generador))# -> 3
print(next(generador))# -> Genera error StopIteration dado que el generador no tiene más elementos

#la función next solo sirve si el objeto es un iterador
#aunque las listas, tuplas, conjuntos y diccionarios pueden iterarse, estos no son considerados
#iteradores sino iterables, esto lo sabemos si tratamos de usar next en una lista por ejemplo
lista = ["a","b","c"]
print(next(lista))# -> TypeError: 'list' object is not an iterator

#otra particularidad de los iteradores, es que no podemos regresar a un índice anterior
#los iteradores solo pueden avanzar al siguiente valor, recordemos que estos no conservan
#todos sus valores para ahorrar memoria
