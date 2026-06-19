# Microsoft Fabric Notebook: 01 Bronze Ingestion
# Purpose: Read raw source files and land them into Bronze Delta tables.

from pyspark.sql import functions as F

# In Fabric, update these paths to match your Lakehouse Files location.
RAW_BASE_PATH = "Files/sample_data/raw"
BRONZE_TABLE_PREFIX = "bronze"

pipeline_run_id = "manual_run_001"
source_system = "sample_cre_files"

sources = {
    "properties": f"{RAW_BASE_PATH}/properties.csv",
    "leases": f"{RAW_BASE_PATH}/leases.csv",
    "rent_payments": f"{RAW_BASE_PATH}/rent_payments.csv",
}

for table_name, path in sources.items():
    df = (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .csv(path)
    )

    bronze_df = (
        df
        .withColumn("source_system", F.lit(source_system))
        .withColumn("source_file_name", F.lit(path))
        .withColumn("pipeline_run_id", F.lit(pipeline_run_id))
        .withColumn("ingestion_timestamp", F.current_timestamp())
    )

    target_table = f"{BRONZE_TABLE_PREFIX}_{table_name}"

    (
        bronze_df.write
        .format("delta")
        .mode("overwrite")
        .saveAsTable(target_table)
    )

    print(f"Loaded {target_table}: {bronze_df.count()} rows")
