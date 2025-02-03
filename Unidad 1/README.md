# Programacion-orientada-a-objetos
Técnicas de Programación Orientada a Objetos

Este repositorio contiene los ejemplos prácticos desarrollados para la tarea de Técnicas de Programación de la asignatura "Programación Orientada a Objetos". Los ejemplos implementan las principales técnicas de POO: abstracción, encapsulación, herencia y polimorfismo.

Estructura del Repositorio

El repositorio está organizado en carpetas, cada una representando una de las técnicas de POO:

Abstracción/: Contiene ejemplos que demuestran cómo simplificar la realidad modelando solo los aspectos esenciales de los objetos.

Encapsulación/: Contiene ejemplos que muestran cómo ocultar los detalles internos de un objeto y exponer solo lo necesario.

Herencia/: Incluye ejemplos de reutilización de código mediante clases que heredan atributos y métodos.

Polimorfismo/: Muestra cómo tratar objetos de diferentes clases de manera uniforme usando interfaces comunes.

Cada carpeta incluye el archivo Python correspondiente con su implementación.

Descripción de las Técnicas

1. Abstracción

La abstracción permite centrarse en los detalles relevantes de un objeto y ocultar los aspectos innecesarios.

Ejemplo: Implementación de una clase base abstracta Figura y clases derivadas como Circulo y Rectangulo que implementan un método abstracto calcular_area().

Ubicación del código: Abstracción/figura.py

2. Encapsulación

La encapsulación protege los datos de acceso no autorizado mediante atributos privados y métodos para manipularlos.

Ejemplo: Clase CuentaBancaria con atributos privados (__saldo) y métodos públicos depositar, retirar y mostrar_saldo.

Ubicación del código: Encapsulación/cuenta_bancaria.py

3. Herencia

La herencia facilita la reutilización de código al permitir que una clase hija derive atributos y métodos de una clase base.

Ejemplo: Clases Perro y Gato que heredan de la clase base Animal, cada una implementando su propio método hacer_sonido().

Ubicación del código: Herencia/animales.py

4. Polimorfismo

El polimorfismo permite que diferentes clases compartan una misma interfaz y sean tratadas de manera uniforme.

Ejemplo: Clases Circulo y Cuadrado que implementan un método dibujar(), permitiendo que objetos de ambas clases sean utilizados con una función genérica renderizar_forma().

Ubicación del código: Polimorfismo/formas.py
