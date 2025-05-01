class DatosPersonales:

    def __init__(self, nombre, apellido, edad):
        self.nombre=nombre
        self.apelllido=apellido
        self.edad=edad

    def getNombre(self):
        return self.nombre
    def getApellido(self):
        return self.apelllido
    def getEdad(self):
        return self.edad

    def corto(self):
        return self.nombre + " " + self.apelllido + " " + self.edad + " años"

    def __str__(self):
        return self.nombre + " " + self.apelllido + " " + self.edad + " años"

if __name__ == '__main__':

        datos = DatosPersonales("Hector", "Flores", "23")
        print(datos)