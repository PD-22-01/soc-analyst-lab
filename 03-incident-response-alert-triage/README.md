# Incident Response & Alert Triage

## Platforms

- LetsDefend
- TryHackMe — SOC Level 1

## Project Overview

Worked simulated SOC alerts across phishing, brute-force and malware categories through the incident lifecycle.

## Incident Lifecycle

**Identification → Validation → Containment → Evidence Collection → IOC Extraction → Timeline → Root Cause → Escalation → Documentation**

## Phishing

Validate the email and sender, extract domains/URLs, determine whether the user interacted with the message, assess credential or payload exposure, determine scope and escalate confirmed compromise.

## Brute Force

Identify repeated authentication failures, determine source and targeted account, establish the timeframe, check for successful authentication following failures, assess scope and escalate when compromise is suspected.

## Malware

Identify the affected endpoint, review process/file context, extract hashes and network indicators, build a basic timeline, follow the approved containment process and escalate when deeper endpoint analysis is required.

## Evidence Collection

Record:
- Alert timestamp
- Affected user
- Hostname
- Source/destination IP
- Domains and URLs
- File hashes
- Relevant log events
- Process information
- Authentication activity
- Related alerts

## Timeline Analysis

1. Initial event
2. User/endpoint activity
3. Detection
4. Related activity
5. Analyst response
6. Containment
7. Escalation
8. Closure

## Verdict & Escalation

Every investigation documents the verdict, supporting evidence and escalation rationale for L2/L3.

## Post-Incident Summary

Completed cases use a standard template covering what happened, impact, evidence, timeline, actions, verdict, escalation, root cause and lessons learned.
