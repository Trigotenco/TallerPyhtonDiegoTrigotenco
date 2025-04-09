class ListaDatos:

    def __init__(self, matricula: str, estudiante: str, asignatura: str):
        self.matricula = matricula
        self.estudiante = estudiante
        self.asignatura = asignatura


class ControlEscolar(ListaDatos):

    def __init__(self):
        self.lista=[]

    def addEstudiante(self,matricula, estudiante, asignatura):
        self.lista.append(ListaDatos(matricula,estudiante,asignatura))

    def show(self):
        for obj in self.lista:
            print(f"{obj.matricula}")
            print(f"{obj.estudiante}")
            print(f"{obj.asignatura}")



if __name__ == '__main__':
    escolar=ControlEscolar()
    escolar.addEstudiante("123456", "Paloma Suarez", "ingles")
    escolar.show()