# data_tools/readers.py

import csv

def read_text_file(filename):
    """Read a text file and return its full contents as a string."""
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()

def read_csv_file(filename):
    """
    Read a CSV file and return a list of dictionaries (one per row).
    Assumes the first row contains headers.
    """
    with open(filename, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)