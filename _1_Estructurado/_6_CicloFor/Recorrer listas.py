if __name__ == '__main__':
    print("________________________________")
    lista=[1,2,3,"Lunes",4,5,6,7,8,9,10,11,12,13,14,15,16]


    lista.append(200)
    lista.append("Viernes")
    lista.append(False)
    lista.append(2.69)

    lista2=[1200,1300,1500]
    lista.append(lista2)

    for elemento in lista:
        print(elemento)

    lista2=[17, 18, 19, 20]
    lista.extend(lista2)

    nombre:str
    nombre="Luis "
    nombre += "Gutierrez "
    #nombre.join("Gutierrez")
    print(nombre)

    lista3=["Federico", "Pablo", "Karla"]
    cadena:str="-".join(lista3)
    print(cadena)
    
    separado=cadena.split()
    for dato in separado:
        print(dato)