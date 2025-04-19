# 📚 Jejo Book Finder

A powerful terminal-based application for searching and managing books using the Google Books API, featuring a rich terminal interface and advanced book management capabilities.

## ✨ Features

- 🔍 **Advanced Search**
  - Search by title, author, or keyword
  - Filter results by language
  - Command-line search options
  - Rich display of book details
  - Mock data support for testing

- 📚 **Book Navigation**
  - View books one at a time with detailed information
  - Navigate through results (next/previous)
  - Quick list view of all results
  - Keyboard shortcuts for faster navigation

- ⭐ **Favorites Management**
  - Add books to favorites with personal notes
  - View and filter favorite books
  - Remove books from favorites
  - Export favorites in multiple formats (CSV/JSON/Markdown)

- 📝 **Recent Books**
  - Automatically track recently viewed books
  - View last 10 books you've seen
  - Quick access to your browsing history

## 🚀 Setup

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

## 💻 Usage

### Interactive Mode
Run the application:
```bash
source venv/bin/activate.ps1  # On Windows: venv\Scripts\activate.ps1
python main.py
```

Follow the on-screen prompts to:
1. Search for books
2. View your favorite books
3. View recently viewed books
4. Export your favorites

### Command Line Mode
Search directly from the command line:
```bash
python main.py --title "Dune" --author "Herbert" --lang "en"
```

View favorites:
```bash
python main.py --favorites
```

Export favorites:
```bash
python main.py --export csv --filename my_books.csv
```

Use mock data for testing:
```bash
python main.py --mock
```

### Book Navigation Options
When viewing a book, you can use these options:
- `y` - Add to favorites (with optional note)
- `n` - Next book
- `b` - Previous book
- `l` - List view of all books
- `q` - Quit to main menu

### Favorites Management Options
When viewing favorites:
- `v` - View a book
- `r` - Remove a book
- `s` - Search/filter favorites
- `q` - Quit to main menu

### DEMO
- link(Video): https://screenrec.com/share/uEwbV29RQD

## 📁 File Structure

- `main.py` - Main application entry point
- `app/`
  - `functional/`
    - `book.py` - Book class definition
    - `book_finder_base.py` - Abstract base class for book finders
    - `favorites.py` - FavoritesManager class for managing saved books
  - `google_books_finder.py` - Google Books API implementation
  - `mock_books_finder.py` - Mock data implementation for testing
  - `ui/` - Controls for interactive user interface
    - `books.py` - Book search and display functionality
    - `favorites.py` - Favorites management UI
    - `favorites.py` - Favorites management UI
    - `menu.py` - Main menu interface
    - `utils.py` - Common UI utilities
- `favorites/` - Directory containing saved favorites and recent books
- `exports/` - Directory containing exported favorites (CSV/JSON/Markdown)
- `requirements.txt` - Project dependencies

## 🔧 Dependencies

- `requests` - For API communication
- `rich` - For beautiful terminal formatting
- `argparse` - For command-line argument parsing
- `python-dotenv` - For environment variable management

## 🎨 Terminal Features

- Color-coded output
- Formatted tables for book listings
- Interactive panels for book details
- Clickable links (in supporting terminals)
- Progress indicators
- Clear error messages

## 🧪 Testing

The application includes a mock implementation for testing purposes:
- Use `--mock` flag to run with mock data
- Mock implementation provides consistent test data
- Useful for development and testing without API calls
- Demonstrates polymorphism and inheritance in the codebase 