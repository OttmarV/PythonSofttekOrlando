x = []
x = list() #[]
x = [1, 2, 3, 4]
x = [True, 1.01, 10, "hola"]
print(x)
print(*x) # Desempaquetar
print(x[3])

#agregar elemento
x.append("manzana")
print(x)

#Insertar
x.insert(1,False)
print(x)

#Replace
x[2] = "uva"
print(x)

#Pedir a usuario
y = input()
print(y)

#remover ultimo
print(x.pop())
print(x.pop(0))
print(x)

#Remover valor
#x.remove(True)
#print(x)

#tamaño de lista
print(len(x))

#añadir listas
y = [1,2,3,4]
z = [4,5,6,7]

lista = y + z
print(lista)
y.extend(z)
print(y)

#iterar lista
for item in lista:
    print(item)

#forma 2
#5
#0,1,2,3,4
for iter in range(len(lista)):
    print(lista[iter])

print(lista)
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)

#slicing
print(lista[::2])
print(lista[::-1])


