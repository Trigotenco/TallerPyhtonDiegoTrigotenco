#def potencia(x:int)-> int:
 #   return int (pow(x,2))

if __name__ == '__main__':
    numeros =[1,2,3,4,5,6,7,8,9,10,11,12,13,14]

    print(f"Numeros originales: {numeros}")

    potencia=lambda x:x * x
    numerosCuadrados=list(map(potencia,numeros))
    print(f"Numeros con una funcion: {numerosCuadrados}")