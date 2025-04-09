class Auto:
    marca="Honada"
    modelo=1000
    placa="PCH-96-04"

if __name__ == '__main__':

    taxi=Auto()
    miauto=Auto()

    print(taxi.placa)
    miauto.placa="TCV-963-12"
    print(miauto.placa)