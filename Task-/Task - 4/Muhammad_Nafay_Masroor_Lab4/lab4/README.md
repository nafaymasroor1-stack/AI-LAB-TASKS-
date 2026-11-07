# Lab 4 — A* search and heuristic audit

**Student:** Muhammad Nafay Masroor · **Roll:** 251 · **Section:** 3D

## Run
```bash
python lab4_astar.py
```
No external packages. The graph and heuristic follow the lab manual. The script prints edge-wise consistency checks, A*/UCS paths and traces, expansion counts, and a deliberate overestimate test.

## Results to discuss
Optimal route S→A→C→G costs 6; alternative S→B→G costs 9. Supplied heuristic is admissible on this finite example and consistent on every edge. With h(C)=10 (true remaining cost 3), A* returns the cost-9 route in this graph, demonstrating loss of the optimality guarantee. Goal processing is logged but excluded from expanded-node count; stale queue entries are ignored.
