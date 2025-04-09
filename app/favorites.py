import json
import os
from app.book import Book

class FavoritesManager:
    def __init__(self, filename='favorites/favorites.json'):
        self.filename = filename
        self.favorites = self.load_favorites()

    def load_favorites(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return []
        return []

    def save_favorites(self):
        with open(self.filename, 'w') as f:
            json.dump(self.favorites, f, indent=2)

    def add_favorite(self, book):
        book_data = {
            'title': book.title,
            'authors': book.authors,
            'description': book.description,
            'published_date': book.published_date,
            'info_link': book.info_link
        }
        if book_data not in self.favorites:
            self.favorites.append(book_data)
            self.save_favorites()
            return True
        return False

    def remove_favorite(self, book_title):
        self.favorites = [f for f in self.favorites if f['title'] != book_title]
        self.save_favorites()

    def get_favorites(self):
        return [Book(**book_data) for book_data in self.favorites] 