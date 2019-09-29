# MapReduce and Spark Application

### Verify Hadoop and Spark with host and port

- To check Hadoop:
http://[master-client-port]/dfshealth.html

- To check Spark:
http://[master-client-port]:8080/


### Some useful commands
- To copy a file to hdfs

  ```sh
  ~/hadoop-3.1.2/bin/hadoop fs -put input.csv hdfs://[master-client-port]:9000/input.csv
  ```

- To list all files on hdfs

  ```sh
  ~/hadoop-3.1.2/bin/hadoop fs -ls hdfs://[master-client-port]:9000/
  ```

- To delete a file on hdfs

  ```sh
  ~/hadoop-3.1.2/bin/hdfs dfs -rm -r -skipTrash hdfs://[master-client-port]/output.csv 
  ```
