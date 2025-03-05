if __name__ == '__main__':
    nombre = input("Proporciona tu primer nombre: ")
    ap = input("Proporciona tu apellido paterno: ")
    am = input("Proporciona tu apellido materno: ")

    completo = nombre + " " + ap + " " + am
    n = len(completo.replace(" ", ""))  # Quitamos los espacios para contar solo las letras

    print(f"Tu nombre completo es: {completo}")
    print(f"Tu nombre tiene {n} letras")
