
"""Lab 2: stateless classroom reflex agent."""
STUDENT = "Muhammad Nafay Masroor | Roll: 251 | Section: 3D"
class ClassroomAgent:
    def act(self, temp, occupied):
        if not occupied: return "ECO"
        if temp > 26: return "COOL"
        if temp < 20: return "WARM"
        return "IDLE"
def main():
    print(STUDENT, "\nLAB 2 - REFLEX AGENT")
    percepts = [(29, True), (29, True), (20, True), (26, True), (19, True), (29, False)]
    agent = ClassroomAgent()
    for i, p in enumerate(percepts, 1):
        print(i, p, "target mode", agent.act(*p))
if __name__ == "__main__": main()
