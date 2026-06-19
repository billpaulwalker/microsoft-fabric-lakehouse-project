# Microsoft Fabric Lakehouse Project

## Project Summary

This repository demonstrates an end-to-end Microsoft Fabric lakehouse pattern for a senior data engineering portfolio.

The project shows how legacy SQL Server / SSIS / Azure Data Factory-style data movement can be modernized into a Fabric lakehouse architecture using:

- Microsoft Fabric Lakehouse
- OneLake concepts
- Bronze, Silver, and Gold medallion layers
- Python / PySpark notebooks
- Delta table design
- Incremental loading patterns
- Data validation checks
- Pipeline logging
- Power BI-ready dimensional modeling
- Dev/Test/Prod deployment thinking

## Branding Purpose

This project is designed to support the LinkedIn Featured item:

**Microsoft Fabric Lakehouse Project**

It demonstrates the ability to design, build, explain, and productionize a modern data platform rather than simply list tools on a resume.

## Business Scenario

A commercial real estate organization receives data from operational source systems, Excel/CSV extracts, and API feeds. The business needs trusted reporting for Finance, Accounting, and Operations.

The goal is to create a governed lakehouse pipeline that lands raw source data, cleans and standardizes it, creates curated business-ready tables, and supports Power BI reporting.

## Architecture

```text
Source Systems
  ├── SQL Server / Operational Tables
  ├── CSV / Excel Files
  └── REST API Feeds

        ↓

Bronze Layer
  - Raw landed files
  - Raw Delta tables
  - Minimal transformation
  - Audit columns

        ↓

Silver Layer
  - Cleaned and standardized tables
  - Type casting
  - Deduplication
  - Business rule standardization
  - Data quality checks

        ↓

Gold Layer
  - Dimensional model
  - Fact tables
  - Dimension tables
  - Power BI-ready curated data

        ↓

Semantic Model / Power BI
  - Direct Lake or Import model
  - Business measures
  - Finance / Operations reporting
```

See [`architecture/fabric_lakehouse_architecture.md`](architecture/fabric_lakehouse_architecture.md).

## Repository Structure

```text
microsoft-fabric-lakehouse-project/
  README.md
  architecture/
    fabric_lakehouse_architecture.md
  docs/
    project_case_study.md
    data_contract.md
    validation_checklist.md
    deployment_checklist.md
    linkedin_featured_description.md
  notebooks/
    01_bronze_ingestion.py
    02_silver_cleaning.py
    03_gold_modeling.py
    04_data_validation.py
  sql/
    create_logging_table.sql
    create_watermark_table.sql
    gold_model_ddl.sql
  sample_data/
    raw/
      properties.csv
      leases.csv
      rent_payments.csv
    expected_outputs/
      dim_property.csv
      dim_tenant.csv
      fact_rent_payment.csv
  pipelines/
    fabric_pipeline_design.md
  .github/
    workflows/
      validation.yml
```

## Data Layers

### Bronze

The Bronze layer stores raw source data with limited transformation. The purpose is to preserve source fidelity and support reruns or reprocessing.

Typical Bronze columns:

- source_system
- source_file
- ingestion_timestamp
- pipeline_run_id
- raw business columns

### Silver

The Silver layer applies data cleaning and standardization.

Typical Silver logic:

- remove duplicates
- cast data types
- standardize column names
- validate required fields
- apply simple business rules
- track rejected records where applicable

### Gold

The Gold layer creates Power BI-ready curated tables.

Example Gold tables:

- dim_property
- dim_tenant
- fact_rent_payment

## Production Engineering Patterns Included

- Metadata-driven ingestion concept
- Logging table design
- Watermark table design
- Incremental loading pattern
- Data validation checklist
- Dev/Test/Prod deployment checklist
- Power BI-ready dimensional model
- GitHub Actions placeholder for validation

## How to Use This Repository

This repo is a portfolio scaffold. To make it fully executable in Microsoft Fabric:

1. Create a Fabric workspace.
2. Create a Lakehouse.
3. Upload sample files into the Lakehouse Files area.
4. Convert the `.py` notebook scripts into Fabric notebooks or import them as notebook code.
5. Update Lakehouse paths for your environment.
6. Run Bronze, Silver, Gold, and validation notebooks.
7. Connect Power BI to the Gold tables using Direct Lake or Import mode.
8. Add screenshots and results to the `docs/` folder.
