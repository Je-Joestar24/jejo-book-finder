
from app.ui.utils import console, Prompt, Panel

def display_menu():
    console.print(Panel.fit("📚 Jejo Book Finder", style="bold blue"))
    console.print("1. Search for books")
    console.print("2. View favorites")
    console.print("3. View recently viewed")
    console.print("4. Export favorites")
    console.print("5. Exit")
    return Prompt.ask("Choose an option", choices=["1", "2", "3", "4", "5"])