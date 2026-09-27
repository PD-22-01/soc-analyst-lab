# 02 — Windows & Sysmon Investigation Lab

## Objective

Practice investigating Windows security events using Sysmon-style telemetry and an L1 SOC workflow.

## Investigation Flow

**Alert → Event → Process → Parent Process → User → Network → IOC → Scope → Response**

## What to Look For

- Suspicious process creation
- Unusual parent/child process relationships
- PowerShell execution
- Encoded or obfuscated commands
- Office applications spawning shells
- Unsigned or unusual binaries
- Unexpected outbound network connections
- Multiple failed logons
- Privileged-account activity

## Important Sysmon Event IDs

| Event ID | Meaning |
|---|---|
| 1 | Process creation |
| 3 | Network connection |
| 7 | Image loaded |
| 10 | Process access |
| 11 | File created |
| 12/13/14 | Registry activity |
| 22 | DNS query |

The exact events available depend on the Sysmon configuration.

## L1 Principle

Do not label a process malicious based on its name alone. Correlate the process, parent process, command line, user, path, timestamp and related network activity.
