# Active Directory Detection Lab

## Project Overview
A Windows Active Directory security-monitoring lab focused on authentication, account-management and privilege-related events that an L1 SOC analyst should recognize.

## Lab Components
- Windows client
- Windows Server / Domain Controller
- Active Directory
- Windows Security Event Logs
- Optional SIEM ingestion

## Key Events
| Event ID | Investigation Use |
|---|---|
| 4624 | Successful logon |
| 4625 | Failed logon |
| 4634 | Logoff |
| 4672 | Special privileges assigned |
| 4688 | Process creation |
| 4720 | User account created |
| 4726 | User account deleted |
| 4768 | Kerberos authentication ticket requested |
| 4769 | Kerberos service ticket requested |
| 4776 | NTLM credential validation |

## Scenarios
### Brute-force pattern
Look for repeated 4625 events followed by a successful authentication.

### Unexpected account creation
Investigate 4720, the creating account, timing and related activity.

### Privileged logon
Review 4672 and correlate it with the user, host and surrounding authentication events.

## L1 Investigation Questions
- Which account was involved?
- Which host generated the event?
- What was the source?
- When did the activity occur?
- Was the activity expected?
- Are there related events before or after it?
- Does the evidence require escalation?

## Skills Demonstrated
Active Directory, Windows Security Events, authentication, Kerberos/NTLM concepts, SIEM correlation, L1 triage.
