# Twitter Sentiment Analysis and Tweet Extraction

## Project Description

This project uses pySpark to set up a Spark Streaming environment, which is used to handle realtime
Twitter data. The tweets are obtained through a TCP socket over an in-place Twitter API connection. 

A user can interact with this process by choosing keywords, by which the data flow
of tweets is filtered. The texts of the incoming tweets are then saved in a DStream (discretized
stream) object consisting of Resilient Distributed Datasets (RDDs) in the Spark environment.
Next a couple of transformation are applied to the RDDs and finally they are saved into a temporary
SQL table for later queries. One SQL table is comprised of the different hashtags found in
the texts and their respective number of appearances during the stream. This data is used to
visualize the most relevant hashtags of the topic in question. With the help of Spark Streaming
the graph gets updated with additionally gathered data every minute. The other SQL table is
only used to obtain the full tweets in order to apply a sentiment analysis on the individual texts.
The various tweets are then categorized in either ”positive”, ”neutral” or ”negative” sentiment
classes. These are then counted and plotted to provide an overall sense of sentiment regarding
the discussion of the desired topic.

### Methods Used
* App to Stream Real-Time Twitter Data
* Resilient Distributed Databases (RDDs)
* Data Visualization

### Technologies
* Python
* tweepy (for getting data via the Twitter API)
* Apache Spark
* SQL
* matplotlib, seaborn