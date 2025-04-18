"""
Favorites UI handler module for managing favorite books and exports.

This module provides the user interface for viewing, managing, and exporting
favorite books, including filtering and detailed view functionality.
"""

from app.ui.utils import console, Prompt, Table, Panel, os, datetime


def display_favorite_book(book):
    """Display a favorite book's details in a formatted panel.
    
    Args:
        book (Book): The book object to display
    """
    console.print(Panel.fit(
        f"[bold blue]📘 {book.title}[/bold blue]\n"
        f"[yellow]Author(s):[/yellow] {', '.join(book.authors) if book.authors else 'Unknown'}\n"
        f"[yellow]Published:[/yellow] {book.published_date or 'Unknown'}\n"
        f"[yellow]Summary:[/yellow] {book.description or 'No description available'}\n"
        f"[yellow]More Info:[/yellow] {book.info_link}\n"
        f"[yellow]Note:[/yellow] {book.note or 'No note'}",
        title="Favorite Book Details"
    ))


def view_favorites(favorites_manager, author=None, title=None):
    """View and manage favorite books with filtering options.
    
    This function displays a list of favorite books and provides options to
    view details, remove books, filter the list, or return to the main menu.
    
    Args:
        favorites_manager (FavoritesManager): Manager for handling favorites
        author (str, optional): Author name to filter by
        title (str, optional): Title to filter by
    """
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
        console.print("[yellow]v[/yellow] - View book details")
        console.print("[yellow]r[/yellow] - Remove a book from favorites")
        console.print("[yellow]s[/yellow] - Search/filter favorites")
        console.print("[yellow]q[/yellow] - Quit to main menu")
        
        action = Prompt.ask(
            "Choose action",
            choices=["v", "r", "s", "q"],
            default="q"
        )
        
        if action == "v":
            selection = Prompt.ask("Enter book number to view", choices=[str(i) for i in range(1, len(favorites) + 1)])
            book = favorites[int(selection) - 1]
            display_favorite_book(book)
        elif action == "r":
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

def export_favorites(favorites_manager, format_type=None, filename=None):
    """Export favorite books to a file in various formats.
    
    This function handles the export of favorite books to CSV, JSON, or Markdown
    format, with options for custom filenames and automatic timestamp-based names.
    
    Args:
        favorites_manager (FavoritesManager): Manager for handling favorites
        format_type (str, optional): Export format (csv/json/md)
        filename (str, optional): Custom filename for the export
    """
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