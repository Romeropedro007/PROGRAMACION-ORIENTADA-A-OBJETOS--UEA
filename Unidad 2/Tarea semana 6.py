# Clase base que representa a una persona
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributos encapsulados
        self.__edad = edad

    def get_nombre(self):  # Getter para el nombre
        return self.__nombre

    def set_nombre(self, nombre):  # Setter para el nombre
        self.__nombre = nombre

    def get_edad(self):  # Getter para la edad
        return self.__edad

    def set_edad(self, edad):  # Setter para la edad con validación
        if edad > 0:
            self.__edad = edad
        else:
            print("La edad debe ser un número positivo.")

    # Método que devuelve una descripción general de la persona
    def descripcion(self):
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}"


# Clase derivada que representa a un estudiante (herencia)
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    def descripcion(self):  # Sobrescritura del método descripcion
        return f"Nombre: {self.get_nombre()}, Edad: {self.get_edad()}, Carrera: {self.carrera}"


# Clase derivada que representa a un profesor (herencia)
class Profesor(Persona):
    def __init__(self, nombre, edad, especialidad):
        super().__init__(nombre, edad)
        self.especialidad = especialidad

    def descripcion(self):  # Sobrescritura del método descripcion
        return f"Nombre: {self.get_nombre()}, Edad: {self.get_edad()}, Especialidad: {self.especialidad}"


# Punto de entrada del programa
if __name__ == "__main__":
    # Instancia de la clase base Persona
    persona = Persona("Carlos", 45)
    print(persona.descripcion())

    # Instancia de la clase derivada Estudiante
    estudiante = Estudiante("Ana", 20, "Ingeniería en Sistemas")
    print(estudiante.descripcion())

    # Instancia de la clase derivada Profesor
    profesor = Profesor("María", 35, "Matemáticas")
    print(profesor.descripcion())

    # Modificación de atributos encapsulados
    estudiante.set_nombre("Andrea")
    estudiante.set_edad(21)
    print(estudiante.descripcion())
