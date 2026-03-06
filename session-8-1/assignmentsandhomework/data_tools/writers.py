# data_tools/writers.py

import csv

def write_text_file(filename, content):
    """Write string content to a text file (overwrites)."""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)

def write_csv_file(filename, data):
    """
    Write CSV from data.
    - If data is a list of dicts, writes headers from dict keys.
    - If data is a list of lists/tuples, writes rows as-is.
    """
    if not data:
        # Create an empty file if there's no data
        with open(filename, "w", newline="", encoding="utf-8") as f:
            pass
        return

    with open(filename, "w", newline="", encoding="utf-8") as f:
        if isinstance(data[0], dict):
            fieldnames = list(data[0].keys())
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        else:
            writer = csv.writer(f)
            writer.writerows(data)