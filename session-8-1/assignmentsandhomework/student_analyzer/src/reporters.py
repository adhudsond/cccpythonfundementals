# reporters.py
import csv


def print_report(results):
    """Print a professional report to the terminal."""
    print("=" * 76)
    print("STUDENT ANALYZER REPORT".center(76))
    print("=" * 76)

    c = results["counts"]
    print(f"Total records:         {c['total']}")
    print(f"Valid records:         {c['valid']}")
    print(f"Invalid records:       {c['invalid']}")
    print(f"Passing (>= 60):       {c['passing']} ({c['pass_rate']:.2f}%)")
    print(f"Total A's (>= 90):     {c['total_as']}")
    print(f"Honors:                {c['honors']}")
    print(f"Probation:             {c['probation']}")

    ss = results["subject_stats"]
    print("-" * 76)
    print("CLASS STATS")
    print(f"Score     -> avg={ss['score']['avg']:.2f}, min={ss['score']['min']}, max={ss['score']['max']}")
    print(f"Attendance-> avg={ss['attendance']['avg']:.2f}, min={ss['attendance']['min']}, max={ss['attendance']['max']}")

    top = results["top_student"]
    print("-" * 76)
    if top:
        print(f"Top student: {top['name']} | Avg={top['average']:.2f} | Att={top['attendance']:.0f}% | Grade={top['letter']}")
    else:
        print("Top student: N/A")

    print("-" * 76)
    print(f"{'Name':<12} {'Age':>4} {'Score':>7} {'Att%':>6} {'Grade':>6} {'Pass':>6}")
    print("-" * 76)

    for s in results["students"]:
        print(f"{s['name']:<12} {s['age']:>4} {s['score']:>7.1f} {s['attendance']:>6.0f} {s['letter']:>6} {str(s['passing']):>6}")

    if results["invalid_rows"]:
        print("-" * 76)
        print("INVALID ROWS (skipped):")
        for item in results["invalid_rows"]:
            print(f" - {item['student']} | Reason: {item['reason']}")

    print("=" * 76)


def write_report_csv(results, filename="student_report.csv"):
    """
    Write analyzed student results to CSV.
    Columns: name, age, score, attendance, average, letter, passing
    """
    rows = results["students"]
    fieldnames = ["name", "age", "score", "attendance", "average", "letter", "passing"]

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in rows:
            writer.writerow(r)

    return filename