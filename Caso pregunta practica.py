'''
		Si yo tuviera una lista de estudiantes con sus calificaciones…
		estudiantes = [["orlando",10], ["pedro", 30], ["juan", 15], ["betty", 50],["alejandra", 12], ["omar", 15], ["sergio",12],["andres",30], ["luis",10]]
		… y yo quisiera saber que alumnos tienen la segunda peor calificación en esa lista, alguien me podría pasar el código?
'''

#Conversion de lista a diccionario
estudiantes = [["orlando",10], ["pedro", 30], ["juan", 15], ["betty", 50],["alejandra", 12], ["omar", 15], ["sergio",12],["andres",30], ["luis",10]]
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


#Mismo resultado pero en dict comprehension == FALLIDO
'''
new_dict_comp = {}
new_dict_comp = {score:[name] if score not in new_dict_comp.keys() else \
    new_dict_comp[score].append(name) for name, score in estudiantes_dict.items()}
print(new_dict_comp)
'''