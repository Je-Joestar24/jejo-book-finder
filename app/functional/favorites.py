"""
FavoritesManager module for managing user's favorite books.

This module provides functionality for managing a user's favorite books, including
adding, removing, filtering, and exporting favorites. It also handles recent book
tracking and persistence to JSON files.
"""

import json
import os
import csv
from datetime import datetime
from app.functional.book import Book

class FavoritesManager:
    """A class for managing user's favorite books and recently viewed books.
    
    This class provides functionality to manage a user's favorite books, including
    adding, removing, filtering, and exporting favorites. It also tracks recently
    viewed books and handles data persistence to JSON files.
    
    Attributes:
        filename (str): Path to the favorites JSON file
        recent_filename (str): Path to the recent books JSON file
        favorites (list): List of favorite book dictionaries
        recent_books (list): List of recently viewed book dictionaries
    """
    
    def __init__(self, filename='favorites/favorites.json', recent_filename='favorites/recent.json'):
        """Initialize the FavoritesManager with file paths and load existing data.
        
        Args:
            filename (str, optional): Path to favorites file. Defaults to 'favorites/favorites.json'.
            recent_filename (str, optional): Path to recent books file. Defaults to 'favorites/recent.json'.
        """
        self.filename = filename
        self.recent_filename = recent_filename
        self.favorites = self.load_favorites()
        self.recent_books = self.load_recent_books()

    def load_favorites(self):
        """Load favorite books from the JSON file.
        
        Returns:
            list: List of favorite book dictionaries
        """
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return []
        return []

    def load_recent_books(self):
        """Load recently viewed books from the JSON file.
        
        Returns:
            list: List of recently viewed book dictionaries
        """
        if os.path.exists(self.recent_filename):
            try:
                with open(self.recent_filename, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return []
        return []

    def save_favorites(self):
        """Save favorite books to the JSON file."""
        with open(self.filename, 'w') as f:
            json.dump(self.favorites, f, indent=2)

    def save_recent_books(self):
        """Save recently viewed books to the JSON file."""
        with open(self.recent_filename, 'w') as f:
            json.dump(self.recent_books, f, indent=2)

    def add_favorite(self, book, note=None):
        """Add a book to favorites with an optional note.
        
        Args:
            book (Book): Book object to add
            note (str, optional): User note about the book
            
        Returns:
            bool: True if book was added, False if it was already in favorites
        """
        book_data = book.to_dict()
        book_data['note'] = note
        if book_data not in self.favorites:
            self.favorites.append(book_data)
            self.save_favorites()
            return True
        return False

    def add_recent(self, book):
        """Add a book to recently viewed list.
        
        Args:
            book (Book): Book object to add
        """
        book_data = book.to_dict()
        if book_data not in self.recent_books:
            self.recent_books.insert(0, book_data)
            if len(self.recent_books) > 10:
                self.recent_books.pop()
            self.save_recent_books()

    def remove_favorite(self, book_title):
        """Remove a book from favorites by title.
        
        Args:
            book_title (str): Title of the book to remove
        """
        self.favorites = [f for f in self.favorites if f['title'] != book_title]
        self.save_favorites()

    def get_favorites(self):
        """Get all favorite books as Book objects.
        
        Returns:
            list[Book]: List of favorite Book objects
        """
        return [Book.from_dict(book_data) for book_data in self.favorites]

    def get_recent_books(self):
        """Get all recently viewed books as Book objects.
        
        Returns:
            list[Book]: List of recently viewed Book objects
        """
        return [Book.from_dict(book_data) for book_data in self.recent_books]

    def filter_favorites(self, author=None, title=None):
        """Filter favorite books by author and/or title.
        
        Args:
            author (str, optional): Author name to filter by
            title (str, optional): Title to filter by
            
        Returns:
            list[Book]: List of filtered Book objects
        """
        filtered = self.favorites
        if author:
            filtered = [f for f in filtered if author.lower() in ' '.join(f['authors']).lower()]
        if title:
            filtered = [f for f in filtered if title.lower() in f['title'].lower()]
        return [Book.from_dict(book_data) for book_data in filtered]

    def export_favorites(self, format_type='csv', filename=None):
        """Export favorite books to a file in the specified format.
        
        Args:
            format_type (str, optional): Export format (csv/json/md). Defaults to 'csv'.
            filename (str, optional): Output filename. Defaults to auto-generated name.
            
        Returns:
            str: Path to the exported file
        """
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