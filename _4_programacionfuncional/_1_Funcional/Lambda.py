if __name__ == '__main__':
    lambdaSuma =lambda x,y:x+y
    valor1=int(input("dame un numero: "))
    valor2=int(input("dame otro numero: "))

    suma= lambdaSuma (valor1,valor2)
    print(f"La suma de {valor1} y {valor2} es {suma}")