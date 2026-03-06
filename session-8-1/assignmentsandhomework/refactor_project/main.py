# main.py
# Refactored: uses modules (validators, calculators, formatters)

from validators import clean_numeric_list, validate_email, validate_age, validate_score
from calculators import average, minimum, maximum, median, std_dev, score_to_letter, count_as
from formatters import print_header, print_kv, format_percent

def run_demo():
    print_header("REFRACTOR PROJECT DEMO")

    # Example 1: Data cleaning + stats (from earlier data_cleaner/data_validator work)
    raw_data = [10, -999, 25, "invalid", None, 30, 100, 15]
    # remove None/non-numeric and keep only 0..100
    cleaned, removed = clean_numeric_list(raw_data, low=0, high=100)

    print_kv("Raw data", raw_data)
    print_kv("Cleaned data", cleaned)
    print_kv("Removed items", removed)

    stats = {
        "Avg": average(cleaned),
        "Min": minimum(cleaned),
        "Max": maximum(cleaned),
        "Median": median(cleaned),
        "Std Dev": std_dev(cleaned),
        "A count (>=90)": count_as(cleaned),
    }

    print("\n--- Statistics ---")
    for k, v in stats.items():
        if isinstance(v, float):
            print_kv(k, f"{v:.2f}")
        else:
            print_kv(k, v)

    # Example 2: Grade conversion
    print("\n--- Grade Conversion ---")
    for s in [95, 85, 75, 65, 55]:
        print_kv(f"Score {s}", score_to_letter(s))

    # Example 3: Email validation
    print("\n--- Email Validation ---")
    for e in ["user@company.com", "invalid.email", " USER@EMAIL.COM "]:
        cleaned_email, ok = validate_email(e)
        print_kv(cleaned_email, "Valid" if ok else "Invalid")

    # Example 4: Input-like validation checks
    print("\n--- Validation Checks ---")
    for a in [-1, 0, 13, 18, 65, 121]:
        ok, msg = validate_age(a)
        print_kv(f"Age {a}", msg)

    for sc in [-5, 0, 87, 101]:
        ok, msg = validate_score(sc)
        print_kv(f"Score {sc}", msg)

    # Pass rate example
    if cleaned:
        passing = 0
        for x in cleaned:
            if x >= 60:
                passing += 1
        pass_rate = (passing / len(cleaned)) * 100
        print("\n--- Pass Rate (cleaned scores) ---")
        print_kv("Passing", f"{passing} of {len(cleaned)}")
        print_kv("Pass rate", format_percent(pass_rate))


if __name__ == "__main__":
    run_demo()