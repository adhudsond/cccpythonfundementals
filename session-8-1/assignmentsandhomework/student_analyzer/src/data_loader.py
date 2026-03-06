# data_loader.py
import csv


def load_students_csv(filename):
    """
    Load student data from a CSV file.

    Expected columns:
      name, age, score, attendance

    Returns:
      list[dict]: Each dict has keys: name(str), age(int), score(float), attendance(float)
    """
    students = []
    with open(filename, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        required = {"name", "age", "score", "attendance"}
        if reader.fieldnames is None:
            raise ValueError("CSV is missing a header row.")
        missing = required - set(reader.fieldnames)
        if missing:
            raise ValueError(f"CSV missing required columns: {sorted(missing)}")

        for row_num, row in enumerate(reader, start=2):
            try:
                name = row["name"].strip()
                age = int(row["age"])
                score = float(row["score"])
                attendance = float(row["attendance"])

                if not name:
                    raise ValueError("Empty name")

                students.append(
                    {"name": name, "age": age, "score": score, "attendance": attendance}
                )
            except Exception as e:
                # Skip bad rows safely (could also log)
                # Keeping it simple for this project.
                continue

    return students