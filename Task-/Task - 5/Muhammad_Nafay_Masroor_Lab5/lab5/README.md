# Lab 5 — Minimax and Alpha-Beta pruning

**Student:** Muhammad Nafay Masroor · **Roll:** 251 · **Section:** 3D

## Run
```bash
python lab5_minimax.py
```
No external packages. The script compares the root value and terminal-leaf evaluations for plain Minimax and Alpha-Beta, then reverses branch order. Both algorithms must return the same root value; pruning efficiency depends on ordering.

## Viva notes
MAX selects the larger child value; MIN selects the smaller. Alpha is MAX's lower bound and beta is MIN's upper bound. A branch is pruned when alpha ≥ beta because it cannot change the ancestor's decision. Leaf counts include only evaluated terminal utilities.
