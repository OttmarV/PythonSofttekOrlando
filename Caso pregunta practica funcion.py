'''
		Si yo tuviera una lista de estudiantes con sus calificaciones…
		estudiantes = [["orlando",10], ["pedro", 30], ["juan", 15], ["betty", 50],["alejandra", 12], ["omar", 15], ["sergio",12],["andres",30], ["luis",10]]
		… y yo quisiera saber que alumnos tienen la segunda peor calificación en esa lista, alguien me podría pasar el código?
'''

def penultimo(estudiantes):
    #Conversion de lista a diccionario
    estudiantes_dict = dict(estudiantes)
    print(estudiantes_dict)

    #Cambio, scores son keys y nombres son values
    new_dict = {}
    for name, score in estudiantes_dict.items():
        if score not in new_dict.keys():
            new_dict[score] = [name]
        else:
            new_dict[score].append(name)
    print(new_dict)

    #Asignacion de valores requeridos
    calificacion, alumnos = sorted(new_dict.items(), key=lambda x:x[0])[1]
    print("Calificacion: {calificacion} \nAlumnos: {alumnos}".format(calificacion=calificacion, alumnos = ", ".join(alumnos)))


if __name__ == "__main__":
    
    estudiantes = [["orlando",10], ["pedro", 30], ["juan", 15], ["betty", 50],["alejandra", 12], ["omar", 15], ["sergio",12],["andres",30], ["luis",10]]

    penultimo(estudiantes)


