"""
Menu UI handler module for displaying the main application menu.

This module provides the main menu interface for the book finder application,
allowing users to navigate between different features and functionalities.
"""

from app.ui.utils import console, Prompt, Panel

def display_menu():
    """Display the main menu and get user selection.
    
    This function presents the main menu options to the user and handles
    the selection process. It uses a formatted panel for the title and
    provides numbered options for different application features.
    
    Returns:
        str: The user's menu choice (1-5)
    """
    console.print(Panel.fit("📚 Jejo Book Finder", style="bold blue"))
    console.print("1. Search for books")
    console.print("2. View favorites")
    console.print("3. View recently viewed")
    console.print("4. Export favorites")
    console.print("5. Exit")
    return Prompt.ask("Choose an option", choices=["1", "2", "3", "4", "5"])