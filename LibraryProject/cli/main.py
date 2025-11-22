import logging
from library_manager.inventory import LibraryInventory
from library_manager.book import Book

logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

inventory = LibraryInventory()

def menu():
    while True:
        print("\n===== Library Manager =====")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. View All Books")
        print("5. Search Book")
        print("6. Exit")
        
        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid input. Try again.")
            continue

        if choice == 1:
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            inventory.add_book(Book(title, author, isbn))
            print("Book added successfully.")

        elif choice == 2:
            isbn = input("Enter ISBN to issue: ")
            book = inventory.search_by_isbn(isbn)
            if book and book.issue():
                inventory.save_books()
                print("Book issued.")
            else:
                print("Book unavailable.")

        elif choice == 3:
            isbn = input("Enter ISBN to return: ")
            book = inventory.search_by_isbn(isbn)
            if book and book.return_book():
                inventory.save_books()
                print("Book returned.")
            else:
                print("Invalid action.")

        elif choice == 4:
            for b in inventory.display_all():
                print(b)

        elif choice == 5:
            title = input("Enter title keyword: ")
            results = inventory.search_by_title(title)
            if results:
                for b in results:
                    print(b)
            else:
                print("No books found.")

        elif choice == 6:
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    menu()

