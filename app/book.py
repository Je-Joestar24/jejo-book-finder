class Book:
    def __init__(self, title, authors, description, published_date, info_link):
        self.title = title
        self.authors = authors
        self.description = description
        self.published_date = published_date
        self.info_link = info_link

    def __str__(self):
        return f"""
📘 {self.title}
   Author(s): {', '.join(self.authors) if self.authors else 'Unknown'}
   Published: {self.published_date or 'Unknown'}
   Summary: {self.description or 'No description available'}
   More Info: {self.info_link}
""" 