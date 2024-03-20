# Import necessary libraries
from pyspark.sql import SparkSession
import mlflow.pyfunc

# Create a SparkSession
spark = SparkSession.builder \
    .appName("DeployMLflowModel") \
    .getOrCreate()

# Define the model URI
MODEL_URI = "models:/<DeployMLflowModel>/<1.3>"
try:
    # Load the model
    model = mlflow.pyfunc.load_model(MODEL_URI)
except Exception as e:
    print("Error occurred while loading the model: ", str(e))
    spark.stop()

try:
    # Read the data
    test_data = spark.read.csv("test_data.csv", header=True, inferSchema=True)

    # Define a function to make predictions on each partition
    def predict_partition(iter):
        for row in iter:
            predictions = model.predict(row)
            # Show the predictions for the current row
            print(predictions)

    # Apply the function to each partition of the DataFrame
    test_data.foreachPartition(predict_partition)

except Exception as e:
    print("Error occurred while making predictions: ", str(e))
finally:
    # Stop the SparkSession
    spark.stop()