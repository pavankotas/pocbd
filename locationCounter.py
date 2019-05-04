from pyspark.sql import SparkSession
from pyspark.sql import Row
from pyspark.sql import functions

# def parseInput(line):
#     fields = line.split()
#     return Row(country)
if __name__ == "__main__":
    spark = SparkSession.builder.appName("LocationCounter").getOrCreate()
    lines = spark.sparkContext.textFile("../hashtags.txt").toDF()
    lines.take(10)
    # locations = lines.map(parseInput)
    # filtered = lines.take(10)
    spark.stop()
