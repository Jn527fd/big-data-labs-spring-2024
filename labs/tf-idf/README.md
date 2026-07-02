# TF-IDF Starter Lab

Small Hadoop Streaming style starter exercise for term-frequency and TF-IDF processing.

| File | Purpose |
| --- | --- |
| `input.txt` | Small sample input with one document id and phrase per line |
| `mapper.py` | Cleans text, removes stopwords, and emits word counts by source file |
| `reducer.py` | Starter reducer that groups mapper output by file and word |
| `kick-off-hadoop.bash` | Example Hadoop command sequence for staging input and launching the job |

The reducer intentionally preserves starter-code structure from the course. A more complete experimental TF-IDF reducer is available in [`../hadoop-streaming/reducer_tfidf.py`](../hadoop-streaming/reducer_tfidf.py).
