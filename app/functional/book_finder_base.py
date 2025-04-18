"""
BookFinderBase module for defining the abstract base class for book finders.

This module provides the abstract base class that defines the interface and common
functionality for all book finder implementations.
"""

from abc import ABC, abstractmethod
import logging
from app.functional.book import Book

class BookFinderBase(ABC):
    """Abstract base class for book finder implementations.
    
    This class defines the interface and common functionality for all book finder
    implementations. It provides logging setup and response handling, while requiring
    concrete implementations to provide their own search functionality.
    
    Attributes:
        logger (Logger): Logger instance for the book finder
    """
    
    def __init__(self):
        """Initialize the book finder and set up logging."""
        self.setup_logging()

    def setup_logging(self):
        """Configure logging for the book finder.
        
        Sets up a logger with both file and console handlers, using a standard
        format for log messages.
        """
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('book_finder.log'),
                logging.StreamHandler()
            ]
        )

    @abstractmethod
    def search_books(self, query, title=None, author=None, lang=None):
        """Search for books using the implemented finder.
        
        This is an abstract method that must be implemented by concrete classes.
        It should search for books based on the provided criteria and return
        a list of Book objects.
        
        Args:
            query (str): General search query
            title (str, optional): Title to search for
            author (str, optional): Author to search for
            lang (str, optional): Language to filter by
            
        Returns:
            list[Book]: List of found books
            
        Raises:
            NotImplementedError: If not implemented by concrete class
        """
        pass

    def handle_response(self, response):
        """Handle the API response and convert it to Book objects.
        
        This method processes the API response and converts it into a list of
        Book objects. It handles error cases and logging.
        
        Args:
            response (dict): API response data
            
        Returns:
            list[Book]: List of processed Book objects
        """
        books = []
        try:
            items = response.get('items', [])
            for item in items:
                volume_info = item.get('volumeInfo', {})
                book = Book(
                    title=volume_info.get('title', 'Unknown Title'),
                    authors=volume_info.get('authors', []),
                    description=volume_info.get('description', ''),
                    published_date=volume_info.get('publishedDate', ''),
                    info_link=volume_info.get('infoLink', '')
                )
                books.append(book)
            logging.info(f"Successfully processed {len(books)} books")
            return books
        except Exception as e:
            logging.error(f"Error processing response: {str(e)}")
            return [] 