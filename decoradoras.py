#Para entender las funciones decoradoras, necesitamos entender unos pocos puntos antes:
#----------------Punto 1----------------------------------
#en python todo es un objeto, por lo tanto podemos crear una función y podemos asignar esa función a una variable

def hola():
    return "hola!"

saludo = hola # asignamos a la variable saludo una referencia a la función hola

print(saludo())# -> esto equivale a hacer print(hola())
#-------------fin punto 1---------------------------------

#----------------Punto 2----------------------------------
#de lgual modo, podemos llamar a una función y que esta función nos regrese otra función

def hola2():
    def saludo():
        return "Hola desde Saludo!"
    
    return saludo # la funcion hola2 nos regresa una referencia a la función saludo

#qué pasa si llamamos la función hola2?
print(hola2())# -> <function hola2.<locals>.saludo at 0x00000257927CC310>

local = hola2()# -> el contenido de local es la función saludo que se construyó dentro de hola2

#entonces podemos usar esto:
print(local()) #esto técnicamente está ejecutando la función que retornó hola2, es decir, saludo
#------------fin punto 2 ---------------------------------

#------------Punto 3 -------------------------------------
#de igual forma que podemos asignar una función a una variable(referencia), podemos también
#mandar una función como argumento de otra:
def uno_a_diez():
    lista = [x for x in range(1,11)]
    return lista

def contenedora(funcion):
    print(funcion())

contenedora(uno_a_diez)
#-------------fin punto 3--------------------------------- 
#-------------Punto 4-------------------------------------
#que pasaría si nosotros quisieramos saber cuándo se va a ejecutar nuestra función que enviamos como argumentos?

def uno_a_diez2():
    lista = [x for x in range(1,11)]
    return lista

def contenedora2(funcion):
    def notificacion(): #nuestra funcion interna notificación, ejecuta algo antes y después de nuestra funcion parametro
        print("ejecutando función")
        print(funcion())#aquí es cuando se ejecuta la función que originalmente enviamos
        print("terminó la ejecución")

    return notificacion #contenedora2 retorna nuestra función original encapsulada en notificación

#EXPLICACION
#Lo anterior es como si redefinieramos nuestra función original, digamos por ejemplo, si tenemos una funcion:
""" def hey():
    print("hey") """
#el resultado de enviar la función hey a contenedora2 sería como si redefiniéramos hey así:
""" def hey():
    print("ejecutando función")
    print("hey")
    print("terminó la ejecución") """

#Como contenedora2 es una funcion que a su vez retorna una función podemos ejecutar la función que retorna así:
contenedora2(uno_a_diez2)() #este segundo paréntesis ejecuta la función retornada por contenedora2

#notamos que la forma de llamar a la función es un tanto rara
#pero podemos estar un poco más familiarizados haciendo esto:

resultado = contenedora2(uno_a_diez2)
resultado()
#--------------fin punto 4---------------------------
#--------------Punto 5-------------------------------
#pero probablemente esto no es práctico, ya que si quisieramos hacer la misma encapsulación para
#otras funciones, tendríamos que llamar a contenedora2 cada vez, en cambio, podemos hacer lo siguiente
def contenedora3(funcion):
    def notificacion(): #nuestra funcion interna notificación, ejecuta algo antes y después de nuestra funcion parametro
        print("ejecutando función")
        print(funcion())#aquí es cuando se ejecuta la función que originalmente enviamos
        print("terminó la ejecución")

    return notificacion #contenedora2 retorna nuestra función original encapsulada en notificación

@contenedora3 #esta es la forma real de utilizar una decoradora
def pares():
    lista_par = [x for x in range(101) if x % 2 == 0]
    return lista_par

#de esta manera, podemos llamar a la función pares, y veremos que
pares()
#esta ha sido encapsulada dentro de la funcion contenedora

#pero, que pasaría si la función que vamos a encapsular requiere parámetros?
#aquí entran en juego los *args y los **kwargs

def encapsular(funcion):
    def decorar(*args, **kwargs): #simplemente, la encapsuladora decorar, funge como receptora de esos parámetros
        print("antes de ejecutar")
        print(funcion(*args, **kwargs)) # y los envía a la función original
        print("despues de ejecutar")
    
    return decorar

#así, podemos usar nuestra encapsuladora para funciones con parámetros o sin parámetros ahora
@encapsular
def impares(limite):
    lista_impar = [x for x in range(limite) if x % 2 != 0]
    return lista_impar

impares(10)

#----------------fin punto 5 -------------------------------
#----------------punto final -------------------------------
#puede que en este punto te estés preguntando ¿Y esto para qué sirve?, pero imagina por ejemplo un escenario donde
#tienes que validar que todos los argumentos de tu función tengan un cierto tipo de dato:

def validar_enteros(funcion):
    def validado(*args, **kwargs):
        #validamos los args y kwargs
        try: 
            args = [int(x) for x in args] #falla si algún argumento no se puede convertir a entero
        except:
            print("el argumento no es numérico")
            return None #si algun argumento no cumple con ser de tipo entero, no tiene caso ejecutar la función original

        try:
            kwargs = {k: int(v) for k, v in kwargs.items()} #falla si algún argumento no se puede convertir a entero
        except:
            print("el argumento no es numérico")
            return None #mismo caso con los kwargs
        
        return funcion(*args, **kwargs) #si las validaciones tuvieron éxito, entonces si se ejecuta la función original

    return validado #la función regresada puede ser un None si la validación falló, o la función original si todo salió bien

#así podemos usar nuestra decoradora para nuestras validaciones
@validar_enteros
def impares2(limite):
    lista_impar = [x for x in range(limite) if x % 2 != 0]
    return lista_impar

"""
si no quisiera usar la decoradora validar_enteros tendría entonces que definir impares como:
def impares2(limite):
    try: 
        limite = int(limite) #la conversión a int arroja una excepción si el valor pasado no puede convertirse a entero
        lista_impar = [x for x in range(limite) if x % 2 != 0]
        return lista_impar
    except:
        print("El limite no es entero")
        return None
"""

@validar_enteros
def suma(a, b):
    return a + b

"""
De igual forma para la suma:
def suma(a, b):
    try: 
        a = int(a)
        b = int(b)
        return a + b
    except:
        print("uno de los parámetros no es entero")
        return None
"""

#y ver los resultados:
impares2("hola") # imprime el mensaje de error
resultado = impares2(10) # regresa una lista de números impares 
print(resultado) # imprime la lista
print(suma(1,2)) # regresa el resultado de sumar 1 y 2
print(suma("hola", "mundo")) # imprime el mensaje de error, seguido de un None


