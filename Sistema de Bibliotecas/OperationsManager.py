from Admin import *

class OperationsManager:
    def __init__(self):
        self.admin = Admin()

    def print_menu(self):
        print("Opciones del programa: ")
        options = [
            '1) Añadir libro',
            '2) Imprimir todos los libros',
            '3) Imprimir libros por nombre',
            '4) Añadir usuario',
            '5) Libros prestados',
            '6) Libros devueltos',
            '7) Imprimir libros prestados por usuario',
            '8) Imprimir todos los usuarios'
        ]
        print('\n'.join(options))
        return self.get_choice(len(options))

    def get_choice(self, num_options):
        msg = f" Ingrese su elección del 1 al {num_options} \n: "
        return input_is_valid(msg, 1, num_options)

    def add_book(self):
        book_id = input('Por favor ingrese el id del libro: \n')
        book_name = input('Por favor ingrese el nombre del libro: \n')
        book_quantity = input('Por favor ingrese la cantidad de libros: \n')
        self.admin.add_book(book_id, book_name, book_quantity)

    def print_books(self):
        print(self.admin.print_all_books())

    def search_books(self):
        query = input('Ingrese su consulta: \n')
        print(', '.join(self.admin.search_for_book(query)))

    def add_user(self):
        user_id = int(input('Introduzca el ID de usuario: \n'))
        user_name = input('Introduzca el nombre de usuario: \n')
        self.admin.add_user(user_id, user_name)

    def borrow_book(self):
        user_name = input('Introduzca el nombre de usuario: \n')
        book_name = input('Introduzca el nombre del libro: \n')
        self.admin.borrow_book(user_name, book_name)

    def return_book(self):
        user_name = input('Introduzca el nombre de usuario: \n')
        book_name = input('Introduzca el nombre del libro: \n')
        self.admin.return_book(user_name, book_name)

    def print_users_borrowed(self):
        self.admin.print_users_borrowed()

    def print_all_users(self):
        self.admin.print_all_users()

    def run(self):
        while True:
            choice = self.print_menu()

            if choice == 1:
                self.add_book()
            elif choice == 2:
                self.print_books()
            elif choice == 3:
                self.search_books()
            elif choice == 4:
                self.add_user()
            elif choice == 5:
                self.borrow_book()
            elif choice == 6:
                self.return_book()
            elif choice == 7:
                self.print_users_borrowed()
            elif choice == 8:
                self.print_all_users()
            else:
                print("Saliendo del programa.")
                break