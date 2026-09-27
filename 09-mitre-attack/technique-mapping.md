# MITRE ATT&CK Technique Mapping

The purpose of this file is to connect observed behavior to ATT&CK techniques during investigations.

## Example: Suspicious PowerShell

**Observed behavior:** PowerShell executed from a suspicious parent process.

**Potential ATT&CK technique:** T1059.001 — PowerShell

**Evidence to document:**

- Parent process
- Command line
- User
- Host
- Timestamp
- Network activity
- File activity

## Example: Valid Account Abuse

**Observed behavior:** Suspicious authentication using a legitimate account.

**Potential ATT&CK technique:** T1078 — Valid Accounts

Do not map a technique merely because it is possible. Map it when the observed evidence supports the behavior.

## Analyst Rule

**Behavior first → evidence second → technique mapping third.**
