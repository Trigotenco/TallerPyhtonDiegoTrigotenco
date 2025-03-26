if __name__ == '__main__':
    diccionario = {
        """
        ("id", "int"):'2',
        'nombre':'Juan',
        'apellido':'Gutierrez'
        
        """
    }

    diccionario[("Ana", 25)]="Estudiante"
    diccionario[("Luis", 30)]="Ingeniero"
    diccionario[("Carlos", 40)]="Abogado"

    ocupacion_ana = diccionario[("Ana", 25)]
    ocupacion_Luis = diccionario[("Luis", 30)]

    print(f"Ana es: {ocupacion_ana}")
    print(f"Luis es: {ocupacion_Luis}")

