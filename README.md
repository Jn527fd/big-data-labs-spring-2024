# Big Data Labs: Spring 2024

Coursework portfolio completed during the Spring 2024 semester, focused on distributed data processing with Hadoop, Spark, Hive, and Python.

This repository collects lab code, datasets, cluster setup notes, and streaming examples from a big data course. It is organized as a learning and portfolio artifact rather than a production application.

## What This Project Demonstrates

- Hadoop Streaming with custom Python mappers and reducers
- Word count and TF-IDF style text-processing exercises
- Spark Streaming and Spark Structured Streaming over socket inputs
- Hive external tables over Hadoop output
- Data ingestion examples using text corpora, web logs, stock prices, RSS headlines, and synthetic click streams
- Practical use of Google Cloud Dataproc, HDFS, `spark-submit`, and `netcat`

## Repository Map

| Path | Purpose |
| --- | --- |
| [`labs/hadoop-streaming`](labs/hadoop-streaming) | Python mapper/reducer examples for Hadoop Streaming |
| [`labs/tf-idf`](labs/tf-idf) | Starter TF-IDF exercise based on Hadoop Streaming |
| [`labs/spark-streaming`](labs/spark-streaming) | Spark Streaming demos and data feeder scripts |
| [`labs/pyspark-streaming-original`](labs/pyspark-streaming-original) | Original PySpark streaming examples kept for reference |
| [`docs`](docs) | Dataproc, Hadoop, Hive, and course reference notes |
| [`data/books`](data/books) | Public-domain Lewis Carroll text corpus used for Hadoop labs |
| [`data/samples`](data/samples) | Smaller sample datasets: stocks, logs, taxi rides, Hamlet snippets, and speeches |
| [`data/text-processing`](data/text-processing) | Review data and Poe story corpus for text-processing work |
| [`data/archives`](data/archives) | Compressed source archives retained from the coursework |
| [`tools`](tools) | Shared helper scripts used by lab feeders |

## Featured Labs

### Hadoop Streaming

The Hadoop workflow is documented in [`docs/hadoop-on-gcp.md`](docs/hadoop-on-gcp.md). It covers staging input files into HDFS, running Hadoop's built-in word count, and replacing the default mapper/reducer behavior with Python scripts from [`labs/hadoop-streaming`](labs/hadoop-streaming).

### TF-IDF Text Processing

[`labs/tf-idf`](labs/tf-idf) contains a small Hadoop Streaming starter lab that emits per-document word counts and sketches the path toward TF-IDF scoring.

### Spark Structured Streaming

[`labs/spark-streaming`](labs/spark-streaming) contains socket-based streaming examples and feeders for speeches, news headlines, stock prices, and synthetic user events. The walkthrough is in [`labs/spark-streaming/README.md`](labs/spark-streaming/README.md).

### Hive Over Hadoop Output

[`docs/hive-on-gcp.md`](docs/hive-on-gcp.md) shows how Hadoop word-count output can be exposed as a Hive external table and queried with SQL.

## How To Use This Repo

Most examples are designed for a Linux shell on Google Cloud Dataproc, a Spark-enabled machine, or a university server with Hadoop/Spark tooling installed.

Typical workflow:

```bash
git clone https://github.com/<your-github-username>/big-data-labs-spring-2024.git
cd big-data-labs-spring-2024
```

Then follow the lab-specific notes:

- Hadoop and HDFS: [`docs/hadoop-on-gcp.md`](docs/hadoop-on-gcp.md)
- Hive: [`docs/hive-on-gcp.md`](docs/hive-on-gcp.md)
- Spark streaming: [`labs/spark-streaming/README.md`](labs/spark-streaming/README.md)

## Notes

- Some files are course starter code, and some are completed or exploratory coursework.
- A few scripts require live network access for RSS feeds, NLTK corpora, stock data, or remote stopword lists.
- Hadoop and Spark examples generally assume command-line tools such as `hadoop`, `mapred`, `spark-submit`, and `nc`.
- The PDF syllabus and legacy note fragments are preserved in [`docs`](docs) for context.

