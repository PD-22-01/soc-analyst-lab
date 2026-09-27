# Splunk SIEM Dashboard

## Project Overview
A defensive SOC lab for ingesting security logs into Splunk, building searches, and creating an analyst-focused dashboard for authentication and suspicious activity.

## Objectives
- Understand SIEM data ingestion and normalization.
- Search Windows/security-style events using SPL.
- Detect repeated authentication failures and unusual activity.
- Build dashboard panels that help an L1 analyst triage alerts.
- Document investigation findings and escalation decisions.

## Lab Scenario
Synthetic Windows security events are used to simulate normal activity and suspicious authentication behavior. The analyst investigates the data rather than relying on a single alert.

## Investigation Workflow
1. Identify the alert or unusual pattern.
2. Confirm the time range and affected host/user.
3. Search related authentication events.
4. Compare successful and failed logons.
5. Check source IP and account activity.
6. Determine whether the behavior is isolated or repeated.
7. Record evidence and recommended L1 action.

## Example SPL
    index=windows EventCode=4625
    | stats count by Account_Name, src_ip, host
    | sort - count

## Dashboard Panels
- Failed logons by user
- Failed logons by source IP
- Authentication activity over time
- Top affected hosts
- Successful logons following repeated failures

## Skills Demonstrated
Splunk, SPL, SIEM monitoring, authentication analysis, alert triage, IOC identification, incident documentation.

> This is a defensive learning project using synthetic/lab data. No production credentials or sensitive logs are included.
