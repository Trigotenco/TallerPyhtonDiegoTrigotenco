def extrae(agenda:tuple):
    i:int=0
    while(i<len(agenda)):
        nombre,correo,tel = agenda[i]
        i+=1
        yield agenda[i]
if __name__ == '__main__':

    agenda=[]
    agenda.append(("Juan1","juan1@gmail.com","221586985"))
    agenda.append(("Juan2", "juan2@gmail.com", "222586985"))
    agenda.append(("Juan3", "juan3@gmail.com", "224586985"))
    agenda.append(("Juan4", "juan4@gmail.com", "225586985"))
    agenda.append(("Juan5", "juan5@gmail.com", "226586985"))
    agenda.append(("Juan6", "juan6@gmail.com", "227586985"))
    agenda.append(("Juan7", "juan7@gmail.com", "228586985"))
    agenda.append(("Juan8", "juan8@gmail.com", "229586985"))
    agenda.append(("Juan9", "juan9@gmail.com", "221186985"))
    agenda.append(("Juan10", "juan10@gmail.com", "221086985"))

    for a,b,c in extrae(agenda):
        print("-" * 30)
        print(f"ID: {a}")
        print(f"Nombre: {b}")
        print(f"Correo: {c}")
        print("-" * 30)

