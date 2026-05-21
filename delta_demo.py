from pyspark.sql import SparkSession
from delta import configure_spark_with_delta_pip

builder = SparkSession.builder \
    .appName("DeltaLakeDemo") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")

spark = configure_spark_with_delta_pip(builder).getOrCreate()

data = [
    ("Alice", 90),
    ("Bob", 85),
    ("Charlie", 95)
]

df = spark.createDataFrame(data, ["student", "grade"])

df.write.format("delta").mode("overwrite").save("delta-table")

delta_df = spark.read.format("delta").load("delta-table")

delta_df.show()
