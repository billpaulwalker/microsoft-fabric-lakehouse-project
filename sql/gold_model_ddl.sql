-- Example Gold model DDL
-- Adjust syntax depending on whether you implement Gold as Delta tables,
-- Fabric Warehouse tables, or Lakehouse tables.

CREATE TABLE IF NOT EXISTS dim_property (
    property_key        BIGINT,
    property_id         VARCHAR(50),
    property_name       VARCHAR(200),
    property_type       VARCHAR(100),
    city                VARCHAR(100),
    state               VARCHAR(50),
    square_feet         BIGINT,
    active_flag         VARCHAR(10)
);

CREATE TABLE IF NOT EXISTS dim_tenant (
    tenant_key          BIGINT,
    tenant_id           VARCHAR(50),
    tenant_name         VARCHAR(200)
);

CREATE TABLE IF NOT EXISTS fact_rent_payment (
    payment_key         BIGINT,
    payment_id          VARCHAR(50),
    lease_id            VARCHAR(50),
    property_key        BIGINT,
    tenant_key          BIGINT,
    payment_date        DATE,
    payment_amount      DECIMAL(18,2),
    payment_status      VARCHAR(50)
);
