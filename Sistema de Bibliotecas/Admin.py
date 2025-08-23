from Book import *
from User import *
from utility import *


class Admin:
    def __init__(self):
        self.books = []  # objeto del libro
        self.users = {}  # objeto de usuario como clave

    def add_book(self, book_id, book_name, book_quantity):
        for book in self.books:
            if book.id == book_id:
                return print("Este libro ya existe")
        new_book = Book(book_id, book_name, book_quantity)
        self.books.append(new_book)
        print("El libro se agregó correctamente")

    def print_all_books(self):
        lst_of_books = []
        for book in self.books:
            lst_of_books.append(book.name)
        if not lst_of_books:
            return f"No hay libros"
        return ", ".join(lst_of_books)

    def search_for_book(self, query):
        found_books = [book.name for book in self.books if book.name[:len(query)].upper() == query.upper()]
        if not found_books:
            return f"No se encontró ningún libro"
        return found_books

    def add_user(self, user_id, user_name):
        for user in self.users:
            if user.id == user_id:
                return print(f"Este usuario ya existe!")
        new_user = User(user_id, user_name)
        self.users[new_user] = None
        print("Usuario creado con éxito!")

    def borrow_book(self, user_name, book_name):
        found_book = ''.join(self.search_for_book(book_name))
        user_found = False
        available_books = [book for book in self.books if book.name == found_book and book.quantity > 0]
        if not available_books:
            return print("Cantidad insuficiente!")
        available_books[0].quantity -= 1
        for user, values in self.users.items():
            if user.name.lower() == user_name.lower():
                if values is None:
                    self.users[user] = [book_name]
                else:
                    self.users[user].append(book_name)
                user_found = True
        if not user_found:
            return print('No hay ningún usuario con este nombre')
        return print(F'El usuario{user_name} lo tiene {found_book}')

    def return_book(self, user_name, book_name):
        found_book = ''.join(self.search_for_book(book_name))
        user_found = False
        available_books = [book for book in self.books if book.name == found_book]
        if not available_books:
            return print("No existe ningún libro con este nombre")
        available_books[0].quantity += 1
        for user, values in self.users.items():
            if user.name.lower() == user_name.lower():
                if len(values) == 1:
                    self.users[user] = None
                else:
                    self.users[user].remove(book_name)
                user_found = True
        if not user_found:
            return print('No hay ningún usuario con este nombre')
        return print(F'El usuario{user_name} devolvio {found_book}')

    def print_users_borrowed(self):
        users_found = [user for user in self.users if self.users[user] is not None]
        if users_found:
            for user in users_found:
                print(f'El usuario {user.name} tomó prestados los libros {" y ".join(self.users[user])}')
        else:
            print('No hay usuarios que tomen prestado ningún libro')

    def print_all_users(self):
        all_users = [user.name for user in self.users]
        if all_users:
            for user in all_users:
                print(user, end=' ')