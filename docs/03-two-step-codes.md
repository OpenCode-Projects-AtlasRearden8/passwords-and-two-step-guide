# 3. Two-Step Codes (2FA), Made Simple

A password is something you *know*. A two-step code is something you *have* —
usually a six-digit number that changes every 30 seconds on your phone. With
both, a stranger who steals your password still can't get in, because they
don't have your phone. That single sentence is why 2FA is the highest-value
five minutes you can spend on any account.

## The everyday experience

Sign in with email + password as usual. The site asks for a code. You open an
authenticator app (or your Messages/phone app), glance at a six-digit number,
type it in. Done — you're usually not asked again for 30 days on that device.
The annoyance is honestly small; the protection is structural: guesses,
phishing, and breached passwords all die at that second step.

## The three kinds of second step

**1. Your phone number / text message (SMS or voice).**
The easiest and most familiar — and the weakest. Texts can be hijacked
(**SIM swapping**: someone convinces your carrier to move your number to their
SIM) and messages sit unencrypted on carrier machines. It's still *far* better
than nothing, so **turn it on if it's all a service offers and today**. But
upgrade when you can.

**2. An authenticator app (time-based codes, or "TOTP" in the glossary).**
The sweet spot for most people. Apps like those built into your password
manager, or Google Authenticator, Microsoft Authenticator, and Authy, show a
six-digit code that refreshes every 30 seconds, entirely on your device. No
carrier, no interception of texts, works in airplane mode. Set the app to
**back up its codes** (most can now) — this matters in
[chapter 4](04-backup-codes.md).

**3. A passkey / security key (something physical or built in).**
A fingerprint, face, PIN, or a USB key you tap. Strictly speaking it's a
better-than-2FA upgrade called **passkeys** — covered in plain English in
[chapter 5](05-passkeys-plain-english.md). Start here if your accounts are
high-value and your devices are modern.

## Turning one on, generally (it is always the same shape)

1. Sign in and find **Security** (sometimes under *Account Settings*).
2. Look for **two-step verification**, **2FA**, **two-factor authentication**,
   or **sign-in verification**. Google sometimes shows *Security Checkup*;
   Amazon calls it *Two-Step Verification*; Apple *Two-Factor Authentication*.
3. Choose **authenticator app** when offered.
4. The site shows a **QR code**. Open your authenticator app → *add account*
   (a plus sign) → *scan QR code* → point your camera at the screen.
5. The app shows a streaming six-digit code for that site. Type it back into
   the site to confirm. It'll usually show **backup codes** at the end — save
   them! That's literally the next chapter: [04-backup-codes.md](04-backup-codes.md).

Keep the phone you set it on until it's confirmed, and try signing out and back
in once so you know where the code comes from. That first test replaces months
of anxiety.

## What genuinely worries people (and the honest answers)

**"What if my phone dies?"** Authenticator codes are *derived on the phone*,
not sent through it. If it dies, you land on the **backup codes** path
([chapter 4](04-backup-codes.md)) — which exist for exactly this. Keep at
least one code somewhere real.

**"What if I'm selling my phone?"** Before you hand it over, move your codes:
on the new phone, re-add accounts or use the app's transfer/export feature,
then wipe. The [account tidy plan](08-one-evening-account-tidy.md) includes a
slot for this.

**"Doesn't the site have my code if I type it?"** Only the site gets the code,
for you, right then. A code you gave a *fraudulent* site is dead in 30
seconds — which is precisely why codes beat static passwords. Scammers still
try ("read me the code") — remember: **nobody legitimate ever asks for a
six-digit code out loud, in text, or over the phone.** That request *is* the
red flag. See the privacy chapters if you'd like a longer weather report on
scams.

## A sliver of housekeeping

- [ ] Write down which of these you'd like to switch on for your top four
      accounts (email, bank, phone, social).
- [ ] Do ONE today. Email is the best one — because whoever owns your email
      can reset every other password you own.
- [ ] While you're in there, glance for **backup codes** and stash them
      ([chapter 4](04-backup-codes.md)).

Not perfect yet? Fine. One account per day this week beats zero forever.
