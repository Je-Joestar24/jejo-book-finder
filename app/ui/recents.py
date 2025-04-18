from app.ui.utils import console, Table

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