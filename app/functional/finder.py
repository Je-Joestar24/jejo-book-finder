"""
BookFinder module for searching books using the Google Books API.

This module provides the concrete implementation of the BookFinderBase class
for searching books using the Google Books API.
"""

import requests
import logging
from app.functional.book import Book

class BookFinder:
    """A class for searching books using the Google Books API.
    
    This class implements the book search functionality using the Google Books API.
    It handles API requests, response processing, and error handling.
    
    Attributes:
        api_url (str): URL for the Google Books API
        logger (Logger): Logger instance for the book finder
    """
    
    def __init__(self):
        """Initialize the BookFinder with API URL and logging setup."""
        self.api_url = "https://www.googleapis.com/books/v1/volumes"
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

    def search_books(self, query, title=None, author=None, lang=None):
        """Search for books using the Google Books API.
        
        This method constructs the search query based on the provided criteria
        and makes a request to the Google Books API.
        
        Args:
            query (str): General search query
            title (str, optional): Title to search for
            author (str, optional): Author to search for
            lang (str, optional): Language to filter by
            
        Returns:
            list[Book]: List of found books
            
        Raises:
            requests.exceptions.RequestException: If the API request fails
        """
        try:
            search_query = []
            if query:
                search_query.append(query)
            if title:
                search_query.append(f"intitle:{title}")
            if author:
                search_query.append(f"inauthor:{author}")
            if lang:
                search_query.append(f"lang:{lang}")

            params = {'q': '+'.join(search_query)}
            response = requests.get(self.api_url, params=params)
            response.raise_for_status()
            return self.handle_response(response.json())
        except requests.exceptions.RequestException as e:
            logging.error(f"API request failed: {str(e)}")
            return []

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