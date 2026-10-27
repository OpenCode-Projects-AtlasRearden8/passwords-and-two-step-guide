# 11. Glossary

Plain-English definitions, in the order they matter in this guide. If a term
appears in a chapter, it lives here too.

**2FA / two-factor authentication / two-step verification.** Proving it's you
with two different *kinds* of proof: something you know (a password) and
something you have (your phone, an app, a key). The names vary by site; the
idea is one.

**Account takeover.** When someone else gains control of your account — the
scenario this book is quietly preventing.

**App grant / OAuth / "sign in with Google."** When one site asks *another*
service for permission to see bits of your account. Convenient — and worth
revisiting every tidy, since old grants often outlive the apps they served.

**Backup codes / recovery codes.** One-time-use rescue strings a site gives
you when you enable 2FA. Each works once as a substitute second step.
[Chapter 4](04-backup-codes.md) is about keeping them.

**Breach / data breach.** A server somewhere got broken into and its data
left. Not your failure — but the reason unique passwords matter.

**Client-side encryption.** Your data is scrambled on *your* device, before
it ever goes to the provider's server. What makes "the manager got hacked"
different from "the database leaked" — see
[chapter 1](01-choosing-a-password-manager.md).

**Credential stuffing.** Attackers take leaked email-password pairs and try
them at logins everywhere. It works exactly as long as you reuse passwords;
unique passwords make it pointless.

**Credit freeze.** A free, reversible lock on your credit file at the three
major US bureaus, so nobody can open new credit in your name. Nothing to do
with passwords — makes identity theft annoying for the thief.

**Export.** The password-manager function that writes your whole vault to a
file. Rehearse it once: [chapter 2](02-strong-memorable-passphrases.md) and
[the tidy plan](08-one-evening-account-tidy.md) cite it as the escape route.

**Fingerprint/Face/PIN unlock (biometric/PIN).** The device-level "it's me"
gate. Not *on the website itself* — it just unlocks keys stored on the device.

**Keystone account.** The account whose "reset my password" email gives access
to everything else — your email. It gets your highest locks, first.

**MFA (multi-factor authentication).** The general version of 2FA with any
number of factors. You never have to say it out loud.

**Passkey.** A modern sign-in pair: the site holds a public half, and your
device holds (and syncs) the private half. Nothing to type; nothing to phish
— [chapter 5](05-passkeys-plain-english.md).

**Passphrase.** A password made of linked random words — long, memorable,
*generated from randomness*, not from poetry you love. The core technique of
[chapter 2](02-strong-memorable-passphrases.md).

**Password generator.** Built into every password manager: the button that
makes a long random string of letters/numbers/symbols — once per account, so
each is unique.

**Password manager.** An app that stores all your passwords in one encrypted,
passphrase-locked vault, and fills them in for you. Defined (with
fear-checkpoints) in [chapter 1](01-choosing-a-password-manager.md).

**Phishing.** A fake login page, text, or email designed to catch the secret
you were about to give to the real site. Two-step codes and passkeys are the
structural fix; slow-down-and-go-direct is the human fix.

**Secure note.** An encrypted, non-password storage bin inside a password
manager — commonly where backup codes, security-question answers, and
account-recovery instructions live.

**Security key.** A physical USB/NFC stick that holds passkeys or acts as a
second step. A serious upgrade for the accounts you care most about; a
convenient extra key for the same [passkey flow](05-passkeys-plain-english.md).

**Security questions.** The "mother's maiden name" fallback. Treat answers
as extra passwords (say something memorable but false/impersonal) and file
them with [backup codes](04-backup-codes.md).

**Session.** A moment-when-you-stayed-logged-in entry — the thing the list on
a site's security pages shows, and the thing you revoke when something
doesn't look like it was you.

**SIM swapping.** A scam in which someone convinces your phone carrier to
move your number to *their* SIM, then intercepts your text-message 2FA codes.
The reason authenticator apps beat SMS codes ([chapter 3](03-two-step-codes.md)).

**TOTP.** The technical name for the rolling 30-second six-digit codes an
authenticator app shows. You'll see this acronym in settings menus; no need
to remember it.

**Trusted contact / legacy contact / Inactive Account Manager / Digital
Legacy.** Official, named programs from big providers for letting a person
you chose reach certain bits of your account (now, later, or only if you go
quiet). The *good* Level 3 door — see
[chapter 7](07-sharing-access-with-a-trusted-person.md).

**Vault.** The encrypted storage inside a password manager. One vault, one
passphrase, on every device.
