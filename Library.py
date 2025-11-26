# Implement a student library system using OOPs where students can burrow from a list of books.
# create a separate library and student class. Your program must be the menu driver.

class Library:
    def __init__(self, books):
        self.books = books   # list of available books

    def display_books(self):
        print("\n--- Available Books ---")
        if not self.books:
            print("No books left in the library.")
            return
        for idx, book in enumerate(self.books, start=1):
            print(f"{idx}. {book}")

    def borrow_book(self, book_name):
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"✔ '{book_name}' has been borrowed.")
            return True
        else:
            print("✘ Book not available.")
            return False

    def return_book(self, book_name):
        self.books.append(book_name)
        print(f"✔ '{book_name}' has been returned to the library.")


class Student:
    def __init__(self, name):
        self.name = name
        self.borrowed = []   # books the student borrowed

    def request_book(self):
        book_name = input("Enter the name of the book to borrow: ")
        return book_name

    def return_book(self):
        book_name = input("Enter the name of the book to return: ")
        return book_name


# -------------------- MENU DRIVER --------------------
def main():
    library = Library(["Python Basics", "Data Structures", "Algorithms", "Machine Learning", "AI Essentials"])
    student = Student("Artt")

    while True:
        print("\n===== STUDENT LIBRARY MENU =====")
        print("1. Display available books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. View my borrowed books")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            library.display_books()

        elif choice == "2":
            book = student.request_book()
            if library.borrow_book(book):
                student.borrowed.append(book)

        elif choice == "3":
            book = student.return_book()
            if book in student.borrowed:
                student.borrowed.remove(book)
                library.return_book(book)
            else:
                print("✘ You did not borrow this book.")

        elif choice == "4":
            print("\n--- Your Borrowed Books ---")
            if not student.borrowed:
                print("You have not borrowed any books.")
            else:
                for b in student.borrowed:
                    print(f"- {b}")

        elif choice == "5":
            print("Exiting program...")
            break

        else:
            print("Invalid option! Try again.")


if __name__ == "__main__":
    main()
