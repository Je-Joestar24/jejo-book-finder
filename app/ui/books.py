from app.ui.utils import console, Panel, Prompt, Table

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