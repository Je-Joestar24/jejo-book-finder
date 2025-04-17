
from app.ui.utils import console, Prompt, Table


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