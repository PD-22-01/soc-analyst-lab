# Sample Phishing Email

## Email Metadata

**From:** Microsoft 365 Security <microsoft365-security@micr0soft-support.com>  
**To:** alex.johnson@example.local  
**Subject:** Urgent: Your Microsoft 365 account will be suspended  
**Date:** 2026-09-27 10:14 IST

## Email Body

Your Microsoft 365 account has been flagged for unusual activity.

To prevent your account from being suspended, please verify your account immediately:

`https://micr0soft-support.com/verify/account`

Failure to verify your account may result in restricted access.

Microsoft 365 Security Team

## Analyst Observations

### 1. Suspicious Sender

The domain is:

`micr0soft-support.com`

The spelling resembles "Microsoft" but replaces the letter **o** with **0**.

### 2. Urgency

The email threatens account suspension to encourage immediate action.

### 3. Suspicious URL

The verification link does not use an official Microsoft domain.

### 4. User Interaction

The user clicked the link.

This means the investigation should continue beyond simply classifying the email.

## Questions for the Analyst

1. Did the user enter credentials?
2. Was MFA requested?
3. What IP address did the user connect to?
4. Did the endpoint download anything?
5. Were there suspicious sign-ins afterward?
6. Did other users receive the same message?
7. Is the domain present in DNS/proxy logs?
8. Does the URL redirect somewhere else?

## Expected Initial Classification

**Likely phishing — investigate and validate before final closure.**
