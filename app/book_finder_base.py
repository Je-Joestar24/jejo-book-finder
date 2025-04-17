from abc import ABC, abstractmethod
import logging
from app.book import Book

class BookFinderBase(ABC):
    def __init__(self):
        self.setup_logging()

    def setup_logging(self):
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
        
        Args:
            query (str): General search query
            title (str, optional): Title to search for
            author (str, optional): Author to search for
            lang (str, optional): Language to filter by
            
        Returns:
            list[Book]: List of found books
        """
        pass

    def handle_response(self, response):
        """Handle the API response and convert it to Book objects.
        
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