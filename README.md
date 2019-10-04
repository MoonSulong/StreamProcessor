# Stream Processer
An application with Spark, Kafka, Flink and Flask

## Table of contents
* [1. Project Description](#1-project-descriptions)
* [2. Spark Config](#2-spark-config)
* [3. Continue](#3-continue...)

## 1. Project Description 

- A framework with `Spark` to process real-time Twitter stream data based on hashtags for popular words analysis 
- A positive/negative keywords monitor in a consistent manner to handle 60 tweets per second with `Kafka`
- Optimized processing efficiency with `Flink`, and visualized 1% of filtered public Tweets with `Ajax` and `Flask` 
   
![Spring MVC framework](https://raw.githubusercontent.com/MoonSulong/Ecommerce/master/img/SpringMVC.png)
> Spring MVC framework

## 2. Spark Config
- Develop Environment(Google Cloud)
   * Linux: Ubuntu 16.04 LTS, 15GB disk, 
	** sh -c "$(curl -fsSL https://raw.githubusercontent.com/Linuxbrew/install/master/install.sh)"
	** test -d ~/.linuxbrew && eval $(~/.linuxbrew/bin/brew shellenv)
	** test -d /home/linuxbrew/.linuxbrew && eval $(/home/linuxbrew/.linuxbrew/bin/brew shellenv)
	** test -r ~/.bash_profile && echo "eval \$($(brew --prefix)/bin/brew shellenv)" >>~/.bash_profile
	** echo "eval \$($(brew --prefix)/bin/brew shellenv)" >>~/.profile
  * Java & Scala
	** sudo apt update
	** sudo add-apt-repository ppa:webupd8team/java
	** sudo apt-get install build-essential curl file git
	** sudo apt-get install openjdk-8-jdk
	** brew install scala
  * Spark
	** wget https://archive.apache.org/dist/spark/spark-1.6.3/spark-1.6.3-bin-hadoop2.4.tgz
	** tar -xvzf spark-1.6.3-bin-hadoop2.4.tgz
	** rm -rf spark-1.6.3-bin-hadoop2.4.tgz

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
## 3. Continue...
