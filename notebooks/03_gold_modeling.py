# Microsoft Fabric Notebook: 03 Gold Modeling
# Purpose: Build Power BI-ready dimension and fact tables.

from pyspark.sql import functions as F
from pyspark.sql.window import Window

properties = spark.table("silver_properties")
leases = spark.table("silver_leases")
payments = spark.table("silver_rent_payments")

# Dimension: Property
dim_property = (
    properties
    .select(
        "property_id",
        "property_name",
        "property_type",
        "city",
        "state",
        "square_feet",
        "active_flag"
    )
    .dropDuplicates(["property_id"])
)

property_window = Window.orderBy("property_id")
dim_property = dim_property.withColumn("property_key", F.row_number().over(property_window))

dim_property.write.format("delta").mode("overwrite").saveAsTable("dim_property")

# Dimension: Tenant
dim_tenant = (
    leases
    .select("tenant_id", "tenant_name")
    .dropDuplicates(["tenant_id"])
)

tenant_window = Window.orderBy("tenant_id")
dim_tenant = dim_tenant.withColumn("tenant_key", F.row_number().over(tenant_window))

dim_tenant.write.format("delta").mode("overwrite").saveAsTable("dim_tenant")

# Fact: Rent Payment
fact_rent_payment = (
    payments.alias("p")
    .join(leases.alias("l"), on="lease_id", how="left")
    .join(dim_property.alias("dp"), on="property_id", how="left")
    .join(dim_tenant.alias("dt"), on="tenant_id", how="left")
    .select(
        F.col("p.payment_id"),
        F.col("p.lease_id"),
        F.col("dp.property_key"),
        F.col("dt.tenant_key"),
        F.col("p.payment_date"),
        F.col("p.payment_amount"),
        F.col("p.payment_status")
    )
)

payment_window = Window.orderBy("payment_id")
fact_rent_payment = fact_rent_payment.withColumn("payment_key", F.row_number().over(payment_window))

fact_rent_payment.write.format("delta").mode("overwrite").saveAsTable("fact_rent_payment")

print("Gold tables created.")
