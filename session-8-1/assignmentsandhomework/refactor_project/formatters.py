# formatters.py
# Formatting functions (nice reports, labels, consistent output)

def format_money(value):
    """Format a number as dollars."""
    return f"${value:,.2f}"


def format_percent(value):
    """Format a number as percent with 2 decimals."""
    return f"{value:.2f}%"


def print_header(title, width=60):
    """Print a clean report header."""
    print("=" * width)
    print(title.center(width))
    print("=" * width)


def print_kv(label, value, label_width=22):
    """Print a label/value line neatly aligned."""
    print(f"{label:<{label_width}} {value}")


def format_list(label, items):
    """Return a formatted string for a labeled list."""
    return f"{label}: {items}"