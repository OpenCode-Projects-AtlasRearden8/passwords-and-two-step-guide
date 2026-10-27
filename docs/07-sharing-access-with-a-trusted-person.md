# 7. Sharing Access With a Trusted Person

At some point life asks for help: a spouse who handles the bills, an adult
child who helps their parent, a business partner who needs the shared
bookkeeping site, a sibling who'll need to reach things if something happens
to you. Sharing access is normal and necessary. The goal of this chapter is to
do it on purpose — with the right door, the right scope, and a way back.

## First: match the door to the need

Not every situation needs the same key. There are three levels, from least to
most powerful — **start at level 1** and move up only if you must.

### Level 1 — Share the surface, not the vault

If someone just needs to *do a task* on your behalf, the best door is the
site's **built-in** permission, which never exposes your password:

- Banks, doctors' portals, utilities: look for **"Joint," "authorized user,"
  "caregiver access," "delegate"** — set up through those institutions, so
  they have a record too.
- Google accounts: **"Delegate"** for calendar/mail tasks (grants limited
  access rather than your sign-in).
- Mobile plans: add an **authorized user** on the account line for support
  calls.
- Email rarely needs delegation — but a shared **household email address**
  (e.g. for utilities) can be cleaner than sharing anyone's personal one.

Level 1 wins because it's **revocable and loggable** — both of you can see it,
and either of you can end it.

### Level 2 — Let them *use* a password without ever *seeing* a password

Password managers can hand someone a credential so they sign in, and the
password itself is never revealed. This is the everyday route for small
teams, households, and partners:

- Create a **shared collection/folder/vault** inside the manager (Bitwarden
  organizations, 1Password family/team vaults, etc.).
- Move **only the specific logins** that person needs into it — not your
  whole vault.
- Grant **"can use"/"no read-back"** permission when offered, so the password
  is filled in but can't be copied out in plain text.
- When the job ends (they change jobs, you close the account), remove their
  access — a right-click, not a negotiation.

Use this for: shared household utilities, a family trust/rewards account,
small-business bookkeeping, reselling (eBay/Amazon) seller accounts.

### Level 3 — The real emergency door (planned in advance)

Some two-factor, deep, or hard-to-recover accounts need a genuinely trusted
person to hold a key. Two good tools here, both take under an hour.

**Built-in "trusted contact" / legacy programs.** Apple, Google, and others
let you name an **actual trusted-contact person** for account recovery or
after-death access (Google *Inactive Account Manager*, Apple *Digital
Legacy*, Facebook *Legacy Contact*). These institutions authenticate the
helper and walk them through proof; the codes and vaults never spill in plain
sight. This works **with** the institution — never against it — and it
survives on purpose, more than any note under the mattress.

**Break-glass: one sealed page, two real names.** For everything not covered
by a program: one physical envelope, stored with deeds/wills, holding
*the account you'd want them to reach, and which kind of help they'd need*
(recovery program name, not raw passwords if you can avoid it), and agreed
next steps. See also [the tidy plan](08-one-evening-account-tidy.md) slot for
this. Passwords in this envelope only for the few accounts that have no
recovery program — and rotate those passwords if the envelope ever has to
come back out of storage.

## The etiquette and the rules that keep both sides safe

- **Never type your password over chat, text, email, or the phone.** Not even
  to family. Apps like the password-manager share flow exist for this reason;
  typed secrets exist in logs forever.
- **Never share a two-step code or its backup codes** ([chapter 4](04-backup-codes.md))
  outside an arrangement you deliberately made. A code is not "a little
  password." It's the key.
- **Change, don't lend.** Better: have the person create their *own* managed
  login than borrow yours — for the accounts that allow separate users
  (eBay seller, bank authorized users, streaming profiles).
- **Set an end date in your head.** Shared access should have a natural end:
  "while she's abroad," "through tax season," "until my surgery recovery."
  Write the date on the same paper where you agreed on the arrangement.
- **A shared device is a shared screen.** If they will ever sign into
  accounts on **your** device, there are no borders: put two-step codes and
  passkeys into a browser profile or user account they don't use — or just
  don't share devices, only accounts.

## What to not do (the stories that end badly)

- **The "we're a couple, same password everywhere" plan.** Romance great,
  security terrible: one leak becomes both leaks, and breakups become password
  crises. A household should have **two** password managers' setups if there
  are two people — with one *shared* collection for the joint stuff.
- **A shared phone with no user separation.** Fingerprint for you, then ask
  the OS for a separate **work profile / guest space** for anything that
  shouldn't mix.
- **"It's easier if I keep her signed in."** Easier now, unpleasant later —
  and often visible to strangers via app sync you forgot about. Sign out of
  shared devices when you're done.
- **Sharing your *email password*** as the "simplest" way to help with
  anything. Your email is the keystone: whoever has it can silently reset
  every other password you own. Hand over the *task*, not the keystone.

## The five-minute version to do today

- [ ] Name the **one trusted person** most situations would involve. Write
      their name on paper.
- [ ] For **your top-three accounts**, look up whether the site offers a
      built-in trusted-contact or recovery-contact feature — note (yes/no/unsure)
      on the same paper.
- [ ] Agree with that person, in one conversation, what's shared *by design*
      (and what isn't). Vague sharing is where trust leaks.

For the full household/business setup, [the tidy plan](08-one-evening-account-tidy.md)
reserves one evening segment for it.
