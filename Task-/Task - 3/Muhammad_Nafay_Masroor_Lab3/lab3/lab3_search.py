
"""Lab 3: BFS, DFS, DLS, IDDFS and UCS on reproducible graphs."""
from collections import deque
import heapq
GRAPH = {
    "A": ["B", "C"], "B": ["D", "E"], "C": ["F"],
    "D": [], "E": ["G"], "F": [], "G": []
}
WEIGHTED = {
    "A": [("B", 1), ("C", 10)], "B": [("D", 1), ("E", 1)],
    "C": [("F", 1), ("G", 2)], "D": [], "E": [("G", 1)],
    "F": [], "G": []
}
def bfs(graph, start, goal):
    q=deque([(start,[start])]); seen=set(); order=[]; trace=[]
    while q:
        node,path=q.popleft()
        if node in seen: continue
        seen.add(node); order.append(node)
        trace.append((node,[n for n,_ in q]))
        if node==goal: return path,order,trace
        for nxt in graph.get(node,[]):
            if nxt not in seen: q.append((nxt,path+[nxt]))
    return None,order,trace
def dfs(graph,start,goal):
    stack=[(start,[start])]; seen=set(); order=[]; trace=[]
    while stack:
        node,path=stack.pop()
        if node in seen: continue
        seen.add(node); order.append(node); trace.append((node,[n for n,_ in stack]))
        if node==goal: return path,order,trace
        for nxt in reversed(graph.get(node,[])):
            if nxt not in seen: stack.append((nxt,path+[nxt]))
    return None,order,trace
def dls(graph,start,goal,limit):
    def visit(node,path,depth):
        if node==goal: return "FOUND",path
        if depth==limit: return ("CUTOFF",None) if graph.get(node,[]) else ("FAILURE",None)
        cutoff=False
        for nxt in graph.get(node,[]):
            if nxt in path: continue
            status,p=visit(nxt,path+[nxt],depth+1)
            if status=="FOUND": return status,p
            cutoff |= status=="CUTOFF"
        return ("CUTOFF",None) if cutoff else ("FAILURE",None)
    return visit(start,[start],0)
def iddfs(graph,start,goal,max_depth):
    attempts=[]
    for limit in range(max_depth+1):
        result=dls(graph,start,goal,limit); attempts.append((limit,*result))
        if result[0]=="FOUND": return result[1],attempts
    return None,attempts
def ucs(graph,start,goal):
    pq=[(0,0,start,[start])]; best={start:0}; order=[]; serial=1
    while pq:
        cost,_,node,path=heapq.heappop(pq)
        if cost!=best.get(node): continue
        order.append(node)
        if node==goal: return path,cost,order
        for nxt,w in graph.get(node,[]):
            if w<0: raise ValueError("UCS requires nonnegative edge costs")
            nc=cost+w
            if nc<best.get(nxt,float("inf")):
                best[nxt]=nc; heapq.heappush(pq,(nc,serial,nxt,path+[nxt])); serial+=1
    return None,float("inf"),order
def main():
    print("LAB 3 - BFS/DFS")
    for fn in (bfs,dfs):
        path,order,trace=fn(GRAPH,"A","G"); print(fn.__name__, "path=",path,"visit_order=",order)
        for row in trace: print(" trace",row)
    print("DLS")
    for lim in (1,2,3,4): print(lim,dls(GRAPH,"A","G",lim))
    print("IDDFS",iddfs(GRAPH,"A","G",4))
    print("UCS weighted",ucs(WEIGHTED,"A","G"))
    assert bfs(GRAPH,"A","G")[0]==["A","B","E","G"]
    assert dfs(GRAPH,"A","G")[0]==["A","B","E","G"]
    assert dls(GRAPH,"A","G",2)[0]=="CUTOFF"
    assert dls(GRAPH,"A","G",3)[0]=="FOUND"
    assert ucs(WEIGHTED,"A","G")[1]==3
    print("All checks passed.")
if __name__=="__main__": main()
