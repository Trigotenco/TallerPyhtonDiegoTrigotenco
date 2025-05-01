import mariadb


def conectar_y_consultar():
    try:
        conexion = mariadb.connect(
            host="localhost",
            database="almacen",
            user="root",
            password="",
            port=3306
        )
        print(type(conexion))
        print("Conexion a la base de datos del servidor Ounus")

        cursor = conexion.cursor()
        consulta= "select * from Usuarios"
        cursor.execute(consulta)

        resultados= cursor.fetchall()
        print("Resultado", type(resultados))
        print("Datos en la tabla: ")
        for fila in resultados:
            print(f"| ID: {fila[0]}| ID_Rol: {fila[1]}| Nombre del Usuario: {fila[2]}| Correo Electronico: {fila[3]}| Contrasennia: {fila[4]}")
            print("_"*170+"|")

        consulta = "SELECT * FROM Roles"
        cursor.execute(consulta)

        resultados = cursor.fetchall()
        print("Resultado", type(resultados))
        print("Datos en la tabla Roles: ")
        for fila in resultados:
            print(f"| ID_Rol: {fila[0]} | Nombre del Rol: {fila[1]}")
            print("_" * 170 + "|")

    except mariadb.Error as e:
        print(f"Error al conectar con la base de datos: {e}")

    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
            print("conexion cerrada")


if __name__ == '__main__':
    conectar_y_consultar()
