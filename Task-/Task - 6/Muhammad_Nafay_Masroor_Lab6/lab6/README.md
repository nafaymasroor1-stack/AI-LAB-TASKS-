# Lab 6 — NLP fundamentals, chunking and retrieval

**Student:** Muhammad Nafay Masroor · **Roll:** 251 · **Section:** 3D

## Run (Python 3.10+, offline baseline)
```bash
python task1_tokens.py
python task2_chunks.py
python task3_retrieval.py
```
The retrieval evaluation intentionally uses a transparent token-overlap baseline to run without a model download. It is not presented as a pretrained embedding model. The lab manual also requires a real SentenceTransformer comparison; install `sentence-transformers` and implement/run the embedding backend before claiming that requirement is complete. Synthetic corpus text is teaching data, not real university policy.

## Included evidence
Six tokenization examples (punctuation, contraction, email, identifier, empty input, Urdu); word windows with 0/10 overlap; sentence-aware packing; source offsets; invalid-overlap/empty/short/long-sentence checks; five documents; eight answerable and two unanswerable queries; dev/test split; top-3 lexical retrieval metrics and CSV logs.

## Limitations
Regex word-like tokenization is not a full multilingual tokenizer. Sentence splitting by punctuation mishandles abbreviations. Lexical overlap misses paraphrases and can rank irrelevant passages for unanswerable queries. Inspect retrieved evidence; do not treat a score as proof of truth.
