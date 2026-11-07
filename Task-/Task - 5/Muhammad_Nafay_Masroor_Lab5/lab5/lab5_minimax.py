
"""Lab 5: Minimax and Alpha-Beta with leaf counts and move ordering."""
from math import inf
TREE=[[[3,5],[2,9]],[[3,5],[2,9]]]  # depth-3 binary tree represented as leaves
def minimax(values, maximizing=True, counter=None):
    if counter is None: counter={"leaves":0}
    if isinstance(values,(int,float)):
        counter["leaves"]+=1; return values
    child=[minimax(v,not maximizing,counter) for v in values]
    return max(child) if maximizing else min(child)
def alphabeta(values, alpha=-inf, beta=inf, maximizing=True, counter=None):
    if counter is None: counter={"leaves":0,"pruned":0}
    if isinstance(values,(int,float)):
        counter["leaves"]+=1; return values
    result=-inf if maximizing else inf
    for i,child in enumerate(values):
        val=alphabeta(child,alpha,beta,not maximizing,counter)
        if maximizing:
            result=max(result,val); alpha=max(alpha,result)
        else:
            result=min(result,val); beta=min(beta,result)
        if alpha>=beta:
            counter["pruned"] += len(values)-i-1
            break
    return result
def run(tree,label):
    c1={"leaves":0}; v1=minimax(tree,True,c1)
    c2={"leaves":0,"pruned":0}; v2=alphabeta(tree,counter=c2)
    print(label, "minimax=",v1,c1,"alpha_beta=",v2,c2)
    assert v1==v2
def main():
    print("LAB 5 - GAME TREE")
    run(TREE,"left-to-right")
    reversed_tree=[list(reversed(branch)) for branch in reversed(TREE)]
    run(reversed_tree,"reordered")
    # Explicit reference tree from the manual is padded to eight leaves.
    print("Manual reference leaves [3,5,2,9,3,5,2,9]")
    padded = [3,5,2,9,3,5,2,9]
    tree = [[padded[0:2], padded[2:4]], [padded[4:6], padded[6:8]]]
    print("Root value:", minimax(tree))
    print("All checks passed.")
if __name__=="__main__": main()
