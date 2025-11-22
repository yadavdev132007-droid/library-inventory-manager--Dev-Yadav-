import json
import logging
from pathlib import Path
from .book import Book

class LibraryInventory:
    def __init__(self, file_path="books.json"):
        self.file_path = Path(file_path)
        self.books = []
        self.load_books()

    def add_book(self, book):
        self.books.append(book)
        logging.info(f"Book added: {book.title}")
        self.save_books()

    def search_by_title(self, title):
        return [b for b in self.books if title.lower() in b.title.lower()]

    def search_by_isbn(self, isbn):
        return next((b for b in self.books if b.isbn == isbn), None)

    def display_all(self):
        return self.books

    def save_books(self):
        data = [b.to_dict() for b in self.books]
        try:
            self.file_path.write_text(json.dumps(data, indent=4))
            logging.info("Book catalog saved.")
        except Exception as e:
            logging.error(f"Error saving file: {e}")

    def load_books(self):
        if not self.file_path.exists():
            logging.warning("Book file missing. Creating a new one.")
            self.save_books()
            return

        try:
            data = json.loads(self.file_path.read_text())
            self.books = [Book(**item) for item in data]
        except Exception as e:
            logging.error(f"Corrupted file. Error: {e}")
            self.books = []
