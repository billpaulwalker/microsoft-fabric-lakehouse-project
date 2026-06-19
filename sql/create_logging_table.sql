-- Pipeline logging table
-- Adjust syntax as needed for Fabric Warehouse, Lakehouse SQL endpoint, or your SQL platform.

CREATE TABLE IF NOT EXISTS pipeline_run_log (
    pipeline_run_id      VARCHAR(100),
    pipeline_name        VARCHAR(200),
    environment          VARCHAR(50),
    source_system        VARCHAR(100),
    target_table         VARCHAR(200),
    start_time           TIMESTAMP,
    end_time             TIMESTAMP,
    status               VARCHAR(50),
    rows_read            BIGINT,
    rows_written         BIGINT,
    error_message        VARCHAR(4000),
    created_at           TIMESTAMP
);
