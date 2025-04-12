class Book:
    def __init__(self, title, authors, description, published_date, info_link, note=None):
        self.title = title
        self.authors = authors
        self.description = description
        self.published_date = published_date
        self.info_link = info_link
        self.note = note

    def __str__(self):
        return f"""
📘 {self.title}
   Author(s): {', '.join(self.authors) if self.authors else 'Unknown'}
   Published: {self.published_date or 'Unknown'}
   Summary: {self.description or 'No description available'}
   More Info: {self.info_link}
   Note: {self.note if self.note else 'No note added'}
"""

    def to_dict(self):
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
        return cls(
            title=data['title'],
            authors=data['authors'],
            description=data['description'],
            published_date=data['published_date'],
            info_link=data['info_link'],
            note=data.get('note')
        ) 