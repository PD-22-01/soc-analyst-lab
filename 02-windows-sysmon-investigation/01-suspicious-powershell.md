# Windows Investigation — Suspicious PowerShell

## Scenario

A SIEM alert reports PowerShell execution on a workstation.

### Alert

| Field | Value |
|---|---|
| Host | WIN-CLIENT-07 |
| User | alex.johnson |
| Process | powershell.exe |
| Parent | winword.exe |
| Time | 2026-09-27 11:18 IST |
| Sysmon Event | 1 — Process Creation |
| Initial Severity | High |

## Why It Is Suspicious

Microsoft Word spawning PowerShell can be suspicious because malicious documents can use macros or other techniques to launch command interpreters.

However, **suspicious does not automatically mean malicious**.

## L1 Investigation

### 1. Review the command line

Look for:

- Encoded commands
- Download commands
- Hidden execution
- Suspicious URLs
- Temporary directories
- Obfuscated strings

### 2. Check the parent process

Expected administrative PowerShell might be launched from legitimate tools or an administrator's terminal.

A Word → PowerShell relationship deserves additional investigation.

### 3. Check the user

Ask:

- Is the user expected to run PowerShell?
- Is the user privileged?
- Was the activity expected?

### 4. Check network activity

Correlate nearby network events.

Look for:

- New external connections
- Suspicious domains
- Unusual destination IPs
- Downloads immediately after process creation

### 5. Check for persistence

Review related file and registry activity when available.

## Response

If malicious execution is confirmed:

1. Preserve evidence.
2. Follow the approved endpoint-containment procedure.
3. Search for the same hash/domain/command line across the environment.
4. Escalate according to the SOC playbook.
5. Document the timeline.

## Interview Answer

> "I would not assume PowerShell is malicious just because it was executed. I would first inspect the command line, parent process, user, timestamp and related network activity. If Word spawned PowerShell with an encoded command and the host then connected to a suspicious external domain, that would increase my confidence that the activity is malicious. I would preserve the evidence, follow the authorized containment process and escalate if the incident is beyond L1 scope."
