# L1 Alert Triage — Phishing Alert

## The 60-Second Mental Model

When a phishing alert arrives, think:

**WHO → WHAT → WHEN → WHERE → ACTION → IMPACT → SCOPE**

### WHO
Who received the email?

### WHAT
What was the email, sender, URL or attachment?

### WHEN
When was it received and when did the user interact with it?

### WHERE
Which systems, domains, IPs or endpoints were involved?

### ACTION
Did the user click, open, download or submit credentials?

### IMPACT
Was an account, endpoint or data potentially compromised?

### SCOPE
Are other users or systems affected?

## L1 Decision Flow

### Case A — User did not interact

- Preserve the email.
- Validate the indicators.
- Search for other recipients.
- Follow the organization's email-remediation process.
- Document and close if no further risk is identified.

### Case B — User clicked but entered no credentials

- Preserve evidence.
- Investigate the destination.
- Check endpoint/browser activity.
- Review authentication activity.
- Search for other affected users.
- Escalate if suspicious post-click activity exists.

### Case C — User entered credentials

Treat the situation as potentially compromised.

Follow the organization's account-compromise procedure, which may include:

- Immediate escalation.
- Session/token revocation where authorized.
- Credential reset.
- MFA review.
- Authentication-log investigation.
- IOC hunting.

### Case D — Malware downloaded/executed

Expand the investigation to the endpoint.

Look for:

- Process creation
- File creation
- Persistence
- Network connections
- Security-tool alerts
- Additional affected hosts

Escalate according to the incident-response procedure.


