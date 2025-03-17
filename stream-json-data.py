from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder \
    .appName("JSONFileStream") \
    .getOrCreate()

# Define the path to the directory containing JSON files
json_path = "file:///path/to/json/directory"

# Read JSON files as a streaming DataFrame
streaming_df = spark.readStream \
    .format("json") \
    .option("path", json_path) \
    .load()

# Perform transformations and aggregations as needed
# For example, you can display the streaming DataFrame
streaming_query = streaming_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

# Wait for the termination of the streaming query
streaming_query.awaitTermination()

# Stop the SparkSession
spark.stop()
