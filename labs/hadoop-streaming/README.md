# Hadoop Streaming

Python mapper and reducer scripts used in the Hadoop Streaming lab.

| File | Purpose |
| --- | --- |
| `mapper_noll.py` | Word-count mapper adapted from Michael Noll's Hadoop Streaming tutorial |
| `reducer_noll.py` | Standard reducer for sorted word-count mapper output |
| `mapper_count_tfidf.py` | Mapper that emits per-file word counts for TF-IDF style processing |
| `reducer_count.py` | Starter reducer for inspecting per-file word counts |
| `reducer_tfidf.py` | Experimental TF-IDF reducer implementation |

See [`../../docs/hadoop-on-gcp.md`](../../docs/hadoop-on-gcp.md) for the Dataproc/HDFS workflow.
