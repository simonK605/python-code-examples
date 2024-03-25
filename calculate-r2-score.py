from pyspark.ml.linalg import Vectors
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Test credentials
# Dummy linear regression model
model = LinearRegression()

# Example DataFrame with test data (replace with your actual data)
# Assume df is a DataFrame with columns: 'price', 'area', 'height', 'days_since_bought', 'label'
data = [
    (100, 200, 10, 30, 300),
    (150, 250, 12, 20, 350),
    (120, 220, 11, 25, 320)
]
df = spark.createDataFrame(data, ['price', 'area', 'height', 'days_since_bought', 'label'])

def calculate_r2_score(row):
    """
    Calculates the R2 score for a given row using the dummy linear regression model.

    Args:
        row (pyspark.sql.Row): A row from the DataFrame containing features and label.

    Returns:
        float: The R2 score for the given row.
    """
    # Extract features from the row
    features = [row['price'], row['area'], row['height'], row['days_since_bought']]

    # Predict the label using the linear regression model
    prediction = model.predict([features])

    # Return the R2 score
    return r2_score([row['label']], prediction)

# Apply the function to each row of the DataFrame using map
r2_scores = df.rdd.map(calculate_r2_score)

# Collect the R2 scores
r2_scores = r2_scores.collect()

# Calculate the average R2 score
average_r2_score = sum(r2_scores) / len(r2_scores)

print("Average R2 Score:", average_r2_score)
