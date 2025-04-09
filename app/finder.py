import requests
import logging
from app.book import Book

class BookFinder:
    def __init__(self):
        self.api_url = "https://www.googleapis.com/books/v1/volumes"
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

    def search_books(self, query):
        try:
            params = {'q': query}
            response = requests.get(self.api_url, params=params)
            response.raise_for_status()
            return self.handle_response(response.json())
        except requests.exceptions.RequestException as e:
            logging.error(f"API request failed: {str(e)}")
            return []

    def handle_response(self, response):
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