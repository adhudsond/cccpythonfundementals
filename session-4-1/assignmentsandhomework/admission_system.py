# admission_system.py
# College Admission Logic (and/or/not) + clear explanations

def admission_decision(gpa, test_score, extracurriculars, essay_quality):
    # 1) Auto-accept
    if gpa >= 3.8 and test_score >= 1400:
        decision = "AUTO-ACCEPT"
        explanation = "Meets auto-accept thresholds (GPA >= 3.8 AND test >= 1400)."

    # 3) Interview (placed before Consider so it doesn't get swallowed by Consider)
    elif essay_quality.lower() == "excellent" and gpa >= 3.0:
        decision = "INTERVIEW"
        explanation = "Strong essay + solid GPA (essay == 'excellent' AND GPA >= 3.0)."

    # 2) Consider
    elif (gpa >= 3.5 and test_score >= 1200) or extracurriculars:
        decision = "CONSIDER"
        explanation = "Meets consideration rule ((GPA >= 3.5 AND test >= 1200) OR extracurriculars)."

    # 4) Reject
    else:
        decision = "REJECT"
        explanation = "Does not meet auto-accept, interview, or consider rules."

    print("=" * 52)
    print("COLLEGE ADMISSION DECISION")
    print("=" * 52)
    print(f"GPA:             {gpa}")
    print(f"Test score:      {test_score}")
    print(f"Extracurriculars:{extracurriculars}")
    print(f"Essay quality:   {essay_quality}")
    print("-" * 52)
    print(f"Decision:        {decision}")
    print(f"Explanation:     {explanation}")
    print("=" * 52 + "\n")


# --- Given values ---
gpa = 3.7
test_score = 1280
extracurriculars = True
essay_quality = "excellent"

admission_decision(gpa, test_score, extracurriculars, essay_quality)

# --- Test with different combinations ---
test_cases = [
    (3.9, 1450, False, "good"),        # auto-accept
    (3.2, 1100, False, "excellent"),   # interview
    (3.6, 1210, False, "average"),     # consider (gpa+test)
    (2.9, 1000, True, "poor"),         # consider (extracurriculars)
    (2.5, 900, False, "poor")          # reject
]

for g, t, e, q in test_cases:
    admission_decision(g, t, e, q)
