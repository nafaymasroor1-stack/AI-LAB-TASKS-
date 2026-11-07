# Lab 3 — Uninformed search

**Student:** Muhammad Nafay Masroor · **Roll:** 251 · **Section:** 3D

## Run
```bash
python lab3_search.py
```
No third-party packages. The original unweighted graph uses A→B,C; B→D,E; C→F; E→G. The weighted extension adds an alternative C→G route and nonnegative costs; it is intentionally distinguished from the manual-trace graph.

## Expected interpretation
BFS and DFS find A→B→E→G in the supplied successor order, with different visit traces. DLS returns CUTOFF at limits 1 and 2 and FOUND at 3 and 4. IDDFS repeats bounded searches with a path-local cycle check. UCS minimizes total weight rather than number of hops. The supplied small weighted extension demonstrates cost-based search; edit edge costs to explore different hop/cost trade-offs.
