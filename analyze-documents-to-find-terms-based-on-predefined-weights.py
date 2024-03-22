from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col
from pyspark.sql.types import StringType
import pyspark.sql.functions as F

# Create a SparkSession
spark = SparkSession.builder \
    .appName("Find Best Matching Terms") \
    .getOrCreate()

# Create small dataframe with sample data
small_df = spark.createDataFrame([
    ("dataPeople", 0.5, 0.6, 0.7),
    ("dataDog", 0.4, 0.8, 0.3),
    ("dataBird", 0.6, 0.5, 0.9)
], ["term", "people", "dog", "bird"])

# Create large dataframe with sample data
large_df = spark.createDataFrame([
    (1, "people dog"),
    (2, "bird dog bird"),
    (3, "people bird"),
], ["id", "text"])

# Define a UDF to find the best matching term
@udf(returnType=StringType())
def find_best_matching_term(text, *topics):
    max_weight = 0
    best_term = None
    # Iterate over the small dataframe to find the best matching term
    for term, weight in zip(small_df.select("term").collect(), topics):
        weight = float(weight)
        if weight > max_weight:
            max_weight = weight
            best_term = term
    return best_term[0]

# Apply the UDF to large dataframe to find the best matching term
large_df = large_df.withColumn("best_matching_term", find_best_matching_term(col("text"), *small_df.columns[1:]))
# Join large dataframe with small dataframe based on the best matching term
joined_df = large_df.join(small_df, large_df.best_matching_term == small_df.term, "left")
# Calculate the sum of term weights
sum_of_term_weights = joined_df.select("id", *[F.sum(col(topic)).alias(f"sum_{topic}") for topic in small_df.columns[1:]])
# Find the maximum topic based on the sum of term weights
max_topic = sum_of_term_weights.select("id", F.greatest(*[col(topic) for topic in sum_of_term_weights.columns[1:]]).alias("max_topic"))
# Join the maximum topic with the joined dataframe
final_df = joined_df.join(max_topic, "id")

# Show the final dataframe
final_df.show()

# Stop the SparkSession
spark.stop()