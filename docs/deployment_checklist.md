# Dev/Test/Prod Deployment Checklist

## Pre-Deployment

- Code committed to Git.
- Pull request reviewed.
- Notebook parameters reviewed.
- Environment-specific settings validated.
- Lakehouse references verified.
- Secrets and credentials not hardcoded.
- Logging table available.
- Watermark table available.
- Validation notebook passes in Dev.

## Test Environment

- Run full pipeline against test data.
- Compare Bronze, Silver, and Gold row counts.
- Validate schema changes.
- Validate Power BI model compatibility.
- Confirm incremental load behavior.
- Confirm rerun behavior after simulated failure.

## Production Deployment

- Approval received.
- Release notes documented.
- Deployment window confirmed.
- Production connections validated.
- Initial run monitored.
- Row counts checked.
- Power BI refresh or Direct Lake model checked.
- Stakeholders notified after successful deployment.

## Rollback Plan

- Identify previous stable notebook version.
- Preserve prior Delta table version where applicable.
- Revert deployment if validation fails.
- Restore semantic model if impacted.
- Document root cause and corrective action.
