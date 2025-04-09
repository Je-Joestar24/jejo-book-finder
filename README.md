# 📚 Jejo Book Finder

A terminal-based application for searching and managing books using the Google Books API.

## Features

- Search for books by title, author, or keyword
- View detailed book information
- Save favorite books to a local file
- View and manage your favorite books

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate.ps1  # On Windows: venv\Scripts\activate.ps1
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application:
```bash
python main.py
```

Follow the on-screen prompts to:
1. Search for books
2. View your favorite books
3. Add/remove books from favorites

## File Structure

- `main.py` - Main application entry point
- `book.py` - Book class definition
- `finder.py` - BookFinder class for API integration
- `favorites.py` - FavoritesManager class for managing saved books
- `requirements.txt` - Project dependencies 