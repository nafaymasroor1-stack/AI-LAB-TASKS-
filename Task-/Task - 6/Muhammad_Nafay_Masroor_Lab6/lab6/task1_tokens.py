
"""Lab 6 Task 1: whitespace and Unicode word-like token comparison."""
import re
SAMPLES=["Hello, world!","I can't attend.","nafay@example.com","CS4944","", "یہ مصنوعی تعلیمی متن ہے"]
PATTERN=re.compile(r"\w+|[^\w\s]",re.UNICODE)
def main():
    print("LAB 6 TASK 1 - TOKENIZATION")
    for s in SAMPLES:
        ws=s.split(); regex=PATTERN.findall(s)
        print("text:",repr(s)); print("whitespace:",ws,len(ws)); print("word-like:",regex,len(regex))
    print("Note: regex is illustrative, not a complete Urdu or multilingual tokenizer.")
if __name__=="__main__": main()
