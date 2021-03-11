
#Son inmutables
#pueden almacenar numeros distintos
#se pueden iterar

color = (255,255,255) #blanco
position = (100, 500)
mytuple= (1, "hola", 1.5, [1,2,3])

print(mytuple[1])

x, y = position
print(x,y)

a, b, c, d = mytuple
print(a,b,c,d)

a = mytuple[0]
b = mytuple[-1]

a, *_, b = mytuple
print(a, _, b)

ayuda = list(mytuple)
ayuda.append("otro")
mytuple = tuple(ayuda)

print(mytuple)

print(mytuple[3][1])