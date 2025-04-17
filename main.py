import argparse
from app.finder import BookFinder
from app.favorites import FavoritesManager
from app.controls import view_favorites, export_favorites, search_books, display_menu, view_recent, console

def main():
    parser = argparse.ArgumentParser(description="Jejo Book Finder")
    parser.add_argument("--title", help="Search by title")
    parser.add_argument("--author", help="Search by author")
    parser.add_argument("--lang", help="Search by language")
    parser.add_argument("--favorites", action="store_true", help="View favorites")
    parser.add_argument("--export", help="Export favorites (format: csv/json/md)")
    parser.add_argument("--filename", help="Export filename")
    args = parser.parse_args()

    book_finder = BookFinder()
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