# Home SOC Lab

## Technologies

- Windows
- Ubuntu
- Sysmon
- Microsoft Sentinel
- Azure Log Analytics
- KQL
- MITRE ATT&CK

## Project Overview

Built a home SOC lab to practice endpoint telemetry collection, Windows event analysis, detection engineering and alert triage.

Sysmon was deployed on Windows endpoints and logs were forwarded into a Microsoft Sentinel / Log Analytics workspace.

## Detection Scenarios

### Failed Logon Burst

Generated repeated failed authentication attempts and traced the resulting Windows security events.

**Event ID:** 4625 — An account failed to log on.  
**MITRE ATT&CK:** T1110 — Brute Force.

### Local Administrator Creation

Created a local administrator account in the lab and investigated the resulting Windows security telemetry.

**Event ID:** 4720 — A user account was created.  
**MITRE ATT&CK:** T1136.001 — Create Account: Local Account.

### Service Installation

Generated a service-installation event and investigated the associated Windows telemetry.

**Event ID:** 7045 — A new service was installed in the system.  
**MITRE ATT&CK:** T1543.003 — Create or Modify System Process: Windows Service.

## Sentinel Workflow

1. Generate controlled activity in the lab.
2. Confirm the relevant Windows/Sysmon event.
3. Verify ingestion into Log Analytics.
4. Query the event using KQL.
5. Investigate surrounding activity.
6. Map the behavior to MITRE ATT&CK.
7. Tune the detection threshold.
8. Document the finding and response.

## Detection Tuning

Authentication alerts were tuned using thresholds and contextual investigation to reduce false positives.

**Endpoint Activity → Windows/Sysmon Telemetry → Sentinel → KQL → Detection → Investigation → MITRE Mapping → Tuning**
