'''
Funcion: Bloque organizado y rehusable de codigo. Proporciona modularidad y reutilizacion. 
Se compone de 3 partes, la keyword "def", los parentesis y la funcion 
argumentos = con lo que trabaja la funcion
def funct(name):    #name es el argumento

*args = se utiliza para pasar un numero de argumentos no definidos, se obtiene una tupla
**kwargs = se utiliza para pasar un numero de argumentos no definidos, se obtiene un diccionario
Se pueden combinar los *args y los **kwargs
''' 

def funcion(*args):
    print(args)

funcion(1,2,3,4,5,6)
funcion()
funcion("Hola", "Mundo", 3)

def funcion2(**kwargs):
    print(kwargs)
funcion2(primero = 1, segundo = 2)

def funcion3(*args, **kwargs):
    print(args)
    print(kwargs)

funcion3("hola", "mundo", primer = 1, segundo = "hey")

print(type(range(2,10)))
