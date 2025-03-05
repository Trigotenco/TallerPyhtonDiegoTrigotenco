if __name__ == '__main__':
    x=int(input("Ingresa un numero: "))
    y=int(input("Ingresa otro numero: "))

    i:int=1
    mult:int=1

    while i<y:
        mult=x*y
        i=i+1

    print(f"El resultado de {x} y {y} = {mult}")