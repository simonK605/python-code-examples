from pyspark.ml.feature import VectorAssembler, StringIndexer
from pyspark.ml.classification import LogisticRegression
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import IntegerType, StringType
from pyspark.ml.evaluation import BinaryClassificationEvaluator

# Create a SparkSession
spark = SparkSession.builder.appName("LogisticRegressionExample").getOrCreate()

# Sample data
data = [("1", "0", 3), ("0", "2", 0), ("3", "1", 2), ("0", "0", 1)]
df = spark.createDataFrame(data, ["feature1", "feature2", "label"])

# Convert string columns to integer
df = df.withColumn("feature1", col("feature1").cast(IntegerType()))
df = df.withColumn("feature2", col("feature2").cast(IntegerType()))

# Use VectorAssembler to combine features
assembler = VectorAssembler(inputCols=["feature1", "feature2"], outputCol="features")
output = assembler.transform(df)

# Keep only the features and label columns
final_data = output.select("features", "label")

# Split the data into training and testing sets
train_data, test_data = final_data.randomSplit([0.7, 0.3], seed=42)

# Create a Logistic Regression model
lr = LogisticRegression()

# Fit the model to the training data
lr_model = lr.fit(train_data)

# Make predictions on the testing data
predictions = lr_model.transform(test_data)

# Evaluate the model using BinaryClassificationEvaluator
evaluator = BinaryClassificationEvaluator(labelCol="label")
accuracy = evaluator.evaluate(predictions)

# Print the model evaluation metrics
print("Model Evaluation Metrics:")
print("Accuracy:", accuracy)

# Stop the SparkSession
spark.stop()