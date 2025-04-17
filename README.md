# 📚 Jejo Book Finder

A powerful terminal-based application for searching and managing books using the Google Books API, featuring a rich terminal interface and advanced book management capabilities.

## ✨ Features

- 🔍 **Advanced Search**
  - Search by title, author, or keyword
  - Filter results by language
  - Command-line search options
  - Rich display of book details

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

### Book Navigation Options
When viewing a book, you can use these options:
- `y` - Add to favorites (with optional note)
- `n` - Next book
- `b` - Previous book
- `l` - List view of all books
- `q` - Quit to main menu

### Favorites Management Options
When viewing favorites:
- `r` - Remove a book
- `s` - Search/filter favorites
- `q` - Quit to main menu

## 📁 File Structure

- `main.py` - Main application entry point
- `app/book.py` - Book class definition
- `app/finder.py` - BookFinder class for API integration
- `app/favorites.py` - FavoritesManager class for managing saved books
- `app/controls.py` - Controls for interactive user interface
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