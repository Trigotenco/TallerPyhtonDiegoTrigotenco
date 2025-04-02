import json
import sys

BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
RESET = "\033[0m"

def extrae(usuarios):
    for usuario in usuarios:
        yield usuario["id"], usuario["nombre"], usuario["edad"], usuario["RFC"]

if __name__ == '__main__':
    with open("edadesbd.Json", "r", encoding="utf-8") as archivo:
        datos = json.load(archivo)

    i = 1
    for id_, nombre, edad, RFC in extrae(datos["personas"]):
        match i % 3:
            case 1:
                sys.stdout.write(YELLOW)
            case 2:
                sys.stdout.write(BLUE)
            case 3:
                sys.stdout.write(CYAN)
            case _:
                sys.stdout.write(RESET)

        print("-" * 30)
        print(f"ID: {id_}")
        print(f"Nombre: {nombre}")
        print(f"Edad: {edad}")
        print(f"RFC: {RFC}")

        if edad >= 18:
            print("Estatus: Mayor de edad")
        else:
            print("Estatus: Menor de edad")

        print("-" * 30)
        sys.stdout.write(RESET)
        i += 1
