from pyspark.sql.types import ArrayType, IntegerType
from pyspark.sql.functions import regexp_replace, udf
from pyspark.ml.image import ImageSchema
import numpy as np


def image_to_numpy(image_data):
    """
    Converts image data to a numpy array.

    Args:
        image_data: Image data in binary format.

    Returns:
        numpy array: Image data represented as a numpy array.
    """
    height = 200
    width = 200
    n_channels = 3
    return np.reshape(image_data, (height, width, n_channels)).tolist()


# Define a user-defined function (UDF) to convert image data to numpy arrays
spark_to_np_array = udf(image_to_numpy, ArrayType(ArrayType(ArrayType(IntegerType()))))

# Load images from the specified directory
images_df = ImageSchema.readImages("/mnt/images/*", recursive=True, numPartitions=100)

# Extract file names and apply the UDF to convert images to numpy arrays
images_df = images_df.withColumn("FileName", regexp_replace('image.origin', 'dbfs:/mnt/images/', '')) \
    .withColumn("ImageArray", spark_to_np_array(images_df["image.data"])) \
    .select("FileName", "ImageArray")
