import json
import os
import csv
from datetime import datetime
from app.functional.book import Book

class FavoritesManager:
    def __init__(self, filename='favorites/favorites.json', recent_filename='favorites/recent.json'):
        self.filename = filename
        self.recent_filename = recent_filename
        self.favorites = self.load_favorites()
        self.recent_books = self.load_recent_books()

    def load_favorites(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return []
        return []

    def load_recent_books(self):
        if os.path.exists(self.recent_filename):
            try:
                with open(self.recent_filename, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return []
        return []

    def save_favorites(self):
        with open(self.filename, 'w') as f:
            json.dump(self.favorites, f, indent=2)

    def save_recent_books(self):
        with open(self.recent_filename, 'w') as f:
            json.dump(self.recent_books, f, indent=2)

    def add_favorite(self, book, note=None):
        book_data = book.to_dict()
        book_data['note'] = note
        if book_data not in self.favorites:
            self.favorites.append(book_data)
            self.save_favorites()
            return True
        return False

    def add_recent(self, book):
        book_data = book.to_dict()
        if book_data not in self.recent_books:
            self.recent_books.insert(0, book_data)
            if len(self.recent_books) > 10:
                self.recent_books.pop()
            self.save_recent_books()

    def remove_favorite(self, book_title):
        self.favorites = [f for f in self.favorites if f['title'] != book_title]
        self.save_favorites()

    def get_favorites(self):
        return [Book.from_dict(book_data) for book_data in self.favorites]

    def get_recent_books(self):
        return [Book.from_dict(book_data) for book_data in self.recent_books]

    def filter_favorites(self, author=None, title=None):
        filtered = self.favorites
        if author:
            filtered = [f for f in filtered if author.lower() in ' '.join(f['authors']).lower()]
        if title:
            filtered = [f for f in filtered if title.lower() in f['title'].lower()]
        return [Book.from_dict(book_data) for book_data in filtered]

    def export_favorites(self, format_type='csv', filename=None):
        if not filename:
            filename = f'exports/favorites_export_{datetime.now().strftime("%Y%m%d_%H%M%S")}.{format_type}'
        
        if format_type == 'csv':
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=['title', 'authors', 'description', 'published_date', 'info_link', 'note'])
                writer.writeheader()
                for book in self.favorites:
                    row = book.copy()
                    row['authors'] = ', '.join(row['authors']) if row['authors'] else ''
                    writer.writerow(row)
        elif format_type == 'json':
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.favorites, f, indent=2, ensure_ascii=False)
        elif format_type == 'md':
            with open(filename, 'w', encoding='utf-8') as f:
                f.write('# Favorite Books\n\n')
                for book in self.favorites:
                    f.write(f"## {book['title']}\n")
                    f.write(f"**Authors:** {', '.join(book['authors']) if book['authors'] else 'Unknown'}\n")
                    f.write(f"**Published:** {book['published_date'] or 'Unknown'}\n")
                    f.write(f"**Note:** {book.get('note', 'No note')}\n")
                    f.write(f"**Link:** {book['info_link']}\n\n")
                    if book.get('description'):
                        f.write(f"### Description\n{book['description']}\n\n")
                    f.write("---\n\n")
        return filename 