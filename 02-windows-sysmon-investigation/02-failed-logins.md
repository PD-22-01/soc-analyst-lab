# Windows Investigation — Multiple Failed Logins

## Scenario

A SIEM reports 25 failed Windows logon attempts against one user within 10 minutes.

## Initial Questions

1. Is the source internal or external?
2. Is the source IP known?
3. Is the user currently working?
4. Were there successful logins afterward?
5. Are multiple accounts being targeted?
6. Is the affected account privileged?

## Investigation

Correlate:

- Failed authentication events
- Successful authentication events
- Source IP
- Destination host
- Username
- Timestamp
- Logon type
- Other affected accounts

## Possible Explanations

- User entered the wrong password repeatedly.
- A service has an outdated password.
- A mapped drive or scheduled task is using old credentials.
- Password spraying is occurring.
- Brute-force activity is occurring.
- An account may already be compromised.

## L1 Response

Do not immediately classify the alert as an attack.

Establish the pattern and correlate the evidence.

Escalate when there is evidence of:

- Successful suspicious authentication
- Multiple targeted accounts
- External attack infrastructure
- Privileged-account targeting
- Continued attack activity
