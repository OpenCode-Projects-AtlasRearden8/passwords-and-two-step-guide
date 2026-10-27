# STATUS.md — The Passwords & Two-Step Guide

Last updated: 2026-10-27

## What was built

A beginner handbook about accounts and sign-ins — passwords and two-step
sign-ins, explained like a friend would — in the Asdale Dynamics, LLC
beginner-guide series style.

Contents:

- **`docs/` — 12 Markdown chapters (the source of truth):**
  - `index.md` — start here; the whole idea in four sentences
  - `01-choosing-a-password-manager.md` — picking a manager + honest fear-checkpoints
  - `02-strong-memorable-passphrases.md` — the 4-random-words recipe, memory tricks, traps
  - `03-two-step-codes.md` — 2FA made simple (SMS vs authenticator app vs passkey)
  - `04-backup-codes.md` — rescue codes: getting, storing, regenerating
  - `05-passkeys-plain-english.md` — what passkeys are, how sign-in feels, fallbacks
  - `06-after-a-breach-alert.md` — calm 15-minute breach-response ritual
  - `07-sharing-access-with-a-trusted-person.md` — Level 1/2/3 sharing, etiquette
  - `08-one-evening-account-tidy.md` — the two-hour evening plan (ADHD-friendly segments)
  - `09-setup-worksheets.md` — six printable pen-friendly worksheets (A–F)
  - `10-faq.md` — real questions, plain answers
  - `11-glossary.md` — plain-English definitions of every term used
- **`build.py`** — stdlib-only static site generator (Markdown subset → HTML),
  with a print button on the worksheets/tidy pages and full attribution footer.
- **`assets/`** — `style.css` (warm, print-friendly) and `favicon.svg`.
- **`site/`** — generated output (gitignored; rebuild with `python3 build.py`).
- **`tests/`** — 26 unittest cases: converter unit tests, whole-site build
  tests, internal-link/anchor integrity, attribution checks, and a
  secret-shaped-string scan.
- **`LICENSE`** — MIT, `Copyright (c) 2026 Asdale Dynamics, LLC`.
- **`README.md`** — overview, run/test instructions, chapter table; credits
  Asdale Dynamics, LLC.

## How to run it

```bash
python3 build.py             # builds the static site into site/
python3 -m unittest discover -s tests -v   # runs the test suite
```

Then open `site/index.html` in any browser. No dependencies to install; the
site works fully offline (no analytics, cookies, or required JavaScript).

## Verification results

- `python3 build.py` → "Built 14 files into site/" (12 pages + stylesheet + favicon); re-ran into a temp dir successfully.
- `python3 -m unittest discover -s tests` → **Ran 26 tests … OK**.
- Verified all internal `.md` links in docs resolve to real files (test).
- Verified all generated nav links and `#anchor` jumps resolve (test).
- Verified every page carries the "Asdale Dynamics, LLC" attribution and exact
  copyright line (test).
- No secrets/API keys/personal data in any file (scripted scan in tests).

## Known gaps

- The Markdown subset covers the constructs used here (headings, lists,
  tables, quotes, fenced code, inline styles); exotic Markdown is out of scope
  and would render as plain paragraphs.
- Print styling is tuned for US Letter/A4 but not tested against physical
  printers on every browser.
- Content is educational only — it is not a substitute for any provider's own
  account-recovery instructions, which can change without notice.
- No sitemap/SEO extras; site is a reading experience for one person, not a
  search target.
