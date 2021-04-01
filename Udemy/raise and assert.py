
"""
Programa para imprimir una caja
"""
import traceback

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception("Symbol should be a string of length 1")
    if (width < 2) or (height < 2):
        raise Exception("width and height should be < 2 in length")
    
    print(symbol * width)

    for _ in range(height - 2):
        print(symbol + " " * (width-2) + symbol)
    
    print(symbol * width)

boxPrint("*", 10, 10)

#Escribe en log si hay una excpecion
try: 
    raise Exception("This is the error message")
except:
    errorFile = open("Udemy\\Error log.txt", "a")
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print("The traceback info was written error_log2.txt")

#Assertion practice: se utilizan para detectar errores del programa que no se espera que se recuperen
# a diferencia de las exceptions, los assertions detectan errores en el programa, y las exceptions errores del usuario. 

market_2nd = {'ns':'green', 'ew':'red'}

def switchLights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = "green"

    assert "red" in intersection.values(), "Neither light is red!! " + str(intersection) #nos ayuda a verificar statements, si el assert falla el prgrama debe crashear

print(market_2nd)
switchLights(market_2nd)
print(market_2nd)

