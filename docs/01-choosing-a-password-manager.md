# 1. Choosing a Password Manager, Without Fear

A password manager is a locked notebook for your passwords. You unlock it once
with one passphrase you actually remember; it remembers everything else. That's
the entire concept. Everything else is packaging.

## Why the sticky-note era has to end

The old system — same comforting password everywhere — breaks in one place and
falls everywhere. Websites get breached, lists of email-and-password pairs get
traded for years, and attackers try your password on every other site (it's
called **credential stuffing**, and it works because reuse works). A manager
gives every account its own long, random password that exists nowhere else.

You are not lazy for wanting a manager. Remembering dozens of unique passwords
is a machine's job, and your job is remembering one good passphrase.

## What good enough looks like

Any serious password manager does these things:

- **Syncs** your vault across your phone, laptop, and browser.
- **Locks** your vault behind one passphrase you choose.
- **Fills** passwords into websites and apps with one tap, so the strong ones
  cost you nothing.
- **Generates** long random passwords on the spot.
- **Supports two-step codes** (see [chapter 3](03-two-step-codes.md)) and lets
  you store **secure notes** (for backup codes — see
  [chapter 4](04-backup-codes.md)).

That checklist is the whole meal. Everything else — teams, watch apps, travel
mode — is garnish. If a tool passes that list and is one you trust enough to
actually open, it's the right one.

## Familiar examples

These come up constantly, for different comfort levels; each is fine, and the
best one is whichever you'll use:

- **Built into your device:** Apple's *iCloud Keychain* (iPhone/Mac) or
  Google's *Password Manager* (Android/Chrome). Zero setup, already where your
  accounts live, much better than reuse — just weaker at secure notes and
  cross-brand sync.
- **Standalone apps** such as *1Password*, *Bitwarden*, or *Proton Pass*.
  Work everywhere, on everything, with more structure: secure notes, backup
  code storage, export.
- **A paper master list in a locked drawer.** Truly local, no software at
  all — works, but doesn't generate passwords or sync, and it's fragile.

## Fear checkpoints (the honest worries)

**"Now all my eggs are in one basket."**
Yes — one very strong basket. A manager vault is encrypted with your
passphrase, so breaking it means guessing a long passphrase, not a password.
You're upgrading from dozens of weak, reused baskets to one armored one.

**"What if I forget the passphrase?"**
This is the one real daily-life risk, and it's why [chapter 2](02-strong-memorable-passphrases.md)
teaches passphrases built to be unforgettable, and
[chapter 4](04-backup-codes.md) has you establish a rescue path *before*
you need it.

**"What if the manager company gets hacked?"**
Well-designed vaults (every mainstream one) encrypt client-side: the company
holds scrambled data it can't read without your passphrase. The realistic
worst case from a provider breach is exposed metadata and phishing fallout,
not "everyone's passwords leaked." Reduce risk anyway: keep backup codes
outside the vault ([chapter 4](04-backup-codes.md)) and turn on the second
lock everywhere that matters ([chapter 3](03-two-step-codes.md)).

**"What if the company vanishes?"**
Export. Every manager listed above can export your whole vault as a file.
Knowing *that you can leave* is what makes it safe to arrive. Do one export
early so the escape route is familiar — one page of [the tidy plan](08-one-evening-account-tidy.md)
covers it.

## Choosing in five minutes

- [ ] Do you want zero new software? → device built-in manager.
- [ ] Across iPhone **and** Windows, or Android **and** Mac? → standalone app.
- [ ] Prefer open-source/local options? → Bitwarden (or a self-hosted variant).
- [ ] Write down your pick somewhere physical.

## The one thing to do after picking

Choose the passphrase that unlocks the vault last — **after** reading
[chapter 2](02-strong-memorable-passphrases.md) — then install the app and
add your first five accounts. You don't need to migrate everything tonight.
The [one-evening plan](08-one-evening-account-tidy.md) handles the rest
later, calmly.
