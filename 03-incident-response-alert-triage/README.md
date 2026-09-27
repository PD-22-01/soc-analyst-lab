# 03 — Incident Response & Alert Triage

## Objective

Practice the SOC Analyst L1 response process for common security incidents.

## L1 Triage Framework

### 1. Understand the Alert

Determine what triggered the alert and which security control generated it.

### 2. Validate

Ask whether the activity is expected, suspicious or clearly malicious.

### 3. Identify Scope

Determine:

- Affected user
- Host/device
- Account
- Source and destination IP
- Domain
- Time window
- Related alerts

### 4. Collect Evidence

Gather relevant logs, authentication events, process information, network connections and IOCs.

### 5. Assess Severity

Consider:

- Asset importance
- User/account privilege
- Evidence of compromise
- Business impact
- Number of affected systems
- Whether the threat is still active

### 6. Contain

Perform only actions authorized by the organization's incident-response procedure.

Examples include isolating an endpoint, disabling a compromised account, blocking a malicious domain or IP, or removing a malicious email.

### 7. Escalate

Escalate when the incident exceeds L1 authority, scope or technical complexity.

### 8. Document

Record:

- What happened
- What was observed
- Evidence
- Actions taken
- Who was notified
- Current status
- Recommended next step

## Common L1 Scenarios

- Phishing email
- Multiple failed logins
- Suspicious PowerShell activity
- Malware alert
- Impossible-travel login
- Suspicious outbound connection
- DNS tunneling indicator
- Account compromise
- Brute-force activity

## Analyst Mindset

A good L1 analyst should avoid jumping to conclusions. Start with the alert, validate the evidence, establish scope, follow the playbook, and escalate when necessary.
