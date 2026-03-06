# analyzers.py

def average(values):
    return sum(values) / len(values) if values else 0


def validate_student(student):
    """
    Validate a single student record.

    Rules:
      age: 0-120
      score: 0-100
      attendance: 0-100
      name: non-empty string

    Returns:
      (bool, str): (is_valid, reason_if_invalid)
    """
    name = student.get("name")
    age = student.get("age")
    score = student.get("score")
    attendance = student.get("attendance")

    if not isinstance(name, str) or not name.strip():
        return False, "Invalid name"
    if not isinstance(age, int) or age < 0 or age > 120:
        return False, "Invalid age"
    if not isinstance(score, (int, float)) or score < 0 or score > 100:
        return False, "Invalid score"
    if not isinstance(attendance, (int, float)) or attendance < 0 or attendance > 100:
        return False, "Invalid attendance"
    return True, ""


def analyze_students(students):
    """
    Compute statistics and categories.

    Categories:
      - honors: avg score >= 90 AND attendance >= 90
      - probation: avg score < 70 OR attendance < 75
      - passing: score >= 60

    Returns:
      dict: analysis results
    """
    valid = []
    invalid = []

    for s in students:
        ok, reason = validate_student(s)
        if ok:
            valid.append(s)
        else:
            invalid.append({"student": s, "reason": reason})

    scores = [s["score"] for s in valid]
    attendances = [s["attendance"] for s in valid]

    # Per-student averages (here it's single score; still useful structure)
    # If you later add multiple subject scores, this part scales nicely.
    per_student = []
    for s in valid:
        per_student.append(
            {
                "name": s["name"],
                "age": s["age"],
                "score": s["score"],
                "attendance": s["attendance"],
                "average": s["score"],
                "letter": score_to_letter(s["score"]),
                "passing": s["score"] >= 60,
            }
        )

    # Class stats
    class_avg = average(scores)
    class_min = min(scores) if scores else None
    class_max = max(scores) if scores else None

    # Top student
    top_student = None
    if per_student:
        top_student = per_student[0]
        for s in per_student:
            if s["average"] > top_student["average"]:
                top_student = s

    # Counts
    passing_count = sum(1 for s in per_student if s["passing"])
    pass_rate = (passing_count / len(per_student)) * 100 if per_student else 0

    total_as = sum(1 for s in per_student if s["score"] >= 90)

    honors = [s for s in per_student if s["average"] >= 90 and s["attendance"] >= 90]
    probation = [s for s in per_student if s["average"] < 70 or s["attendance"] < 75]

    subject = {
        "score": {"avg": class_avg, "min": class_min, "max": class_max},
        "attendance": {
            "avg": average(attendances),
            "min": min(attendances) if attendances else None,
            "max": max(attendances) if attendances else None,
        },
    }

    return {
        "counts": {
            "total": len(students),
            "valid": len(valid),
            "invalid": len(invalid),
            "passing": passing_count,
            "pass_rate": pass_rate,
            "total_as": total_as,
            "honors": len(honors),
            "probation": len(probation),
        },
        "subject_stats": subject,
        "top_student": top_student,
        "students": per_student,
        "invalid_rows": invalid,
    }


def score_to_letter(score):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"