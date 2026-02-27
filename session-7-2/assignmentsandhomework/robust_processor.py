# robust_processor.py
# Production-quality student CSV processor with:
# - file error handling
# - per-row validation
# - logging
# - graceful failure

import csv
import logging


def process_student_data(filename):
    """
    Read and process student CSV data safely.

    Expected CSV columns:
        name, age, score

    Validation rules:
        - age must be between 0 and 120
        - score must be between 0 and 100

    Behavior:
        - Handles file errors gracefully
        - Skips invalid rows
        - Logs warnings/errors/info
        - Returns results dict or None
    """
    logger = logging.getLogger("student_processor")

    valid_students = []
    total_rows = 0
    invalid_rows = 0

    logger.info(f"Starting processing for file: {filename}")

    # Try to read file
    try:
        with open(filename, "r", newline="") as f:
            reader = csv.DictReader(f)

            # Check required columns
            required_columns = {"name", "age", "score"}
            if reader.fieldnames is None:
                logger.error("File is empty or missing a header row.")
                return None

            missing_columns = required_columns - set(reader.fieldnames)
            if missing_columns:
                logger.error(f"Missing required columns: {missing_columns}")
                return None

            # Parse and validate each row
            for row_number, row in enumerate(reader, start=2):  # row 2 = first data row
                total_rows += 1

                try:
                    name = row["name"].strip()
                    age = int(row["age"])
                    score = float(row["score"])

                    if not name:
                        raise ValueError("Name is empty")

                    if not (0 <= age <= 120):
                        raise ValueError(f"Invalid age: {age}")

                    if not (0 <= score <= 100):
                        raise ValueError(f"Invalid score: {score}")

                    valid_students.append({
                        "name": name,
                        "age": age,
                        "score": score
                    })

                    logger.info(
                        f"Valid row {row_number}: name={name}, age={age}, score={score}"
                    )

                except (ValueError, TypeError, KeyError) as e:
                    invalid_rows += 1
                    logger.warning(f"Skipping invalid row {row_number}: {row} | Reason: {e}")
                    continue

    except FileNotFoundError:
        logger.error(f"File not found: {filename}")
        return None
    except PermissionError:
        logger.error(f"No permission to read file: {filename}")
        return None
    except csv.Error as e:
        logger.error(f"CSV parsing error in file {filename}: {e}")
        return None
    except Exception as e:
        logger.exception(f"Unexpected error while processing {filename}: {e}")
        return None

    # Graceful handling if no valid data
    if not valid_students:
        logger.warning("No valid student records found.")
        return {
            "file": filename,
            "total_rows": total_rows,
            "valid_rows": 0,
            "invalid_rows": invalid_rows,
            "average_age": 0,
            "average_score": 0,
            "highest_score": None,
            "lowest_score": None,
            "top_student": None,
            "students": []
        }

    # Calculate statistics
    total_age = 0
    total_score = 0
    highest_score = valid_students[0]["score"]
    lowest_score = valid_students[0]["score"]
    top_student = valid_students[0]["name"]

    for student in valid_students:
        total_age += student["age"]
        total_score += student["score"]

        if student["score"] > highest_score:
            highest_score = student["score"]
            top_student = student["name"]

        if student["score"] < lowest_score:
            lowest_score = student["score"]

    average_age = total_age / len(valid_students)
    average_score = total_score / len(valid_students)

    results = {
        "file": filename,
        "total_rows": total_rows,
        "valid_rows": len(valid_students),
        "invalid_rows": invalid_rows,
        "average_age": average_age,
        "average_score": average_score,
        "highest_score": highest_score,
        "lowest_score": lowest_score,
        "top_student": top_student,
        "students": valid_students
    }

    logger.info(
        f"Processing complete: total_rows={total_rows}, "
        f"valid_rows={len(valid_students)}, invalid_rows={invalid_rows}"
    )

    return results


if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s"
    )

    # Create a sample CSV for testing
    sample_file = "students_data.csv"
    with open(sample_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "age", "score"])
        writer.writerow(["Alice", 20, 95])
        writer.writerow(["Bob", 25, 88])
        writer.writerow(["Carol", 130, 78])     # invalid age
        writer.writerow(["David", 22, 105])     # invalid score
        writer.writerow(["", 19, 91])           # invalid name
        writer.writerow(["Eve", "abc", 85])     # invalid age type
        writer.writerow(["Frank", 30, 72])

    # Test with existing file
    print("\n--- Test: Existing File ---")
    result = process_student_data(sample_file)
    print(result)

    # Test with missing file
    print("\n--- Test: Missing File ---")
    result = process_student_data("missing_file.csv")
    print(result)