# Fabric Lakehouse Architecture

## Purpose

This architecture demonstrates a practical Microsoft Fabric lakehouse pattern for moving raw source data into trusted analytics-ready data products.

## High-Level Flow

```text
Source Systems → Bronze → Silver → Gold → Semantic Model → Power BI
```

## Source Systems

Example sources:

- SQL Server operational tables
- CSV or Excel files from business users
- REST API feeds
- Third-party extracts

## Bronze Layer

The Bronze layer is the raw landing zone.

### Responsibilities

- Preserve source data as received.
- Add ingestion metadata.
- Avoid heavy business logic.
- Support replay and troubleshooting.

### Example Bronze Tables

- bronze_properties
- bronze_leases
- bronze_rent_payments

### Common Columns

- source_system
- source_file_name
- ingestion_timestamp
- pipeline_run_id
- raw source columns

## Silver Layer

The Silver layer is the cleaned and standardized layer.

### Responsibilities

- Rename columns into standard naming conventions.
- Cast data types.
- Remove duplicate records.
- Standardize values.
- Validate required fields.
- Prepare data for business modeling.

### Example Silver Tables

- silver_properties
- silver_leases
- silver_rent_payments

## Gold Layer

The Gold layer is the business-ready layer.

### Responsibilities

- Create dimensional models.
- Define table grain clearly.
- Support Power BI semantic models.
- Reduce transformation logic inside reports.
- Provide trusted metrics and curated business entities.

### Example Gold Tables

- dim_property
- dim_tenant
- fact_rent_payment

## Power BI Consumption

Power BI should consume the Gold layer through:

- Direct Lake when supported and appropriate
- Import mode when transformations, performance, or governance require it
- Semantic models with clearly defined relationships, measures, and business logic

## Production Considerations

A production version should include:

- Logging
- Monitoring
- Row count validation
- Schema validation
- Watermark tracking
- Retry handling
- Alerting
- Access control
- Workspace separation
- Dev/Test/Prod promotion
