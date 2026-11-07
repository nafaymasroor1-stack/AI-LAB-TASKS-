
"""Lab 2: boundary and repeat-command assertions."""
from lab2_model import StatefulClassroomAgent
def main():
    a = StatefulClassroomAgent()
    trace = [(29,True),(29,True),(20,True),(26,True),(19,True),(29,False)]
    expected = [("COOL",True),("COOL",False),("IDLE",True),("IDLE",False),("WARM",True),("ECO",True)]
    for p, exp in zip(trace, expected):
        _, target, send = a.act(*p)
        print(p, target, send)
        assert (target, send) == exp
    print("All checks passed.")
if __name__ == "__main__": main()
