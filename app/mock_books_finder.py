from app.book_finder_base import BookFinderBase
from app.book import Book

class MockBooksFinder(BookFinderBase):
    def __init__(self):
        super().__init__()
        self.mock_books = [
            Book(
                title="The Test Book",
                authors=["Test Author"],
                description="A test book description",
                published_date="2023-01-01",
                info_link="http://example.com/test-book"
            ),
            Book(
                title="Another Test Book",
                authors=["Another Author"],
                description="Another test book description",
                published_date="2023-02-01",
                info_link="http://example.com/another-test-book"
            )
        ]

    def search_books(self, query, title=None, author=None, lang=None):
        """Search for books using mock data.
        
        Args:
            query (str): General search query
            title (str, optional): Title to search for
            author (str, optional): Author to search for
            lang (str, optional): Language to filter by
            
        Returns:
            list[Book]: List of found books
        """
        filtered_books = self.mock_books.copy()
        
        if title:
            filtered_books = [b for b in filtered_books if title.lower() in b.title.lower()]
        if author:
            filtered_books = [b for b in filtered_books if any(author.lower() in a.lower() for a in b.authors)]
        if query:
            filtered_books = [b for b in filtered_books if 
                            query.lower() in b.title.lower() or 
                            any(query.lower() in a.lower() for a in b.authors) or
                            query.lower() in b.description.lower()]
        
        return filtered_books 