if __name__ == '__main__':
    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

    listaImpares = list(filter(lambda x: x % 2 == 0, numeros))
    listaPares = list(filter(lambda x: x % 2 == 1, numeros))

    print(f"Lista de numeros pares: {listaImpares}")
    print(f"Lista de numeros impares: {listaPares}")