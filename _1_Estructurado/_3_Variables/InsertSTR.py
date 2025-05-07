from idlelib.query import Query
from tkinter.constants import INSERT

if __name__ == '__main__':
    palabra: str="%s"
    lista: list=["nombre","apellito_paterno","edad","correo electronico","contrasennia"]

    """
    palabra=palabra
    print(palabra)
    """


    t=len(lista)
    print(t)

    palabra=palabra*len(lista)

    Campos=", ".join(lista) # "nombre apellito_paterno edad correo electronico contrasennia"
    print(Campos)

    querySQL=f"INSERT INTO tabla ({Campos})"
    print(querySQL)

    QuerySQL=f"INSERT INTO tabla ({Campos})" + f"VALUES ({palabra})"
    print(QuerySQL)