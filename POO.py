class Persona:
    """
    Persona hace referencia a las caracterísiticas básicas de una persona  
    Thunder method o constructor porque tienen doble __ al inicio, el primer argumento es una referencia al objeto. 
    El primer parametro de todos los metodos en python, es self. Se puede utilizar otro nombre pero hay que ser consistentes.
    el metodo __str__ retorna un string al momento de intentar imprimir el objeto, esto pasa porque si no lo defininmos, solo imprime el opbjeto, pero no su representacion, no su valor. 
    El __repr__ se usa para lo msimo que el str, solo que python toma como precedencia el str
    Variables estaticas: se pueden utilizar sin necesidad de crear una instancia de la clase - osea es una variable de clase

    """
    def __init__(self, nombre, apellido = "NA", edad = 20):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        #self.__estatura = 1.65   # me dice que el atributo es privado, es decir, no se muestra o utiliza fuera de mi clase. Se pueden manipular desde los metodos de la clase
        self._estatura = 1.65   #Esta protected porue solo tiene un _


    def saludo(self):
        print(f"Hola, me llamo {self.nombre}")

"""
    @property #hace que un metodo se pueda mandar a llamar como si fuera variable fuera de la clase
    def altura(self):
        return self.__estatura

    @altura.settar #creamos un accesor, esto hace que python no lo tome como una funcion
    def altura(self, altura):
        self.__estatura = altura

    def __repr__(self):
        return f"Persona {self.nombre} edad {self.edad} años" 

    def __str__(self):
        return f"Persona {self.nombre} {self.apellido}"

    def __del_(self):
        print("borrado")
"""
class Usuario:
    pass 

class Alumnos(Persona, Usuario):

    generacion = 2021

    def __init__(self, nombre, apellido, edad, semestre, materias):
        super().__init__(nombre, apellido, edad)
        self.semestre = semestre
        self.materias = materias
        if isinstance(materias, list):
            self.materias = materias
        else:
            self.materias = []
        
    def saludo(self):
        super().saludo()
        print(f"curso el semestre {self.semestre} y tengo estas materias {self.materias}")

    def __eq_(self, alumno):
        return self.semestre == alumno.semestre

    def __metodoprivado(self):
        print("este es un metodo privado")
    
    def metodo_publico(self):
        self.__metodoprivado()

pers = Persona("Juan", "Perez", 30)
alumno = Alumnos("pedro", "diaz", 18, 1, ["mate1", "progra1"])
alumno2 = Alumnos("pedro", "diaz", 18, 1, ["mate1", "progra1"])

if alumno == alumno2:
    print("son iguales")
else:
    print("son diferentes")

print(pers.__doc__) # muestra la descripcion que tengamos como strings en la clase 
alumno.saludo()
alumno.metodo_publico()
