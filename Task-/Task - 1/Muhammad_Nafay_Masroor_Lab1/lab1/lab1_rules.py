
"""Lab 1: transparent scholarship screening rules."""
STUDENT = "Muhammad Nafay Masroor | Roll: 251 | Section: 3D"

def rule_based(score, documents_complete, eligibility_ok, attendance_ok):
    reasons = []
    checks = {
        "score >= 70": score >= 70,
        "documents complete": documents_complete,
        "eligibility condition": eligibility_ok,
        "attendance >= 75%": attendance_ok,
    }
    reasons = [name for name, passed in checks.items() if not passed]
    return ("Review" if not reasons else "Hold"), reasons

def main():
    print(STUDENT, "\nLAB 1 - RULE TESTS")
    cases = [
        ("pass", 85, True, True, True, "Review"),
        ("eligibility fail", 85, True, False, True, "Hold"),
        ("attendance fail", 85, True, True, False, "Hold"),
        ("threshold boundary", 70, True, True, True, "Review"),
    ]
    for name, score, docs, eligible, attendance, expected in cases:
        actual, reasons = rule_based(score, docs, eligible, attendance)
        print(f"{name}: expected={expected}, actual={actual}, result={'PASS' if actual == expected else 'FAIL'}, reasons={reasons or ['all checks passed']}")
    assert all(rule_based(c[1], c[2], c[3], c[4])[0] == c[5] for c in cases)

if __name__ == "__main__":
    main()
