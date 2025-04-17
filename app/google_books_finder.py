import requests
from app.functional.book_finder_base import BookFinderBase

class GoogleBooksFinder(BookFinderBase):
    def __init__(self):
        super().__init__()
        self.api_url = "https://www.googleapis.com/books/v1/volumes"

    def search_books(self, query, title=None, author=None, lang=None):
        """Search for books using the Google Books API.
        
        Args:
            query (str): General search query
            title (str, optional): Title to search for
            author (str, optional): Author to search for
            lang (str, optional): Language to filter by
            
        Returns:
            list[Book]: List of found books
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