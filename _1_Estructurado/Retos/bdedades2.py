import json
import sys
from logging import exception

BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
RESET = "\033[0m"

def extrae():
    archivo = open("edadesbd.Json", "r", encoding="utf-8")
    try:
        usuarios = json.load(archivo)
        for usuario in usuarios["personas"]:
            yield usuario["id"], usuario["nombre"], usuario["edad"], usuario["RFC"]

    except FileExistsError:
        print(MAGENTA, "¡Error! El archivo no existe")
    except json.JSONDecodeError:
        print(YELLOW, "¡Error! El archivo no contiene un JSON valido")
    except exception as e:
        print(CYAN, "Pues no se que ocurrio", e)
    else:
        archivo.close()
        print(RESET, "Archivo JSONcerrado")



if __name__ == '__main__':


    i = 1
    for id_, nombre, edad, RFC in extrae():
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
