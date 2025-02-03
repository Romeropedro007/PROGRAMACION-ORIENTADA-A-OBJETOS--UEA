# Clase abstracta que define un modelo básico para figuras geométricas
from abc import ABC, abstractmethod

class Figura(ABC):
    """
    Clase base abstracta para representar figuras geométricas.
    Contiene un método abstracto calcular_area().
    """
    @abstractmethod
    def calcular_area(self):
        pass

class Circulo(Figura):
    """
    Clase Circulo que extiende Figura e implementa calcular_area().
    """
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.1416 * (self.radio ** 2)

class Rectangulo(Figura):
    """
    Clase Rectangulo que extiende Figura e implementa calcular_area().
    """
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.ancho * self.alto

# Ejemplo de uso
if __name__ == "__main__":
    circulo = Circulo(5)
    print("Área del círculo:", circulo.calcular_area())

    rectangulo = Rectangulo(4, 7)
    print("Área del rectángulo:", rectangulo.calcular_area())
