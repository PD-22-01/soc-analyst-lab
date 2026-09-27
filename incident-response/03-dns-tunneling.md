# Incident Response — Suspected DNS Tunneling

## Scenario

A workstation generates an unusually high number of DNS queries containing long, random-looking subdomains.

## Why It Can Be Suspicious

DNS can be abused as a covert channel to move data or communicate with command-and-control infrastructure.

One indicator alone does not prove DNS tunneling.

## L1 Investigation

Check:

- Query volume
- Query length
- Entropy/randomness
- Repeated unusual subdomains
- Domain age/reputation where approved tools are available
- Source host
- Process generating the DNS requests
- Timing and frequency
- Other network connections

## Correlation

Connect DNS activity with endpoint and network telemetry.

Ask:

**Which process generated the DNS traffic, and what else did that host do at the same time?**

## Escalation

Escalate if there is strong evidence of data exfiltration, malware, command-and-control activity or a compromised endpoint.

## Interview Answer

> "I would not classify long DNS queries as tunneling immediately. I would first establish the baseline and check query frequency, subdomain structure, the queried domain, the source host and the process responsible. I would correlate the DNS activity with endpoint and network events. If multiple indicators support tunneling or command-and-control activity, I would preserve the evidence, follow the approved containment process and escalate."
