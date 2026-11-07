
"""Lab 6 Task 2: source-preserving word windows and sentence-aware chunks."""
import re
def windows(text,size=40,overlap=0):
    if size<=0 or overlap<0 or overlap>=size: raise ValueError("require size>0 and 0<=overlap<size")
    spans=[]; words=list(re.finditer(r"\S+",text))
    step=size-overlap
    for i in range(0,len(words),step):
        j=min(i+size,len(words))
        if i>=j: break
        spans.append((words[i].start(),words[j-1].end()))
        if j==len(words): break
    return spans
def sentence_chunks(text,size=40):
    if size<=0: raise ValueError("size must be positive")
    cuts=[0]+[m.end() for m in re.finditer(r"[.!?]\s+",text)]+[len(text)]
    out=[]; pending=None; count=0
    for a,b in zip(cuts,cuts[1:]):
        n=len(text[a:b].split())
        if not n: continue
        if n>size:
            if pending: out.append(pending)
            out.extend(windows(text[a:b],size,0))
            pending=None; count=0
        elif pending and count+n<=size:
            pending=(pending[0],b); count+=n
        else:
            if pending: out.append(pending)
            pending=(a,b); count=n
    if pending: out.append(pending)
    return out
def main():
    docs={
      "handbook":"Late work is normally penalized. Students with illness may request an extension with medical evidence before the deadline. Submit files as PDF.",
      "it":"Reset a forgotten password using the recovery link. Never share recovery codes. Contact support if the link expires.",
      "support":"Damaged parcels must be reported within 48 hours. Attach photographs of the item and packaging. Keep the shipping label."
    }
    for doc,text in docs.items():
        print("\\n",doc)
        for name,spans in [("window0",windows(text,10,0)),("window2",windows(text,10,2)),("sentence",sentence_chunks(text,10))]:
            chunks=[text[a:b] for a,b in spans]
            print(name,"count",len(chunks),"chunks",chunks)
    assert windows("",40,0)==[]
    assert len(windows("short text"))==1
    try: windows("a b",2,2)
    except ValueError: print("invalid overlap correctly rejected")
    else: raise AssertionError("invalid overlap accepted")
    long=" ".join(["word"]*95)+"."
    assert all(len(long[a:b].split())<=40 for a,b in sentence_chunks(long))
    print("All boundary checks passed.")
if __name__=="__main__": main()
