# Email Security & Phishing Investigation

## Technologies and Sources

- Email headers
- SPF / DKIM / DMARC
- Any.Run
- VirusTotal
- URLScan.io
- AbuseIPDB

## Project Overview

Investigated phishing and BEC-style samples end to end, from initial email analysis through IOC enrichment and final verdict.

## Investigation Workflow

**Email → Headers → Authentication → Sender/Domain → URLs/Attachments → Sandbox → IOC Enrichment → Verdict**

## Header Analysis

Reviewed email headers and traced messages through the **Received** chain.

Key questions:
- Where did the message originate?
- Which mail servers handled it?
- Do timestamps make sense?
- Does the visible sender match the underlying infrastructure?
- Are there suspicious relay or originating IPs?

## SPF / DKIM / DMARC

Used SPF, DKIM and DMARC results and alignment as evidence when assessing sender authenticity. Authentication failures were treated as investigation signals, not automatic proof of maliciousness.

## Spoofing and Lookalike Domains

Investigated typosquatting, character substitution, lookalike domains, suspicious subdomains and sender/display-name mismatches.

## URL and Attachment Analysis

Analyzed suspicious URLs and attachments in controlled environments, focusing on redirects, destination domains, file types, hashes, network indicators and observed behavior.

## IOC Enrichment

Enriched potential IOCs with VirusTotal, URLScan.io and AbuseIPDB to add context to the investigation.

## Verdict

Cases were classified using the available evidence, for example:
- Malicious / confirmed phishing
- Suspicious / requires escalation
- Benign / false positive
- Undetermined

**Headers + Authentication + Infrastructure + URL/File Analysis + IOC Context = Defensible Verdict**
