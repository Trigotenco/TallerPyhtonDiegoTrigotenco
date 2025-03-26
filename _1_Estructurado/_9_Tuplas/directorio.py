from itertools import count

if __name__ == '__main__':
    agenda={}

    agenda["GOAT800717"]=("Tomas Gonzalez","csctomasgonzalez@gmail.com","2228274937")
    agenda["GOAT800718"]=("Luis Gonzalez","cluis378@gmail.com","2228529367")
    agenda["GOAT800719"]=("Fabiola Gonzalez","Fabis25@gmail.com","2228529367")
    agenda["GOAT800718"]=("Fernando Gonzalez","fergon56@gmail.com","2228529367")

    nombre,correo,numero=["GOAT800717"]

    def contar_hasta(n)-> tuple[str, int]:
        count=1
        potencia=0

        while count<=n