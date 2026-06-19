# Data Contract

## Purpose

This document defines expected source data structures for the sample commercial real estate data used in this project.

## Source: properties.csv

| Column | Type | Required | Description |
|---|---|---:|---|
| property_id | string | yes | Unique property identifier |
| property_name | string | yes | Property display name |
| property_type | string | yes | Office, Retail, Industrial, Multifamily |
| city | string | yes | City |
| state | string | yes | State |
| square_feet | integer | yes | Total property square footage |
| active_flag | string | yes | Y/N active indicator |

## Source: leases.csv

| Column | Type | Required | Description |
|---|---|---:|---|
| lease_id | string | yes | Unique lease identifier |
| property_id | string | yes | Related property |
| tenant_id | string | yes | Tenant identifier |
| tenant_name | string | yes | Tenant display name |
| lease_start_date | date | yes | Lease start date |
| lease_end_date | date | yes | Lease end date |
| leased_square_feet | integer | yes | Leased area |
| monthly_rent | decimal | yes | Contracted monthly rent |

## Source: rent_payments.csv

| Column | Type | Required | Description |
|---|---|---:|---|
| payment_id | string | yes | Unique payment identifier |
| lease_id | string | yes | Related lease |
| payment_date | date | yes | Date payment was received |
| payment_amount | decimal | yes | Payment amount |
| payment_status | string | yes | Paid, Late, Pending, Failed |
