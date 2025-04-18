"""
UI utilities module providing common components and functionality.

This module contains shared UI components and utilities used across the application,
including console output handling, user input prompts, and formatting tools.
"""

from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from rich.panel import Panel
import os
from datetime import datetime

# Initialize a global console instance for consistent output formatting
console = Console()