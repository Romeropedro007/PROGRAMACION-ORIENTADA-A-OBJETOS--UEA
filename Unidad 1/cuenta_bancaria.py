class CuentaBancaria:
    """
    Clase que representa una cuenta bancaria utilizando encapsulación.
    """
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # Atributo privado

    def depositar(self, cantidad):
        """Método público para depositar dinero."""
        if cantidad > 0:
            self.__saldo += cantidad
        else:
            print("Cantidad inválida.")

    def retirar(self, cantidad):
        """Método público para retirar dinero."""
        if 0 < cantidad <= self.__saldo:
            self.__saldo -= cantidad
        else:
            print("Fondos insuficientes o cantidad inválida.")

    def mostrar_saldo(self):
        """Método público para mostrar el saldo."""
        return f"Saldo actual: {self.__saldo}"

# Ejemplo de uso
if __name__ == "__main__":
    cuenta = CuentaBancaria("Juan Pérez", 1000)
    print(cuenta.mostrar_saldo())
    cuenta.depositar(500)
    print(cuenta.mostrar_saldo())
    cuenta.retirar(300)
    print(cuenta.mostrar_saldo())
