'''
		Si yo tuviera una lista de estudiantes con sus calificaciones…
		estudiantes = [["orlando",10], ["pedro", 30], ["juan", 15], ["betty", 50],["alejandra", 12], ["omar", 15], ["sergio",12],["andres",30], ["luis",10]]
		… y yo quisiera saber que alumnos tienen la segunda peor calificación en esa lista, alguien me podría pasar el código?
'''

#Conversion de lista a diccionario
estudiantes = [["orlando",10], ["pedro", 30], ["juan", 15], ["betty", 50],["alejandra", 12], ["omar", 15], ["sergio",12],["andres",30], ["luis",10]]
#print(sorted(estudiantes, key=lambda x:x[1])) #Con esta linea podemos ver el sort a la lista, pero ya se hace en la linea 25
#estudiantes_dict = dict(sorted(estudiantes, key=lambda x:x[1])) #Esta linea se puede utilizar si en la linea 25 no se hace el sorted

estudiantes_dict = dict(estudiantes)
print(estudiantes_dict)

#Diccionario donde scores son keys y nombres son values
new_dict = {}
for name, score in estudiantes_dict.items():
    if score not in new_dict.keys():
        new_dict[score] = [name]
    else:
        new_dict[score].append(name)
print(new_dict)

#Ordena e imprime los elementos del segundo valor mas bajo, si no se usa esta linea, descomentar linea 11
calificacion, alumnos = sorted(new_dict.items(), key=lambda x:x[0])[1]
print("Calificacion: {calificacion} \nAlumnos: {alumnos}".format(calificacion=calificacion, alumnos = ", ".join(alumnos)))


'''
#Esto se puede utilizar con el new_dict que sale desde la linea 22, se comenta linea 25 y descomenta linea 11
values_view = new_dict.values()
values_iterator = iter(values_view)
first_value = next(values_iterator)
second_value = next(values_iterator)
print(second_value)
'''

#Mismo resultado pero en dict comprehension == FALLIDO
'''
new_dict_comp = {}
new_dict_comp = {score:[name] if score not in new_dict_comp.keys() else \
    new_dict_comp[score].append(name) for name, score in estudiantes_dict.items()}
print(new_dict_comp)
'''