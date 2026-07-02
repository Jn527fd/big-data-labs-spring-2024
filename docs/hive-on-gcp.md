# Hive on GCP Dataproc

This note shows how the Hadoop word-count output can be queried through Hive as an external table.

Start from a Dataproc cluster with the repository cloned on the master node:

```bash
git clone https://github.com/<your-github-username>/big-data-labs-spring-2024.git
cd big-data-labs-spring-2024
```

The setup mirrors the Hadoop workflow in [`hadoop-on-gcp.md`](hadoop-on-gcp.md).

## Load Input Files Into HDFS

```bash
hadoop fs -mkdir -p /user/$USER/five-books
hadoop fs -put data/books/* /user/$USER/five-books
hadoop fs -ls /user/$USER/five-books
```

## Generate Word-Count Output

```bash
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-mapreduce-examples.jar \
  wordcount /user/$USER/five-books /user/$USER/books-count-hive
```

Check that the output exists:

```bash
hadoop fs -ls /user/$USER/books-count-hive
```

## Create A Hive External Table

Open Hive:

```bash
hive
```

Create an external table over the Hadoop output directory:

```sql
CREATE EXTERNAL TABLE bookscount (
  word string,
  count int
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
LOCATION '/user/${env:USER}/books-count-hive';
```

If variable expansion is not enabled in your Hive session, replace `${env:USER}` with the concrete HDFS username used above.

## Query The Table

```sql
SELECT word, count
FROM bookscount
WHERE count > 2000
SORT BY count DESC;
```

This demonstrates the course concept: Hadoop output files can be treated as table data and queried with SQL through Hive.
