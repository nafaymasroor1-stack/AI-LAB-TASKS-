
"""Lab 2: stateful agent avoids sending duplicate mode commands."""
class StatefulClassroomAgent:
    def __init__(self):
        self.previous_mode = None
    def act(self, temp, occupied):
        if not isinstance(occupied, bool): raise TypeError("occupied must be bool")
        if not isinstance(temp, (int, float)): raise TypeError("temperature must be numeric")
        if not occupied: target = "ECO"
        elif temp > 26: target = "COOL"
        elif temp < 20: target = "WARM"
        else: target = "IDLE"
        send = target != self.previous_mode
        old = self.previous_mode
        self.previous_mode = target
        return old, target, send
def main():
    print("LAB 2 - STATEFUL AGENT TRACE")
    agent = StatefulClassroomAgent()
    for i, percept in enumerate([(29,True),(29,True),(20,True),(26,True),(19,True),(29,False),(29,False)], 1):
        old, target, send = agent.act(*percept)
        print(f"{i}: previous={old}, percept={percept}, target={target}, command={'SEND' if send else 'NO SEND'}")
if __name__ == "__main__": main()
