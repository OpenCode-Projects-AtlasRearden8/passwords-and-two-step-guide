# 10. FAQ — The Questions People Actually Ask

Real questions, in the words people really ask them. If your question isn't
here, the [glossary](11-glossary.md) may have its vocabulary.

## Passwords and managers

**Is a password manager safe? What if it gets hacked?**
Serious ones store your data encrypted client-side: the company holds
scrambled data it can't read — your passphrase never leaves your device. A
provider breach exposes metadata, not passwords. Meanwhile your *current*
system (reuse, sticky notes) leaks passwords in bulk every year. Also see
[chapter 1](01-choosing-a-password-manager.md).

**Do I need a password manager if my browser remembers passwords for me?**
It's much better than reusing passwords, and you may not need the standalone
step yet. But a manager adds: secure notes for codes, cross-brand sync, and
generating truly long random passwords. Move up when built-in starts to chafe
([chapter 1](01-choosing-a-password-manager.md) helps choose).

**What if I forget my one passphrase?**
That's the *one* real daily-life risk, and the whole book hedges it: a
passphrase built to be remembered ([chapter 2](02-strong-memorable-passphrases.md)),
a written training copy at home, and backup codes stored *outside* the vault
([chapter 4](04-backup-codes.md)).

**Can I use the same manager passphrase as my email password?**
No. The vault passphrase should exist nowhere else. One stash of passphrases,
one lock each — that's the point.

**Is writing passwords on paper bad?**
Paper in a locked/shared-safely drawer is genuinely fine — it can't be phished
or breached. Its flaws are (a) no password suggestions, (b) no copy-paste, so
you hand-type weaker passwords, (c) it doesn't sync. Use it as the place the
*rescue* things live (backup codes, passphrase-training sheet), not as the
main vault.

## Two-step codes and 2FA

**Is SMS code good enough?**
Better than nothing, much worse than an authenticator app — texts can be
hijacked via SIM swaps and sit on carrier machines. If it's what exists today,
take it. Upgrade when you can: [chapter 3](03-two-step-codes.md).

**What if my phone dies and I'm stuck?**
That's why the [backup codes chapter](04-backup-codes.md) exists — keep one
set physically somewhere findable, and you get back in from any single device
in ten minutes.

**Which account should I do first?**
Email. Always email. It's the master key to every other password-reset flow,
so it gets the strongest lock first — codes, a passkey if possible, and its
own backup codes on paper.

**I got an SMS code and never asked for one. Should I panic?**
No panic, but do act: it normally means someone just correctly guessed/typed
your password and hit your second lock, which did its job. Change that
password now, then scan for unknown sessions; you were one step ahead of
them: [chapter 6](06-after-a-breach-alert.md).

**Should I ever give a six-digit code to anyone?**
No. Not to "support," not "just to test." A code that leaves you can open your
account within its ~30-second life. That request is the scam signal itself.

## Passkeys

**What actually is a passkey, in one sentence?**
A cryptographic pair — one half stored on your device, the site holds the
public half — so "signing in" becomes "prove I have the key," with your
fingerprint/face/PIN unlocking your half.

**Why is it better than a password manager?**
They're not competing. Passkeys remove the *typed* password entirely on any
site that supports them (nothing to phish, nothing ever stolen), while your
manager keeps handling the rest. Over time the manager will also start
storing passkeys, and the line blurs in your favor.
[Chapter 5](05-passkeys-plain-english.md) covers the feel and setup.

**What happens if I lose the device?**
You need your second path: a passkey on another device, a security key, or
recovery codes — always registered *while* you set the first one up. Sites
that offer passkeys walk you through adding a fallback in the same flow.

**Are passkeys ready for older family members?**
When their devices are modern, passkeys are often *easier* than passwords —
nothing to remember or type. The catch is if a phone dies, a grandchild-savvy
helper and a paper backup-code copy smooth it. Do [chapters 3–4](03-two-step-codes.md)
first if in doubt; passkeys later.

## Breaches and identity

**How do I know if my email was in a breach?**
Look your email up at *haveibeenpwned.com* — a respected free lookup with an
expected-result-notification option. Some password managers also scan your
saved passwords against leak databases. Ironically this is one place
"free is best" is real.

**Someone got my password. What's the priority order?**
Change that password first, and every twin/cousin it has elsewhere. Then
2FA ([chapter 3](03-two-step-codes.md)) and backup codes fresh. Then unknown
sessions. Money/identity accounts get extra eight: cards, credit freeze,
three months of activity. The full ritual:
[chapter 6](06-after-a-breach-alert.md).

**Is a credit freeze actually free?**
In the US, yes at all three major bureaus — takes about 20 minutes online and
a PIN to unfreeze. It's the single most protective free thing you can do for
identity-theft peace of mind. It has nothing to do with your *passwords*, but
it's often recommended alongside tidying accounts.

## Trusted people and life admin

**Can I share Netflix-style, same password, with my whole family?**
Households get by, but every leak becomes all leaks, and past-partners still
own your password *forever*. Better: separate vaults + one **shared
collection** ([chapter 7](07-sharing-access-with-a-trusted-person.md)).

**What if my relative needs to reach my stuff "some day"?**
That's the Level 3 door: built-in recovery/legacy programs (Apple, Google,
etc.) plus one physical envelope with the agreed plan — never a list of raw
passwords you can't revoke. [Chapter 7](07-sharing-access-with-a-trusted-person.md)
and [the tidy plan](08-one-evening-account-tidy.md) cover setting both.

## The tidy plan

**I only have 40 minutes, not a whole evening. What do I do?**
Do Segment 2 (email + top 5 accounts, new passwords + 2FA on email) and stop.
That's the highest-value 40 minutes in account hygiene — the rest waits
patiently: [chapter 8](08-one-evening-account-tidy.md).

**I have ADHD / low energy / chronic pain. Is this plan still for me?**
The plan *is* a low-energy design: segments are independent, each takes
scanned-not-perfected minutes, and the map on paper is the only thing holding
it together. Two 60-minute halves or five 20-minute sittings work equally
well. The [worksheets](09-setup-worksheets.md) exist exactly for pen-and-paper
one-at-a-time sittings.

**Do I really need to close old accounts? Can't I just never log in again?**
You *can* — until they're breached in 2031 and join a leak list with your
email and a password you reused. Closing is it being gone-on-purpose: one
page per site under "delete my account" in their support docs, ten minutes
per account during the tidy.
