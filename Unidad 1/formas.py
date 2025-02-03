class Forma:
    """
    Clase base para diferentes formas geométricas.
    """
    def dibujar(self):
        pass

class Circulo(Forma):
    """
    Clase Circulo que hereda de Forma.
    """
    def dibujar(self):
        return "Dibujando un círculo"

class Cuadrado(Forma):
    """
    Clase Cuadrado que hereda de Forma.
    """
    def dibujar(self):
        return "Dibujando un cuadrado"

# Función polimórfica
def renderizar_forma(forma):
    print(forma.dibujar())

# Ejemplo de uso
if __name__ == "__main__":
    formas = [Circulo(), Cuadrado()]
    for forma in formas:
        renderizar_forma(forma)
