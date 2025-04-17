import os
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table

console = Console()

def display_menu():
    console.print(Panel.fit("📚 Jejo Book Finder", style="bold blue"))
    console.print("1. Search for books")
    console.print("2. View favorites")
    console.print("3. View recently viewed")
    console.print("4. Export favorites")
    console.print("5. Exit")
    return Prompt.ask("Choose an option", choices=["1", "2", "3", "4", "5"])

def display_book(book, current_index, total_books):
    console.print(Panel.fit(
        f"[bold blue]📘 {book.title}[/bold blue]\n"
        f"[yellow]Author(s):[/yellow] {', '.join(book.authors) if book.authors else 'Unknown'}\n"
        f"[yellow]Published:[/yellow] {book.published_date or 'Unknown'}\n"
        f"[yellow]Summary:[/yellow] {book.description or 'No description available'}\n"
        f"[yellow]More Info:[/yellow] {book.info_link}",
        title=f"Book {current_index}/{total_books}"
    ))

def search_books(book_finder, favorites_manager, query=None, title=None, author=None, lang=None):
    if not any([query, title, author]):
        query = Prompt.ask("🔍 Enter a book title, author, or keyword")
    
    books = book_finder.search_books(query, title, author, lang)
    
    if not books:
        console.print("[red]No books found. Try a different search term.[/red]")
        return

    current_index = 0
    while current_index < len(books):
        book = books[current_index]
        favorites_manager.add_recent(book)
        display_book(book, current_index + 1, len(books))
        
        console.print("\nOptions:")
        console.print("[yellow]y[/yellow] - Add to favorites (with optional note)")
        console.print("[yellow]n[/yellow] - Next book")
        console.print("[yellow]b[/yellow] - Previous book")
        console.print("[yellow]l[/yellow] - List view of all books")
        console.print("[yellow]q[/yellow] - Quit to main menu")
        
        action = Prompt.ask(
            "Choose action",
            choices=["y", "n", "l", "b", "q"],
            default="n"
        )
        
        if action == "y":
            note = Prompt.ask("Add a note (leave blank to skip)")
            if favorites_manager.add_favorite(book, note):
                console.print("[green]✅ Book added to favorites![/green]")
            else:
                console.print("[yellow]⚠️ Book is already in favorites![/yellow]")
            current_index += 1
        elif action == "n":
            current_index += 1
        elif action == "l":
            table = Table(show_header=True, header_style="bold magenta")
            table.add_column("Index")
            table.add_column("Title")
            table.add_column("Author(s)")
            for i, b in enumerate(books, 1):
                table.add_row(str(i), b.title, ', '.join(b.authors))
            console.print(table)
            selection = Prompt.ask("Enter book number to view", choices=[str(i) for i in range(1, len(books) + 1)])
            current_index = int(selection) - 1
        elif action == "b" and current_index > 0:
            current_index -= 1
        elif action == "q":
            break

def view_favorites(favorites_manager, author=None, title=None):
    favorites = favorites_manager.filter_favorites(author, title)
    if not favorites:
        console.print("[yellow]No favorite books yet![/yellow]")
        return

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Index")
    table.add_column("Title")
    table.add_column("Author(s)")
    table.add_column("Note")
    
    for i, book in enumerate(favorites, 1):
        table.add_row(
            str(i),
            book.title,
            ', '.join(book.authors),
            book.note or "No note"
        )
    
    console.print(table)
    
    while True:
        console.print("\nOptions:")
        console.print("[yellow]r[/yellow] - Remove a book from favorites")
        console.print("[yellow]s[/yellow] - Search/filter favorites")
        console.print("[yellow]q[/yellow] - Quit to main menu")
        
        action = Prompt.ask(
            "Choose action",
            choices=["r", "s", "q"],
            default="q"
        )
        
        if action == "r":
            selection = Prompt.ask("Enter book number to remove", choices=[str(i) for i in range(1, len(favorites) + 1)])
            book = favorites[int(selection) - 1]
            favorites_manager.remove_favorite(book.title)
            console.print("[green]✅ Book removed from favorites![/green]")
            break
        elif action == "s":
            author = Prompt.ask("Filter by author (leave blank to skip)")
            title = Prompt.ask("Filter by title (leave blank to skip)")
            view_favorites(favorites_manager, author, title)
            break
        elif action == "q":
            break

def view_recent(favorites_manager):
    recent_books = favorites_manager.get_recent_books()
    if not recent_books:
        console.print("[yellow]No recently viewed books![/yellow]")
        return

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Index")
    table.add_column("Title")
    table.add_column("Author(s)")
    
    for i, book in enumerate(recent_books, 1):
        table.add_row(str(i), book.title, ', '.join(book.authors))
    
    console.print(table)

def export_favorites(favorites_manager, format_type=None, filename=None):
    # Create exports directory if it doesn't exist
    exports_dir = "exports"
    if not os.path.exists(exports_dir):
        os.makedirs(exports_dir)

    if not format_type:
        format_type = Prompt.ask(
            "Choose export format",
            choices=["csv", "json", "md"],
            default="csv"
        )
    
    if not filename:
        filename = Prompt.ask("Enter filename (leave blank for default)")
    
    # If no filename provided, create a default one with timestamp
    if not filename:
        filename = f'favorites_export_{datetime.now().strftime("%Y%m%d_%H%M%S")}.{format_type}'
    elif not filename.endswith(f'.{format_type}'):
        filename = f'{filename}.{format_type}'
    
    # Prepend exports directory to filename
    filepath = os.path.join(exports_dir, filename)
    
    exported_file = favorites_manager.export_favorites(format_type, filepath)
    console.print(f"[green]✅ Favorites exported to {exported_file}[/green]")