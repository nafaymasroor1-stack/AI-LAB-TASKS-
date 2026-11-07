# Lab 2 — Intelligent agents and PEAS

**Student:** Muhammad Nafay Masroor · **Roll:** 251 · **Section:** 3D

## Run
```bash
python lab2_percepts.py
python lab2_model.py
python lab2_check.py
```
No external packages. ECO/COOL/WARM/IDLE are simulated labels; no physical HVAC hardware is controlled.

## PEAS report content
**Delivery robot:** Performance—safe delivery, on-time arrival, low energy; Environment—campus paths, pedestrians, doors, weather; Actuators—wheels, brakes, speaker/display; Sensors—camera, lidar/depth, GPS/odometry, proximity sensors. Trade-off: speed must not override collision avoidance.

**LLM student-support agent:** Performance—correctness, grounded answers, privacy, helpfulness; Environment—student query, approved knowledge base, academic calendar; Actuators—reply, cite source, ask clarification/escalate; Sensors—user text, retrieved documents, permitted tool results. Assumption: read-only access to approved public/course content, no access to grades or private records. Trade-off: response speed must not reward unsupported answers.

**Environment classification:** A simplified simulator with all variables exposed and fixed transitions can be fully observable and deterministic. Real robot navigation is partially observable and stochastic (occlusion, people, wheel slip). Real student support is partially observable (missing context) and stochastic (ambiguous language, changing source content); a frozen deterministic test harness can be deterministic at its chosen boundary.
