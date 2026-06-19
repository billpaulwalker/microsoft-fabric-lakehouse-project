# Fabric Pipeline Design

## Pipeline Name

`pl_fabric_lakehouse_cre_ingestion`

## Pipeline Purpose

Orchestrate ingestion of raw commercial real estate data into the Bronze layer, then trigger Silver cleaning, Gold modeling, and validation notebooks.

## Pipeline Flow

```text
Start
  ↓
Lookup active source configuration
  ↓
For each active source
  ↓
Copy or land raw file/data into Bronze
  ↓
Run Bronze ingestion notebook
  ↓
Run Silver cleaning notebook
  ↓
Run Gold modeling notebook
  ↓
Run validation notebook
  ↓
Log success/failure
  ↓
End
```

## Parameters

| Parameter | Description |
|---|---|
| environment | dev, test, prod |
| pipeline_run_id | unique run identifier |
| source_system | source system name |
| load_type | full or incremental |
| watermark_value | prior successful high-water mark |

## Logging Requirements

Each pipeline run should capture:

- pipeline_run_id
- pipeline_name
- environment
- source_system
- target_table
- start_time
- end_time
- status
- rows_read
- rows_written
- error_message

## Failure Handling

- Fail fast for missing required files.
- Log failure reason.
- Do not update watermark on failed runs.
- Support rerun from previous successful watermark.
- Alert support owner for production failures.
