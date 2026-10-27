# 5. Passkeys in Plain English

A passkey is your fingerprint, face, or device PIN — used as a *key* to a
website, instead of a password. No six digits to peck at, nothing to type or
screenshot. You tap "Sign in," the device asks for your fingerprint, done.
Behind the curtain, a passkey is a cryptographic pair: the website holds an
*address*, and your phone or computer holds the *key* that only fits it.

## Why it's actually simpler

Say it as a story: the site checks possession of the key, not a secret word.
There's never a scrambled password to steal from the website database, so a
classic "the site was hacked, passwords leaked" story structurally can't
happen there. And no one can *phish* it, because the browser's entire
permission flow means the passkey only answers to the real website — the same
domain you typed. Fake lookalike sites get silence.

## How sign-in feels

- Visit the site. Press **Sign in with your device** (the phrasing varies).
- Your device asks *your* unlock — fingerprint, face, or PIN.
- Success — you're in. No code typing, no syncing to a second device.

That's the whole thing. On a laptop with your fingerprints already registered,
the ask-and-answer is two taps.

## The moving parts (the honest bits)

**Passkeys live on your device.** They sync with your device account (Apple's
"iCloud Keychain," Google's "Password Manager"), so your phone and laptop can
reach them across your family of devices. That's a feature — but it means:
keep your device account protected, too (its own strong passphrase +
its own 2FA). The account that syncs passkeys is a keystone.
[Chapter 2](02-strong-memorable-passphrases.md) helps.

**They don't float from stranger's device to stranger's device.** A passkey is
bound to you — Apple, Google, and Windows let you *export or sign in with a QR
code* to a nearby trusted device, but not to any random machine. That's the
very reason it beats typed codes in [chapter 3](03-two-step-codes.md).

**Backup paths still matter.** Just like codes in
[chapter 4](04-backup-codes.md), you want a **second way in** if a device dies:
commonly, a passkey registered on a second device, a security key, or the same
fallback two-step options. Sites usually ask you to add a second method during
setup — take advantage.

## Turning one on (if your account offers it)

When a site offers "passkeys" or "sign in with a passkey" (many now do:
Google, Apple, Microsoft, GitHub, PayPal, eBay and others):

1. Find it under **Security** or **Sign-in method**.
2. Choose **Create a passkey**. The device asks for your *unlock* and walks
   you through confirming it. On a phone this is fingerprint/face; on a laptop,
   Windows Hello or Touch ID.
3. When asked, add the **second, independent method** (another passkey, a
   recovery phone, or the same folder of backup codes). Note which method is
   the *primary* vs the *fallback* — the site explains this in one screen.
4. Print or file the recovery codes if it provides them:
   [chapter 4](04-backup-codes.md) has the habit.

## Where passkeys fit in the larger picture

- **Compared to a manager password:** passkeys are a *different tier* — you
  can be using both at the same time (and likely will be for a while).
- **Compared to SMS/authenticator codes:** stronger on every dimension —
  phishing-resistant, no codes to shoulder-surf or leak, nothing stolen from
  the site's database. Password managers now just store and offer them.
- **Debated corners:** cross-device vs synced; multi-device choices matter
  for groups (a family, or a small business). If that's you, e.g. a shared
  business account — passkeys get more complicated, and a shared manager
  setup from [chapter 7](07-sharing-access-with-a-trusted-person.md) may be
  simpler for now.

## Adapting your checklists

- [ ] Passkey for your primary email and phone-provider package.
- [ ] Second (backup) method registered for each passkey account.
- [ ] Device account locked down (passphrase + 2FA) — it guards all passkeys.

Passkeys are where sign-in experience is going, but you never have to do it
all today. **One account one day** — most people start with the one they sign
into most mornings.
