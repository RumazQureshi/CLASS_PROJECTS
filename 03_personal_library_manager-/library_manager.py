class BookCollection:
    """A simple personal library manager using a text file for storage with book titles as dictionary keys."""

    def __init__(self):
        """Initialize an empty book dictionary and load from file."""
        self.books = {}  #empty book dictionary
        self.file_name = "library.txt" #text file to store book data
        self.load_books()

    def load_books(self):
        """Load books from the text file into a dictionary."""
        try: #exceptional handling
            with open(self.file_name, "r") as file:
                for line in file:
                    title, author, year, genre, read = line.strip().split(" | ")
                    self.books[title.lower()] = {
                        "title": str(title),
                        "author": str(author),
                        "year": int(year),
                        "genre": str(genre),
                        "read":read == "Read"
                    }
        except FileNotFoundError:
            open(self.file_name, "w").close()  # Create new file if not exists

    def save_books(self):
        """Save books to the text file from dictionary storage."""
        with open(self.file_name, "w") as file:
            for book in self.books.values():
                file.write(f"{book['title']} | {book['author']} | {book['year']} | {book['genre']} | {'Read' if book['read'] else 'Unread'}\n")

    def add_book(self):
        """Add a new book to the txt file using dictionary."""
        title = input("Enter the book title: ").strip()
        if title.lower() in self.books:
            print("This book already exists in your library!\n")
            return

        author = (input("Enter the author: ").strip())
        
        while True:
            try:
                year = int(input("Enter the publication year: ").strip())
                break
            except ValueError:
                print("Invalid input! Please enter a valid year.")

        genre = input("Enter the genre: ").strip()
        read = input("Have you read this book? (yes/no): ").strip().lower() == "yes"

        self.books[title.lower()] = {"title": title, "author": author, "year": year, "genre": genre, "read": read}
        self.save_books()
        print("Book added successfully!\n")

    def remove_book(self):
        """Remove a book using its title."""
        title = input("Enter the title of the book to remove: ").strip().lower()
        if title in self.books:
            del self.books[title]
            self.save_books()
            print("Book removed successfully!\n")
        else:
            print("Book not found!\n")

    def search_book(self):
        """Search for books by title or author."""
        search_type = input("Search by:\n1. Title\n2. Author\nEnter your choice (1-2) : ").strip()
        if search_type == "1":
            search_text = input("Enter the book title: ").strip().lower()
        else:
            search_text = input("Enter the author name: ").strip().lower()

        found_books = []
        if search_type == "1":
            found_books = [book for book in self.books.values() if search_text in book["title"].lower()]
        elif search_type == "2":
            found_books = [book for book in self.books.values() if search_text in book["author"].lower()]
        else:
            print("Invalid choice!\n")
            return

        if found_books:
            print("\nMatching Books:")
            for index, book in enumerate(found_books, 1):
                status = "Read" if book["read"] else "Unread"
                print(f"{index}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
        else:
            print("No matching books found.\n")

    def display_books(self):
        """Show all books in the library."""
        if not self.books:
            print("Your library is empty.\n")
            return

        print("\nYour Library:")
        print("=" * 50)
        for index, book in enumerate(self.books.values(), 1):
            status = "Read" if book["read"] else "Unread"
            print(f"{index}. {book['title']} | {book['author']} | {book['year']} | {book['genre']} | {status}")
        print("=" * 50)

    def display_statistics(self):
        """Show total books and reading percentage."""
        total_books = len(self.books)
        read_books = sum(1 for book in self.books.values() if book["read"])
        read_percentage = (read_books / total_books * 100) if total_books else 0

        print(f"Total Books: {total_books}")
        print(f"Percentage Read: ({read_percentage:.2f}%)\n")

    def run(self):
        """Start the program with a menu."""
        while True:
            print("\nWelcome to Your Personal Library Manager!")
            print("1. Add a book")
            print("2. Remove a book")
            print("3. Search for a book")
            print("4. Display all books")
            print("5. Display statistics")
            print("6. Exit")
            choice = input("Enter your choice (1-6): ").strip()

            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.remove_book()
            elif choice == "3":
                self.search_book()
            elif choice == "4":
                self.display_books()
            elif choice == "5":
                self.display_statistics()
            elif choice == "6":
                print("Library saved to file. Goodbye!")
                break
            else:
                print("Invalid choice! Please try again.\n")


if __name__ == "__main__":
    manager = BookCollection()
    manager.run()
