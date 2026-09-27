# Wireshark Network Analysis

## Project Overview
A defensive network-analysis lab for reviewing packet captures and identifying suspicious network behavior from an L1 SOC perspective.

## Objectives
- Understand packet-level network investigation.
- Filter traffic by protocol, IP, port and DNS activity.
- Identify unusual connections and communication patterns.
- Extract useful network IOCs.
- Correlate packet evidence with a security alert.

## Investigation Workflow
1. Confirm the capture time range.
2. Identify the affected host.
3. Review DNS queries and responses.
4. Inspect HTTP/HTTPS and other relevant protocols.
5. Look for unusual destinations, ports or repeated connections.
6. Follow streams when deeper context is required.
7. Extract IOCs such as IPs, domains and URLs.
8. Document evidence and escalation requirements.

## Useful Filters
    dns
    http
    tcp
    udp
    ip.addr == 10.0.0.10
    tcp.flags.syn == 1 && tcp.flags.ack == 0

## DNS Investigation
For suspected DNS abuse, review high query volume, unusually long or random-looking subdomains, repeated queries to one uncommon domain, TXT-record activity when relevant, and periodic communication.

## Skills Demonstrated
Wireshark, TCP/IP, DNS, packet analysis, network IOC identification, SOC investigation.

> Use only authorized lab traffic or public/sample PCAPs intended for analysis.
