"""
UI Utilities Module

Description:
------------
Provides shared utilities for user interaction and formatted output in the terminal interface.
Leverages the Rich library to display tables, panels, and handle input prompts.

Features:
---------
- Centralized console instance for consistent output across the app.
- User input handling with rich prompts.
- Utility functions for formatting output (e.g., tables, panels).
- Terminal display enhancements using colors and styles.

Usage:
------
Import and use the shared `console` instance:
    from app.ui.utils import console
    console.print("[bold green]Welcome![/bold green]")

Future extensions can include:
- Custom loading indicators
- Theming or layout presets
"""

# --- Standard Library ---
import os
from datetime import datetime

# --- Third-Party Libraries ---
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from rich.panel import Panel

# --- Console Initialization ---
console = Console()

__all__ = ["console", "Prompt", "Table", "Panel"]
