# 03 — Microsoft Sentinel & KQL

## Objective

Practice SIEM investigation and threat hunting using Microsoft Sentinel concepts and Kusto Query Language (KQL).

These queries are **portfolio/lab examples** and should be adapted to the actual table schema in a Sentinel workspace.

## Core L1 Workflow

1. Start with the alert.
2. Identify the relevant table.
3. Filter the time range.
4. Filter the affected user/host/IP.
5. Examine related events.
6. Expand the investigation using IOCs.
7. Document findings.

## Useful KQL Concepts

- where
- project
- summarize
- count
- distinct
- extend
- sort
- order
- bin
- join
- has
- contains
- ago()

## Important Reminder

KQL syntax and available fields depend on the data connector and table. Always inspect the schema before assuming a field exists.
