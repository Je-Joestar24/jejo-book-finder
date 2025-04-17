import argparse
from app.google_books_finder import GoogleBooksFinder
from app.mock_books_finder import MockBooksFinder
from app.functional.favorites import FavoritesManager
from app.ui.utils import console
from app.ui.books import search_books
from app.ui.favorites import view_favorites, export_favorites
from app.ui.menu import display_menu

def get_book_finder(use_mock=False):
    """Factory function to create the appropriate book finder.
    
    Args:
        use_mock (bool): Whether to use the mock finder instead of Google Books
        
    Returns:
        BookFinderBase: An instance of a book finder
    """
    if use_mock:
        return MockBooksFinder()
    return GoogleBooksFinder()

def main():
    parser = argparse.ArgumentParser(description="Jejo Book Finder")
    parser.add_argument("--title", help="Search by title")
    parser.add_argument("--author", help="Search by author")
    parser.add_argument("--lang", help="Search by language")
    parser.add_argument("--favorites", action="store_true", help="View favorites")
    parser.add_argument("--export", help="Export favorites (format: csv/json/md)")
    parser.add_argument("--filename", help="Export filename")
    parser.add_argument("--mock", action="store_true", help="Use mock book finder for testing")
    args = parser.parse_args()

    book_finder = get_book_finder(args.mock)
    favorites_manager = FavoritesManager()

    if args.favorites:
        view_favorites(favorites_manager)
    elif args.export:
        export_favorites(favorites_manager, args.export, args.filename)
    elif any([args.title, args.author, args.lang]):
        search_books(book_finder, favorites_manager, title=args.title, author=args.author, lang=args.lang)
    else:
        while True:
            choice = display_menu()
            
            if choice == "1":
                search_books(book_finder, favorites_manager)
            elif choice == "2":
                view_favorites(favorites_manager)
            elif choice == "3":
                view_recent(favorites_manager)
            elif choice == "4":
                export_favorites(favorites_manager)
            elif choice == "5":
                console.print("[bold blue]👋 Goodbye! Happy reading![/bold blue]")
                break

if __name__ == "__main__":
    main() 