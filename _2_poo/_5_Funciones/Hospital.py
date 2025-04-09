class Hospital:

    def __init__(self):
        self.__NombrePaciente:str="hrthrhy"
        self.__nss:int=1258
        self.__enfermedad:str="covid"

    def getNombrePaciente(self)->str:
        return  self.__NombrePaciente

    def getNns(self) -> str:
        return self.__nns

    @property
    def getEnfermedad(self) -> str:
        return self.__enfermedad

    def setNombrePaciente(self, nombre:str):
        self.__NombrePaciente=nombre

    def setNss(self, nss:str):
        self.__Nss=nss

    def setEnfermedad(self, enfermedad:str):
        self.__enfermedad=enfermedad

if __name__ == '__main__':
    pass
    hospital=Hospital()
    hospital.__NombrePaciente="Juan"

