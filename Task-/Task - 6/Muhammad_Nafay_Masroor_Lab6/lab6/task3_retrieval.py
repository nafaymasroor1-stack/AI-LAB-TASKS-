
"""Lab 6 Task 3: lightweight TF-IDF-free lexical retrieval evaluation.
Uses a deterministic token-overlap baseline so it runs offline without model downloads.
"""
import json, re, time, csv
from pathlib import Path
from task2_chunks import windows, sentence_chunks
def tokens(s): return set(re.findall(r"\w+",s.casefold(),re.UNICODE))
def chunks_for(corpus,strategy):
    out=[]
    for doc,text in corpus.items():
        spans=windows(text,40,0 if strategy=="window0" else 10) if strategy!="sentence" else sentence_chunks(text,40)
        for i,(a,b) in enumerate(spans):
            out.append({"id":f"{doc}:{i}","doc":doc,"start":a,"end":b,"text":text[a:b]})
    return out
def rank(query,chunks):
    qt=tokens(query)
    scored=[]
    for c in chunks:
        ct=tokens(c["text"]); score=len(qt&ct)/max(1,len(qt|ct))
        scored.append((score,c))
    return sorted(scored,key=lambda x:-x[0])[:3]
def main():
    corpus=json.loads(Path("corpus.json").read_text(encoding="utf-8"))
    queries=json.loads(Path("queries.json").read_text(encoding="utf-8"))
    logs=[]
    for strategy in ("window0","window10","sentence"):
        chunks=chunks_for(corpus,strategy)
        for split in ("dev","test"):
            hit=[]; rr=[]
            for q in [x for x in queries if x["split"]==split]:
                start=time.perf_counter(); top=rank(q["query"],chunks); elapsed=time.perf_counter()-start
                good=[i for i,(_,c) in enumerate(top,1) if q["doc"]==c["doc"] and q["evidence"] and q["evidence"] in c["text"]]
                if q["doc"] is not None: hit.append(bool(good)); rr.append(1/good[0] if good else 0)
                logs.append({"strategy":strategy,"split":split,"query":q["query"],"top_ids":";".join(c["id"] for _,c in top),"top_scores":";".join(f"{s:.3f}" for s,_ in top),"latency_s":f"{elapsed:.6f}","answerable":q["doc"] is not None})
            print(strategy,split,"chunks",len(chunks),"Hit@3",sum(hit)/len(hit) if hit else "n/a","MRR@3",sum(rr)/len(rr) if rr else "n/a")
    with open("retrieval_log.csv","w",newline="",encoding="utf-8") as f:
        w=csv.DictWriter(f,fieldnames=logs[0].keys()); w.writeheader(); w.writerows(logs)
    print("Wrote retrieval_log.csv; lexical overlap is a baseline, not a sentence-embedding model.")
if __name__=="__main__": main()
