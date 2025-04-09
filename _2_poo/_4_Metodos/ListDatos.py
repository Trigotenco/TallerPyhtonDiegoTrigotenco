class ListaDtos:

    def __init__(self, matricula:str,  estidiante:str, asignatura:str):
        self.matrucula=matricula
        self.estudiante=estidiante
        self.asignatura=asignatura

if __name__ == '__main__':
    lista=[]
    lista.append(ListaDtos("1258658", "Juan Carlos", "matematicas"))
    lista.append(ListaDtos("1258658", "Memin Pinwin","ingles"))
    lista.append(ListaDtos("1258658", "Pororo meme","ciencias"))
    lista.append(ListaDtos("1258658", "Paola Flores","taller"))

    for obj in lista:
        print(f"Matricula: {obj.matrucula}")
        print(f"Nombre: {obj.estudiante}")
        print(f"Asignatura: {obj.asignatura}")
        print(f"----------------------------")
