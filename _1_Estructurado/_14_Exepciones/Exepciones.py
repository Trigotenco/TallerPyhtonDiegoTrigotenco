if __name__ == '__main__':
    try:
        numero=int(input("introduce un numero: "))
        resultado = 10 / numero
    except ValueError:
        print("¡Error¡ Debes introducir un numero entero. ")
    except ZeroDivisionError:
        print("¡Error¡ Debes introducir un numero entero. ")
    else:
        print("El resultado es:", resultado)
    finally:
        print("fin del programa")
