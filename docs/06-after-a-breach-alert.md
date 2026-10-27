# 6. What to Do After a Breach Alert

"The email said my password was in a data breach." Your heartbeat does a small
drum solo. **Good news: this is survivable, ordinary, and handling it well
takes about 15 minutes.** Breaches are now a normal part of the internet's
weather. What matters is a calm, ordered response.

## Step 0: Confirm it's really from the real company

Twenty seconds of skepticism first: is the alert a scam, not a breach?

- Don't click links in the alert email. Go to the service **directly** (type
  the address or use your own bookmark) and check its notices, security page,
  or support area there.
- A real notice names the service, describes what leaked, and gives next
  steps — it **does not** ask you to "confirm your password" by replying or
  typing it into a different site. That ask is always a scam. (Same rule as
  six-digit codes in [chapter 3](03-two-step-codes.md): no real company asks.)
- If it arrived via a text or a chat, same rule: go direct, never through
  the message.

If it checks out (or you simply can't confirm), continue.

## The response, in order

1. **Change that site's password — now.** You're protecting against the leak
   being used, so go to the real site, change it, and make it long and
   generated (your manager does this in a tap). While you're there, sign out
   of all sessions/devices if offered — it removes strangers who got in.
2. **Check whether you had any overlap.** Did you use that password (or a
   close cousin) **on other sites**? If yes, change all of them too. If you'd
   built a one-password-per-site vault from
   [chapter 1](01-choosing-a-password-manager.md), this step is boring —
   that's the plan working.
3. **Look at the second lock.** If the site offers two-step verification
   ([chapter 3](03-two-step-codes.md)), turn it on. If it offers **new backup
   codes** post-breach, regenerate them, even if you saved old ones. Assume
   the attackers saw everything the lucky ones saw.
4. **Scan the account's activity.** Look for **unknown sign-ins** (most
   security pages show these), **new devices**, **password reset attempts**,
   and **unknown sessions or app grants** ("apps with account access"). Kill
   anything you don't recognize. Check your email filter for **password-reset
   emails you didn't ask for** — attack attempts in progress that quietly
   failed.
5. **If money or identity was involved — a bank, card, tax portal, email —
   also:** freeze the card if a payment account is touched, skim recent
   transactions for three months, and consider a credit freeze (a free
   process at the major bureaus in the US, worth doing once and keeping).
6. **Write down what happened.** four lines in your tidy notebook: date,
   site, what leaked, what you did. A record means next time it takes 5
   minutes instead of being a fog.

## What the alert *is* telling you (reality check)

- The leak exists **whether or not you got the alert**; most breach notices
  come weeks or months late, and some never arrive. Treat every alert as a
  representative sample of the *category of thing that happens all the time.*
- Password-only leaks are recoverable in 15 minutes. **That is the whole
  point** of the password-manager-plus-2FA routine you're building: it turns
  the classic disaster story into a 15-minute chore.
- A leak is **not** a verdict about you. It's a verdict about a server you
  don't operate. The shame was never on your side of the negotiation.

## Things to skip (the panic tax)

- Deleting all your accounts. Sprint changes leave more loose ends than the
  leak itself. Calm, targeted fixes win.
- Changing *every* password in one panic hour. Do the breached one plus any
  password twins tonight; the rest get covered quietly by
  [the tidy plan](08-one-evening-account-tidy.md).
- Paying for breach-protection subscriptions out of adrenaline. Freezes, free
  monitoring, and this guide's habits do most of the work; revisit paid
  services with calm later, if at all.

## Checking future leaks before they check you

- Sites like *haveibeenpwned.com* let you look up whether any **email** you
  use appears in known breach lists (they store and check hashes — the service
  has been a trusted industry standard for a decade). Register your email with
  its free notification option and it will tell you about future ones.
- Some password managers itself check your stored passwords against known
  leak lists ("Watchtower", "Security checkup" style features) — turn it on.
- Decide the ritual now: **any alert or any leak news → change that password
  + check 2FA + check sessions.** Rituals beat adrenaline.

The calm summary: **assume the breach is real, change the password, confirm
the lock, look for strangers, note it down.** Then go make tea. You handled it.
