# Роли пользователей и их функционал

class Reader:
    def register(self):
        print("Регистрация пользователя")

    def view_books(self):
        print("Просмотр доступных книг")

    def search_books(self, query):
        print(f"Поиск книг по: {query}")

    def book_book(self, book):
        print(f"Бронирование книги: {book}")

    def cancel_booking(self, book):
        print(f"Отмена бронирования книги: {book}")

    def view_history(self):
        print("Просмотр истории бронирований")


class Librarian(Reader):
    def add_book(self, book):
        print(f"Добавление книги: {book}")

    def remove_book(self, book):
        print(f"Удаление книги: {book}")

    def issue_book(self, book, reader):
        print(f"Выдача книги '{book}' читателю {reader}")

    def return_book(self, book, reader):
        print(f"Возврат книги '{book}' от читателя {reader}")

    def view_active_bookings(self):
        print("Просмотр списка активных бронирований")

    def manage_catalog(self):
        print("Управление каталогом книг")


class Admin(Librarian):
    def manage_branches(self):
        print("Управление филиалами библиотеки")

    def manage_accounts(self):
        print("Управление учетными записями пользователей и библиотекарей")

    def view_analytics(self):
        print("Просмотр аналитики (выданные книги, популярные книги и т.д.)")


# Пример использования
reader = Reader()
reader.register()
reader.view_books()

librarian = Librarian()
librarian.add_book("Python для начинающих")
librarian.issue_book("Python для начинающих", "Ерсултан")

admin = Admin()
admin.manage_branches()
admin.view_analytics()
