# Microsoft Fabric Notebook: 04 Data Validation
# Purpose: Run basic validation checks across Bronze, Silver, and Gold layers.

from pyspark.sql import functions as F

validation_results = []

def add_result(check_name, status, details):
    validation_results.append({
        "check_name": check_name,
        "status": status,
        "details": details
    })

def table_exists(table_name):
    try:
        spark.table(table_name)
        return True
    except Exception:
        return False

required_tables = [
    "bronze_properties",
    "bronze_leases",
    "bronze_rent_payments",
    "silver_properties",
    "silver_leases",
    "silver_rent_payments",
    "dim_property",
    "dim_tenant",
    "fact_rent_payment"
]

for table_name in required_tables:
    exists = table_exists(table_name)
    add_result(
        f"Table exists: {table_name}",
        "PASS" if exists else "FAIL",
        f"{table_name} exists={exists}"
    )

# Row count checks
for table_name in required_tables:
    if table_exists(table_name):
        count_value = spark.table(table_name).count()
        add_result(
            f"Row count > 0: {table_name}",
            "PASS" if count_value > 0 else "FAIL",
            f"row_count={count_value}"
        )

# Gold relationship checks
if table_exists("fact_rent_payment"):
    fact = spark.table("fact_rent_payment")
    missing_property_keys = fact.filter(F.col("property_key").isNull()).count()
    missing_tenant_keys = fact.filter(F.col("tenant_key").isNull()).count()

    add_result(
        "Fact has valid property keys",
        "PASS" if missing_property_keys == 0 else "FAIL",
        f"missing_property_keys={missing_property_keys}"
    )

    add_result(
        "Fact has valid tenant keys",
        "PASS" if missing_tenant_keys == 0 else "FAIL",
        f"missing_tenant_keys={missing_tenant_keys}"
    )

validation_df = spark.createDataFrame(validation_results)
display(validation_df)

failures = validation_df.filter(F.col("status") == "FAIL").count()

if failures > 0:
    raise Exception(f"Validation failed with {failures} failed checks.")
else:
    print("All validation checks passed.")
