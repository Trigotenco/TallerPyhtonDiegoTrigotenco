def suma(a:int,b:int)->int:
    return a+b

def sumaArreglo(lista:list)->int:
    return sum(lista)


if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(f"La suma es {sumaArreglo(lista)}")
    print(f"La suma es {suma(15,22)}")
