# Incident #1 — Phishing Email Investigation

## Scenario

A user reports receiving an email that appears to come from Microsoft 365. The email claims that the user's account will be suspended unless they verify their password.

The user clicked the link but reports that they did not knowingly download or install anything.

> This is a simulated defensive-security scenario created for SOC training.

## Alert Summary

| Field | Value |
|---|---|
| Alert Type | Suspected Phishing |
| Severity | Medium — initial assessment |
| Affected User | `alex.johnson@example.local` |
| Email Subject | `Urgent: Your Microsoft 365 account will be suspended` |
| Sender | `microsoft365-security@micr0soft-support.com` |
| Recipient | `alex.johnson@example.local` |
| User Action | Clicked the link |
| Attachment | None |
| Initial Status | Under Investigation |

## Step 1 — Validate the Alert

The sender domain is suspicious:

`micr0soft-support.com`

The domain uses the number **0** in place of the letter **o** in "Microsoft."

This is a common phishing technique known as **typosquatting/lookalike-domain abuse**.

The message also creates urgency by threatening account suspension.

### Initial Assessment

The email should **not** be treated as legitimate merely because it uses Microsoft branding or language that appears professional.

## Step 2 — Identify the Indicators

### Email Indicators

- Sender: `microsoft365-security@micr0soft-support.com`
- Suspicious domain: `micr0soft-support.com`
- Subject: `Urgent: Your Microsoft 365 account will be suspended`
- No attachment
- User clicked the embedded link

### Simulated URL

`https://micr0soft-support.com/verify/account`

The URL should be treated as suspicious until verified.

## Step 3 — Determine User Impact

The most important question is:

**Did the user enter credentials after clicking the link?**

For this exercise, assume the user clicked the link but **did not enter a password**.

This changes the response because a click alone does not prove that credentials were compromised.

## Step 4 — Scope the Incident

An L1 analyst should search for:

1. Other recipients of the same email.
2. Other emails containing the same sender/domain.
3. DNS or proxy requests to the suspicious domain.
4. Authentication activity involving the affected user after the click.
5. Endpoint alerts around the same timestamp.
6. Other users who clicked the same URL.

### Example Search Window

Investigate activity from:

**2026-09-27 09:00–12:00 IST**

The exact time window should normally be adjusted based on the actual email timestamp and organizational procedures.

## Step 5 — Recommended L1 Response

If the investigation confirms that the email is malicious:

1. Preserve the email and relevant headers.
2. Search for the sender, domain and URL across the environment.
3. Identify all affected recipients.
4. Check whether anyone clicked the link.
5. Check whether credentials were submitted.
6. Check authentication logs for suspicious activity.
7. Report/block the malicious indicators according to the organization's approved process.
8. Escalate confirmed compromise or suspicious account activity.
9. Document the investigation.

## Step 6 — When to Escalate

Escalate to L2/incident response when:

- Credentials may have been submitted.
- There is evidence of account compromise.
- Multiple users are affected.
- Malware was downloaded.
- Suspicious post-click activity is detected.
- The scope cannot be determined at L1.
- Containment requires actions outside L1 authorization.

## Step 7 — Final Assessment

**Classification:** True Positive — Phishing Attempt

**User impact:** User clicked the link.

**Credential compromise:** Not currently confirmed.

**Recommended status:** Contain/monitor according to the organization's phishing playbook and escalate if additional evidence of compromise is found.

## Key SOC Lesson

**A phishing investigation is not just "delete the email."**

The analyst needs to determine:

**What happened → Who was affected → What did the user do → Was anything compromised → How far did it spread → What action is authorized?**

## Investigation Status

- [x] Initial alert validated
- [x] Suspicious indicators identified
- [x] User action identified
- [ ] Environment-wide IOC search completed
- [ ] Authentication logs reviewed
- [ ] Endpoint activity reviewed
- [ ] Containment completed
- [ ] Escalation completed
- [ ] Incident closed
