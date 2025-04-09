"""

desarrollar un programa en python que utilice
la poo para registrar un libro
los atributos debe de estar en privado
debe tener un constructor para el registro
debes tener solo getters de cada atributos
en la otra clase debe regitrar una coleccion de libros
en esta clase debes tener add, delate y show

"""
class Libro:
    def __init__(self, titulo, autor, anio):
        self.__titulo = titulo
        self.__autor = autor
        self.__anio = anio

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_anio(self):
        return self.__anio


class ColeccionLibros:
    def __init__(self):
        self.__libros = []

    def add(self, libro):
        self.__libros.append(libro)
        print(f" Libros Disponibles: '{libro.get_titulo()}'")
        print(f"_____________________________________________________________________________________________________")

    def delete(self, titulo):
        for libro in self.__libros:
            if libro.get_titulo() == titulo:
                self.__libros.remove(libro)
                print(f" Libro eliminado: '{titulo}'")
                return
        print(f"Libro '{titulo}' no encontrado en la colección.")
        print(f"_____________________________________________________________________________________________________")


    def show(self):
        if not self.__libros:
            print(" La colección está vacía.")
            print(f"_____________________________________________________________________________________________________")

        else:
            print("\nLista de libros Actualizado:")
            for i, libro in enumerate(self.__libros, start=1):
                print(f"{i}. Título: {libro.get_titulo()}, Autor: {libro.get_autor()}, Año: {libro.get_anio()}")
                print(f"_____________________________________________________________________________________________________")



if __name__ == "__main__":
    coleccion = ColeccionLibros()

    libro1 = Libro("1984", "George Orwell", 1949)
    libro2 = Libro("Fahrenheit 451", "Ray Bradbury", 1953)
    libro3 = Libro("El periquillo sarniento", "José Joaquín Fernández de Lizardi", 1816 )
    libro4 = Libro("El diario de Ana Frank", "Ana Frank", 1942)
    libro5 = Libro("Cien años de soledad", " Gabriel García Márquez", 1967)

    coleccion.add(libro1)
    coleccion.add(libro2)
    coleccion.add(libro3)
    coleccion.add(libro4)
    coleccion.add(libro5)

    coleccion.show()

    coleccion.delete("1984")

    coleccion.show()
