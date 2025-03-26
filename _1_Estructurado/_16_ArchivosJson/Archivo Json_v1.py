import json

if __name__ == '__main__':
    with open("Datos.json", "r", encoding="utf-8") as archivo:
        datos= json.load(archivo)

    for persona in datos ["personas"]:
        print("Nombre:", persona["nombre"])
        print("Edad:", persona["Edad"])
        print("Ciudad:", persona["Ciudad"])
        print("Estado:", persona["Estado"])
