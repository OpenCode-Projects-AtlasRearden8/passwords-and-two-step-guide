# The Passwords & Two-Step Guide

Accounts and sign-ins, explained like a friend would. A calm, plain-English
beginner's manual covering:

- choosing a password manager, without the fear checkpoints skipped,
- building strong, memorable passphrases (4 random words, not tortured strings),
- turning on two-step codes (and knowing which kind is which),
- backup codes you can actually find later,
- passkeys in plain English,
- what to do after a breach alert (15-minute calm ritual),
- sharing access with a trusted person — the right door for the right need,
- a one-evening account tidy plan that really fits one evening.

The tone throughout is warm and ADHD-friendly: segments stand alone, "done"
beats "perfect," and pen-and-paper worksheets are included. It distills into
a set of **printable setup worksheets**, a **FAQ** of the questions people
actually ask, and a full **glossary** of plain-English definitions.

Part of the Asdale Dynamics, LLC beginner-guide series (same spirit behind
*The Massive AI Manual*: plain English, step by step, never condescending),
companions to *The Privacy Comfort Handbook* and *The Digital Papers
Handbook*.

## Read it

The Markdown "source of truth" lives in [`docs/`](docs/). Build the static
site and open it in any browser:

```bash
python3 build.py
```

That generates `site/`, a self-contained static HTML site with no external
dependencies, no analytics, no cookies, and no JavaScript requirements (one
optional print button). Open `site/index.html` to start reading. Everything
works offline.

## Test it

```bash
python3 -m unittest discover -s tests -v
```

Tests cover the markdown-to-HTML converter, the full site build (page
generation, navigation, internal links, worksheet anchors, attribution), and
a scan for secret-shaped strings in the built output.

## Contents

| Chapter | File | What it's for |
| --- | --- | --- |
| Start here | `docs/index.md` | Orientation, the whole idea in four sentences |
| 1 | `docs/01-choosing-a-password-manager.md` | Picking a manager + honest fear-checkpoints |
| 2 | `docs/02-strong-memorable-passphrases.md` | The 4-random-words recipe + memory tricks |
| 3 | `docs/03-two-step-codes.md` | Turning on 2FA; SMS vs app vs passkey |
| 4 | `docs/04-backup-codes.md` | Rescue codes: getting, storing, regenerating |
| 5 | `docs/05-passkeys-plain-english.md` | Passkeys: feel, setup, fallbacks |
| 6 | `docs/06-after-a-breach-alert.md` | Calm 15-minute breach-response ritual |
| 7 | `docs/07-sharing-access-with-a-trusted-person.md` | Level 1/2/3 sharing, etiquette, pitfalls |
| 8 | `docs/08-one-evening-account-tidy.md` | The two-hour map-and-migrate evening plan |
| 9 | `docs/09-setup-worksheets.md` | Six printable worksheets (A–F, pen-friendly) |
| 10 | `docs/10-faq.md` | The questions people actually ask |
| 11 | `docs/11-glossary.md` | Plain-English definitions |

## License

MIT — see [`LICENSE`](LICENSE).

Copyright (c) 2026 Asdale Dynamics, LLC. Written and maintained by
**Asdale Dynamics, LLC** — beginner-friendly education and tools, explained
like a friend would.
