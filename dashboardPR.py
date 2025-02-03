import os
import subprocess

def mostrar_codigo(ruta_script):
    # Asegúrate de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None

def ejecutar_codigo(ruta_script):
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Unix-based systems
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código: {e}")

def mostrar_menu():
    # Define la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'Unidad 1/animales.py',
        '2': 'Unidad 1/cuenta_bancaria.py',
        '3': 'Unidad 1/figura.py',
        '4': 'Unidad 1/formas.py',
        '5': 'Unidad 1/poo.py',
        '6': 'Unidad 1/tradicional.py',
        '7': 'Unidad 2/Tarea semana 6.py',
    }

    while True:
        print("\n******** Menu Principal - Dashboard *************")
        # Imprime las opciones del menú
        for key, value in opciones.items():
            print(f"{key} - {value}")
        print("0 - Salir")

        eleccion = input("Elige un archivo para ver su contenido o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegura que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            codigo = mostrar_codigo(ruta_script)
            if codigo:
                ejecutar = input("¿Desea ejecutar el script? (1: Sí, 0: No): ")
                if ejecutar == '1':
                    ejecutar_codigo(ruta_script)
                elif ejecutar == '0':
                    print("No se ejecutó el script.")
                else:
                    print("Opción no válida. Regresando al menú de scripts.")
                input("\nPresiona Enter para volver al menú principal.")
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()
