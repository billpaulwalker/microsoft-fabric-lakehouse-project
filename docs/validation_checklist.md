# Data Validation Checklist

## Bronze Validation

- Source file exists.
- File is readable.
- Required columns are present.
- File row count is greater than zero.
- Ingestion timestamp is populated.
- Pipeline run ID is populated.

## Silver Validation

- Required fields are not null.
- Data types are correctly cast.
- Duplicate business keys are handled.
- Date fields are valid.
- Numeric fields are within expected ranges.
- Invalid records are isolated or flagged.
- Standardized values match expected domains.

## Gold Validation

- Fact table grain is clearly defined.
- Dimension keys are unique.
- Fact rows link to valid dimensions.
- Row counts reconcile to Silver where expected.
- Business metrics reconcile to source totals.
- Power BI relationship keys are valid.
- No unexpected nulls in reporting-critical fields.

## Operational Validation

- Pipeline run was logged.
- Row counts were captured.
- Duration was captured.
- Failure reason was captured if applicable.
- Watermark was updated only after successful completion.
- Alerts are configured for failure conditions.
