import matplotlib.pyplot as plt


class Book:
    def __init__(self, title):
        self.title = title
        self.is_borrowed = False


class Library:
    def __init__(self):
        self.all_books = []

    def add_a_book(self, title):
        book = Book(title)
        self.all_books.append(book)
        print(f"Book {title} added to library")

    def borrow_a_book(self, title):
        for book in self.all_books:
            if book.title == title:
                if not book.is_borrowed:
                    book.is_borrowed = True
                    print(f"You borrowed {title}")
                else:
                    print(f"{title} is already borrowed")
        print(f"Book {title} not found in the library")

    def visualize_available_books(self):
        available_books = [book.title for book in self.all_books if not book.is_borrowed]
        borrowed_books = [book.title for book in self.all_books if book.is_borrowed]
        titles = list(set(available_books + borrowed_books))
        available_counts = [available_books.count(title) for title in titles]
        borrowed_counts = [borrowed_books.count(title)for title in titles]

        x = range(len(titles))
        plt.bar(x, available_counts)
        plt.bar(x, borrowed_counts)
        plt.title("library Book Status", fontsize=16)
        plt.xlabel("Book titles")
        plt.ylabel("Number of books", fontsize=14)
        plt.xticks(x, titles)
        plt.show()


def main():
    library = Library()
    while True:
        print("Welcome to Library Management System!")
        print("Operation Menu:")
        print("1. Add a book")
        print("2. Borrow a book")
        print("3. Visualize available books")
        print("4. Exit")
        choice = int(input("Please choose your operation (1-4) "))
        if choice == 1:
            title = input("Enter thr book title: ")
            library.add_a_book(title)
        elif choice == 2:
            title = input("Enter thr book title: ")
            library.borrow_a_book(title)
        elif choice == 3:
            library.visualize_available_books()
        elif choice == 4:
            input("Program shutting down.. please press Enter ")
            break
        else:
            print("Invalid choice.. Try again ")


if __name__ == "__main__":
    main()
