from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.functions import sum

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("BigDataPipeline") \
    .getOrCreate()

print("Spark Started")

# Read CSV data
df = spark.read.csv(
    "data/ecommerce.csv",
    header=True,
    inferSchema=True
)

#df.show(5)
#df.printSchema()
df=df.dropna()
df=df.dropDuplicates()
df = df.withColumnRenamed("InvoiceNo", "invoice_no")
# df.show(5)
# df.printSchema()

df=df.withColumn("total_price", col("Quantity")*col("UnitPrice"))
df = df.filter(col("Quantity") > 0)
# df.show(5)


sales_df = df.groupBy("Country").agg(
    sum("total_price").alias("total_sales")
)

# sales_df.show()

df.createOrReplaceTempView("sales")

result = spark.sql("""
SELECT Country,
       SUM(total_price) as revenue
FROM sales
GROUP BY Country
ORDER BY revenue DESC
""")

result.show()

# Repartition and write the data back to Parquet
df = df.repartition(4)
df.write \
    .mode("overwrite") \
    .partitionBy("Country") \
    .parquet("Data/processed_data")

# df.cache()
# df.explain()