
"""Lab 1: compare explicit rules with a supplied probability threshold."""
def symbolic(score, complete):
    return "Review" if complete and score >= 70 else "Hold"
def threshold(probability):
    return "Review" if probability >= 0.70 else "Hold"
def main():
    print("case | symbolic | threshold | disagreement")
    cases = [
        ("complete_high", 82, True, .81),
        ("complete_low", 68, True, .74),
        ("incomplete_high", 91, False, .88),
        ("boundary", 70, True, .70),
    ]
    for name, score, complete, probability in cases:
        a, b = symbolic(score, complete), threshold(probability)
        print(name, a, b, a != b, sep=" | ")
if __name__ == "__main__":
    main()
