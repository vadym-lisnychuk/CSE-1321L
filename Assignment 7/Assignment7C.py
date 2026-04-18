class Book:
    def __init__(self, title):
        self.title = title
        self.is_borrowed = False
    def borrow(self):
        if self.is_borrowed:
            print("This book is borrowed")
        else:
            print(f'You borrowed "{self.title}".')
            self.is_borrowed = True
        
    def return_book(self):
        if self.is_borrowed:
            print(f'You returned "{self.title}".')
            self.is_borrowed = False
        else:
            print(f'Error: "{self.title}" was not borrowed.')

    def display_info(self, index):
        if self.is_borrowed:
            status = "Borrowed"
        else:
            status = "Available"

        print(f"{index} - {self.title} ({status}) ")

class Library:
    def __init__(self):
        self.books = [ Book("Python Basics") , Book("Intro to AI")]
    def show_books(self):
        print("Books in Library:")
        ix = 0
        for i in self.books:
            i.display_info(ix)
            ix += 1

    def borrow_book(self):
        ix = 0
        for i in self.books:
            if i.is_borrowed:
                pass
            else:
                i.display_info(ix)
            ix += 1

        choice = int(input("Select a book to borrow: "))

        try:
            self.books[choice].borrow()
        except IndexError:
            print("out of range")

    def return_book(self):
        ix = 0
        for i in self.books:
            i.display_info(ix)
            ix += 1

        
        choice = int(input("Select a book to return: "))

        try:
            self.books[choice].return_book()
        except IndexError:
            print("out of range")

    def add_book(self):
        title = input("Enter the title of the new book: ")
        self.books.append(Book(title))
        print(f'"{title}" has been added to the library!')


def main():
    lib = Library()

    while True:
        print("[Owl Library]\n1. View Books\n2. Borrow Book\n3. Return Book\n4. Add Book\n5. Exit")
        option = int(input("> "))
        print()
        match option:
            case 1:
                lib.show_books()
            case 2:
                lib.borrow_book()
            case 3:
                lib.return_book()
            case 4:
                lib.add_book()
            case 5:
                print("Exiting program... Goodbye!")
                break
        print()

if __name__ == "__main__":
    main()