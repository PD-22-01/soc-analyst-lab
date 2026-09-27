# Wazuh Home SOC Lab

## Project Overview
A blue-team lab design for using Wazuh as a SIEM/XDR-style monitoring platform to collect endpoint telemetry, investigate alerts, and practice L1 SOC workflows.

## Architecture
Endpoint -> Wazuh Agent -> Wazuh Manager/Indexer -> Dashboard -> Analyst

The lab can use a Windows endpoint for endpoint/security events and an Ubuntu endpoint for Linux telemetry.

## Objectives
- Deploy and understand the Wazuh agent/manager architecture.
- Monitor Windows and Linux security activity.
- Investigate authentication and process-related alerts.
- Identify suspicious changes and prioritize alerts.
- Practice evidence collection and escalation.

## Example Scenarios
### Repeated failed logons
Review authentication failures, source information, affected account, and timing.

### New local account
Investigate who created the account, when it was created, and whether related activity occurred.

### Suspicious process activity
Review process details, parent/child relationships, command-line arguments, and surrounding events.

## L1 Investigation Workflow
1. Validate the Wazuh alert.
2. Identify host, user, timestamp and rule.
3. Review related events.
4. Determine whether the activity is expected.
5. Check for additional indicators.
6. Contain only according to the incident procedure.
7. Escalate when scope or impact requires it.
8. Document evidence and conclusion.

## Skills Demonstrated
Wazuh, SIEM/XDR concepts, endpoint monitoring, log analysis, alert triage, incident response, Windows/Linux security.

> Lab content is for defensive training and uses controlled/synthetic activity.
