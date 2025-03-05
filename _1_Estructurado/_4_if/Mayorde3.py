if __name__ == '__main__':
    nombre1 = input("Introduce el primer nombre: ")
    nombre2 = input("Introduce el segundo nombre: ")

    if len(nombre1) > len(nombre2):
        print(f"El nombre con más letras es: {nombre1}")
    elif len(nombre2) > len(nombre1):
        print(f"El nombre con más letras es: {nombre2}")
    else:
        print("Ambos nombres tienen la misma cantidad de letras.")