from app.finder import BookFinder
from app.favorites import FavoritesManager

def display_menu():
    print("\n📚 Jejo Book Finder")
    print("1. Search for books")
    print("2. View favorites")
    print("3. Exit")
    return input("Choose an option (1-3): ")

def search_books(book_finder, favorites_manager):
    query = input("\n🔍 Enter a book title, author, or keyword: ")
    books = book_finder.search_books(query)
    
    if not books:
        print("No books found. Try a different search term.")
        return

    print(f"\n📚 Found {len(books)} books:")
    for i, book in enumerate(books, 1):
        print(f"\n{i}. {book}")
        save = input("⭐ Add to favorites? (y/n): ").lower()
        if save == 'y':
            if favorites_manager.add_favorite(book):
                print("✅ Book added to favorites!")
            else:
                print("⚠️ Book is already in favorites!")

def view_favorites(favorites_manager):
    favorites = favorites_manager.get_favorites()
    if not favorites:
        print("\nNo favorite books yet!")
        return

    print("\n⭐ Your Favorite Books:")
    for i, book in enumerate(favorites, 1):
        print(f"\n{i}. {book}")
        remove = input("Remove from favorites? (y/n): ").lower()
        if remove == 'y':
            favorites_manager.remove_favorite(book.title)
            print("✅ Book removed from favorites!")

def main():
    book_finder = BookFinder()
    favorites_manager = FavoritesManager()

    while True:
        choice = display_menu()
        
        if choice == '1':
            search_books(book_finder, favorites_manager)
        elif choice == '2':
            view_favorites(favorites_manager)
        elif choice == '3':
            print("\n👋 Goodbye! Happy reading!")
            break
        else:
            print("\n❌ Invalid option. Please try again.")

if __name__ == "__main__":
    main() 