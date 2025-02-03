class Animal:
    """
    Clase base para representar un animal genérico.
    """
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass

class Perro(Animal):
    """
    Clase Perro que hereda de Animal.
    """
    def hacer_sonido(self):
        return "Guau Guau"

class Gato(Animal):
    """
    Clase Gato que hereda de Animal.
    """
    def hacer_sonido(self):
        return "Miau Miau"

# Ejemplo de uso
if __name__ == "__main__":
    perro = Perro("Firulais")
    gato = Gato("Michi")

    print(f"El perro {perro.nombre} dice: {perro.hacer_sonido()}")
    print(f"El gato {gato.nombre} dice: {gato.hacer_sonido()}")
