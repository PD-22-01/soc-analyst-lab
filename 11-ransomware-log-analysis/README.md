# Ransomware Log Analysis

## Project Overview
A defensive log-analysis exercise for recognizing indicators that may be associated with ransomware activity and practicing the L1 response workflow.

## Objectives
- Identify suspicious process and file-system activity.
- Recognize rapid changes across many files or directories.
- Correlate endpoint and authentication events.
- Separate an isolated event from a broader incident.
- Document containment and escalation considerations.

## Investigation Indicators
Potential indicators can include unusual process execution, suspicious PowerShell or script activity, rapid file modification/rename activity, unexpected administrative activity, security-tool tampering, multiple hosts showing similar behavior, and authentication events preceding suspicious endpoint activity.

## L1 Response Workflow
1. Validate the alert.
2. Identify the affected host and user.
3. Determine whether encryption/file modification activity is occurring.
4. Preserve relevant evidence.
5. Check whether other endpoints are affected.
6. Isolate the host if authorized by the incident-response procedure.
7. Escalate immediately when widespread impact is suspected.
8. Document the timeline, indicators and actions.

## Timeline Template
| Time | Host | Event | Evidence | Analyst Action |
|---|---|---|---|---|
| T1 | HOST-01 | Suspicious process | Process/command line | Investigate |
| T2 | HOST-01 | File activity spike | Event/log evidence | Assess scope |
| T3 | HOST-02 | Similar activity | Correlated event | Escalate |

## Skills Demonstrated
Log analysis, endpoint detection, correlation, incident response, scope assessment, escalation.

> This project documents defensive analysis only. It does not include ransomware creation or deployment.
