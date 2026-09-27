# 02 — Email Security & Phishing Investigation

## Objective

Practice the L1 investigation of suspicious emails and phishing alerts.

## Initial Triage Checklist

- Who received the email?
- What is the sender address?
- Does the display name match the sender?
- What is the subject?
- Are there suspicious URLs?
- Are there attachments?
- Is the domain legitimate?
- Are there signs of spoofing?
- Did the user click the link?
- Did the user submit credentials?
- Did the user open an attachment?

## Evidence to Collect

- Sender and recipient
- Timestamp
- Message ID
- URLs
- Domains
- IP addresses
- Attachment names and hashes
- Email headers
- Authentication results such as SPF, DKIM and DMARC
- Endpoint activity after interaction

## Response

If the email is confirmed malicious:

1. Preserve relevant evidence.
2. Identify other recipients.
3. Search for the same indicators across the environment.
4. Report or escalate according to the organization's process.
5. Contain affected accounts or endpoints when authorized.
6. Document every action.

## Important Principle

Do not immediately delete evidence or reset systems before the investigation process allows it. Preserve useful evidence first.
