# Spark Streaming Lab

This lab demonstrates socket-based Spark Streaming and Spark Structured Streaming workflows. It can be run on a Google Cloud Dataproc cluster, a Spark-enabled Linux machine, or a university server with Spark installed.

## Setup

Clone the repo:

```bash
git clone https://github.com/<your-github-username>/big-data-labs-spring-2024.git
cd big-data-labs-spring-2024
```

Install helper packages as needed:

```bash
pip3 install tqdm nltk pandas feedparser
```

For stock-price examples, extra finance packages may be required depending on the script.

Add the Spark lab scripts to `PATH`:

```bash
export PATH="$PATH:$HOME/big-data-labs-spring-2024/labs/spark-streaming"
```

## Netcat Smoke Test

Start a sender shell:

```bash
nc -lk 9999
```

In another shell, connect as a listener:

```bash
nc localhost 9999
```

Anything typed in the sender should appear in the listener. Stop both with `Ctrl-C`.

## Speech Feed Into Netcat

Start a sender:

```bash
labs/spark-streaming/inaugural-speech-feeder.py 2>/dev/null | nc -lk 9999
```

Listen from a second shell:

```bash
nc localhost 9999
```

## Structured Streaming Word Count

Start the speech feeder:

```bash
labs/spark-streaming/inaugural-speech-feeder.py 2>/dev/null | nc -lk 9999
```

Run the Spark Structured Streaming word-count job in another shell:

```bash
spark-submit labs/spark-streaming/structured-network-wordcount.py localhost 9999
```

## Other Feeders

- `speech-feeder.py`: cleaned inaugural-speech text stream
- `news-feeder.py`: RSS headline stream
- `stock-price-feeder.py`: GOOG/MSFT price stream
- `aapl-feeder.py`: AAPL CSV stream from [`data/samples/aapl.csv`](../../data/samples/aapl.csv)
- `click-feeder.py`: synthetic click/query event stream

These scripts are intentionally lightweight lab tools. Several depend on live network access or external Python packages.
