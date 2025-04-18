"""
Book class module for managing book data and operations.

This module provides the Book class which represents a book entity with its properties
and methods for data conversion and string representation.
"""

class Book:
    """A class representing a book with its metadata and user notes.
    
    This class encapsulates all the information about a book including its title,
    authors, description, publication date, and additional metadata. It also supports
    user-added notes and provides methods for data serialization and deserialization.
    
    Attributes:
        title (str): The title of the book
        authors (list[str]): List of authors' names
        description (str): Book description or summary
        published_date (str): Publication date of the book
        info_link (str): URL for more information about the book
        note (str, optional): User-added note about the book
    """
    
    def __init__(self, title, authors, description, published_date, info_link, note=None):
        """Initialize a Book instance.
        
        Args:
            title (str): The title of the book
            authors (list[str]): List of authors' names
            description (str): Book description or summary
            published_date (str): Publication date of the book
            info_link (str): URL for more information about the book
            note (str, optional): User-added note about the book. Defaults to None.
        """
        self.title = title
        self.authors = authors
        self.description = description
        self.published_date = published_date
        self.info_link = info_link
        self.note = note

    def __str__(self):
        """Return a formatted string representation of the book.
        
        Returns:
            str: A formatted string containing the book's details
        """
        return f"""
📘 {self.title}
   Author(s): {', '.join(self.authors) if self.authors else 'Unknown'}
   Published: {self.published_date or 'Unknown'}
   Summary: {self.description or 'No description available'}
   More Info: {self.info_link}
   Note: {self.note if self.note else 'No note added'}
"""

    def to_dict(self):
        """Convert the book instance to a dictionary.
        
        Returns:
            dict: Dictionary containing all book attributes
        """
        return {
            'title': self.title,
            'authors': self.authors,
            'description': self.description,
            'published_date': self.published_date,
            'info_link': self.info_link,
            'note': self.note
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Book instance from a dictionary.
        
        Args:
            data (dict): Dictionary containing book attributes
            
        Returns:
            Book: A new Book instance
        """
        return cls(
            title=data['title'],
            authors=data['authors'],
            description=data['description'],
            published_date=data['published_date'],
            info_link=data['info_link'],
            note=data.get('note')
        ) 