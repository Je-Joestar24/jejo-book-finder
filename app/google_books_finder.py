"""
Google Books API integration module for searching and retrieving book information.

This module implements the BookFinderBase interface to search for books using
the Google Books API, providing real book data from Google's extensive database.
"""

import requests
from app.functional.book_finder_base import BookFinderBase

class GoogleBooksFinder(BookFinderBase):
    """Implementation of BookFinderBase using the Google Books API.
    
    This class provides functionality to search for books using the Google Books API,
    handling API requests, response parsing, and error management.
    """
    
    def __init__(self):
        """Initialize the Google Books finder with the API endpoint."""
        super().__init__()
        self.api_url = "https://www.googleapis.com/books/v1/volumes"

    def search_books(self, query, title=None, author=None, lang=None):
        """Search for books using the Google Books API.
        
        This method constructs and sends a search request to the Google Books API,
        handling query parameters and response parsing.
        
        Args:
            query (str): General search query
            title (str, optional): Title to search for
            author (str, optional): Author to search for
            lang (str, optional): Language to filter by
            
        Returns:
            list[Book]: List of found books matching the search criteria
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
            logging.error(f"Google Books API request failed: {str(e)}")
            return [] 