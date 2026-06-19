# Microsoft Fabric Notebook: 02 Silver Cleaning
# Purpose: Clean and standardize Bronze data into Silver Delta tables.

from pyspark.sql import functions as F

# Properties
properties = spark.table("bronze_properties")

silver_properties = (
    properties
    .select(
        F.col("property_id").cast("string"),
        F.trim(F.col("property_name")).alias("property_name"),
        F.initcap(F.trim(F.col("property_type"))).alias("property_type"),
        F.initcap(F.trim(F.col("city"))).alias("city"),
        F.upper(F.trim(F.col("state"))).alias("state"),
        F.col("square_feet").cast("long"),
        F.upper(F.trim(F.col("active_flag"))).alias("active_flag"),
        "pipeline_run_id",
        "ingestion_timestamp"
    )
    .dropDuplicates(["property_id"])
)

silver_properties.write.format("delta").mode("overwrite").saveAsTable("silver_properties")

# Leases
leases = spark.table("bronze_leases")

silver_leases = (
    leases
    .select(
        F.col("lease_id").cast("string"),
        F.col("property_id").cast("string"),
        F.col("tenant_id").cast("string"),
        F.trim(F.col("tenant_name")).alias("tenant_name"),
        F.to_date("lease_start_date").alias("lease_start_date"),
        F.to_date("lease_end_date").alias("lease_end_date"),
        F.col("leased_square_feet").cast("long"),
        F.col("monthly_rent").cast("decimal(18,2)"),
        "pipeline_run_id",
        "ingestion_timestamp"
    )
    .dropDuplicates(["lease_id"])
)

silver_leases.write.format("delta").mode("overwrite").saveAsTable("silver_leases")

# Rent Payments
payments = spark.table("bronze_rent_payments")

silver_payments = (
    payments
    .select(
        F.col("payment_id").cast("string"),
        F.col("lease_id").cast("string"),
        F.to_date("payment_date").alias("payment_date"),
        F.col("payment_amount").cast("decimal(18,2)"),
        F.initcap(F.trim(F.col("payment_status"))).alias("payment_status"),
        "pipeline_run_id",
        "ingestion_timestamp"
    )
    .dropDuplicates(["payment_id"])
)

silver_payments.write.format("delta").mode("overwrite").saveAsTable("silver_rent_payments")

print("Silver tables created.")
