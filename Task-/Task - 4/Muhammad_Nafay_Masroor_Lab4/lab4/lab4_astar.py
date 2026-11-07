
"""Lab 4: A* heuristic audit, UCS control, and overestimate experiment."""
import heapq
GRAPH={"S":[("A",1),("B",4)],"A":[("C",2)],"B":[("G",5)],"C":[("G",3)],"G":[]}
H={"S":5,"A":4,"B":4,"C":2,"G":0}
TRUE_REMAINING={"S":6,"A":5,"B":5,"C":3,"G":0}
def best_first(graph,h,start,goal):
    pq=[(h[start],0,start,[start])]; best={start:0}; expanded=[]; processed=[]
    while pq:
        f,g,node,path=heapq.heappop(pq)
        if g!=best.get(node): continue
        processed.append((node,g,h[node],f))
        if node==goal: return g,path,expanded,processed
        expanded.append(node)
        for nxt,w in graph.get(node,[]):
            ng=g+w
            if ng<best.get(nxt,float("inf")):
                best[nxt]=ng; heapq.heappush(pq,(ng+h[nxt],ng,nxt,path+[nxt]))
    return None,None,expanded,processed
def main():
    print("LAB 4 - A* AND UCS")
    for u,edges in GRAPH.items():
        for v,w in edges:
            assert H[u] <= w+H[v], (u,v)
            print(f"consistency {u}->{v}: {H[u]} <= {w}+{H[v]} PASS")
    a=best_first(GRAPH,H,"S","G")
    z=best_first(GRAPH,{n:0 for n in H},"S","G")
    bad=dict(H); bad["C"]=10
    over=best_first(GRAPH,bad,"S","G")
    print("A* path/cost/expanded/trace:",a)
    print("UCS path/cost/expanded/trace:",z)
    print("Overestimate h(C)=10:",over)
    print("Manual first expansions: S (g,h,f)=(0,5,5); A=(1,4,5); C=(3,2,5); then G=(6,0,6) beats B=(4,4,8).")
    print("True remaining:",TRUE_REMAINING)
    assert a[0]==6 and a[1]==["S","A","C","G"]
    assert z[0]==6 and z[1]==["S","A","C","G"]
    assert over[0]==9 and over[1]==["S","B","G"]
    print("All checks passed.")
if __name__=="__main__": main()
