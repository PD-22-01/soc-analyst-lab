# Incident Response — Brute Force / Password Spraying

## Scenario

The SOC receives an alert for repeated authentication failures.

## L1 Investigation

### Validate

Check:

- Number of failures
- Time window
- Source IP
- Target accounts
- Successful logins
- Internal vs external source
- Privilege of targeted accounts

### Determine the Pattern

**Brute force:** repeated attempts against one account.

**Password spraying:** a small number of common passwords attempted against many accounts.

The exact distinction depends on the observed pattern.

### Containment

Follow the organization's approved controls. Possible actions, when authorized, may include blocking a malicious source, disabling a confirmed compromised account, or enforcing additional authentication controls.

### Escalate

Escalate when there is successful suspicious authentication, privileged-account targeting, multiple affected users, or evidence of compromise.

## Interview Answer

> "I would first validate the failed-login alert and determine whether it targets one account or many accounts. I would identify the source IP, time pattern and whether any attempts were successful. I would then correlate authentication logs with the user's normal activity and check whether the source is known. If I find successful suspicious authentication or multiple targeted accounts, I would treat it as a potential compromise, follow the approved containment process and escalate."
