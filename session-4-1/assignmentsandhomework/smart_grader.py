# smart_grader.py
# Project: Smart Grading System (complex boolean logic + detailed report)

def letter_from_score(score):
    """Fallback grading based on score only."""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def grade_message(letter):
    messages = {
        "A": "Excellent!",
        "B": "Good job!",
        "C": "Satisfactory.",
        "D": "Needs improvement.",
        "F": "Please see instructor."
    }
    return messages.get(letter, "")

def smart_grade(score, attendance, participation):
    """
    Rules:
    - Score >= 90 and attendance >= 80: A
    - Score >= 80 and (attendance >= 70 or participation): B
    - Else: based on score only
    """
    # Basic validation (optional but professional)
    if score < 0 or score > 100 or attendance < 0 or attendance > 100:
        return {
            "final_grade": "INVALID",
            "reason": "Score and attendance must be between 0 and 100.",
            "message": "Fix inputs and try again."
        }

    auto_a = (score >= 90) and (attendance >= 80)
    auto_b = (score >= 80) and ((attendance >= 70) or participation)

    if auto_a:
        final = "A"
        reason = "Rule A: score >= 90 AND attendance >= 80"
    elif auto_b:
        final = "B"
        reason = "Rule B: score >= 80 AND (attendance >= 70 OR participation)"
    else:
        final = letter_from_score(score)
        reason = "Fallback: grade based on score only"

    return {
        "final_grade": final,
        "reason": reason,
        "message": grade_message(final)
    }


# -----------------------------
# INPUTS (edit these to test)
#
