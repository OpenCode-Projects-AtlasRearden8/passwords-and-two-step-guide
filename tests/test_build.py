"""Tests for The Passwords & Two-Step Guide build.

Covers the markdown-to-HTML converter (unit level) and the whole site build
(end-to-end): page generation, navigation, internal links, worksheet anchors,
required attribution, and a scan for secret-shaped strings.
"""

import importlib.util
import re
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent

_spec = importlib.util.spec_from_file_location("pts_build", ROOT / "build.py")
build = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(build)


class ConverterInlineTests(unittest.TestCase):
    def test_headings(self):
        self.assertEqual(build.md_to_html("# Hello"), '<h1 id="hello">Hello</h1>')
        self.assertEqual(build.md_to_html("## Sub part"), '<h2 id="sub-part">Sub part</h2>')

    def test_heading_slug_is_url_safe(self):
        out = build.md_to_html("## What's a 2FA code?")
        self.assertIn('id="whats-a-2fa-code"', out)

    def test_paragraph(self):
        self.assertEqual(build.md_to_html("Just a normal line."), "<p>Just a normal line.</p>")

    def test_bold_italic_inline_code(self):
        out = build.md_to_html("A **bold**, *soft*, and `tick` moment.")
        self.assertIn("<strong>bold</strong>", out)
        self.assertIn("<em>soft</em>", out)
        self.assertIn("<code>tick</code>", out)

    def test_link_markdown_to_html(self):
        out = build.md_to_html("See [chapter](03-two-step-codes.md) now.")
        self.assertIn('href="03-two-step-codes.html"', out)
        self.assertNotIn('.md"', out)

    def test_link_with_anchor(self):
        out = build.md_to_html("See [entry](11-glossary.md#totp) next.")
        self.assertIn('href="11-glossary.html#totp"', out)

    def test_external_link_gets_noopener(self):
        out = build.md_to_html("Look at [a site](https://example.com) here.")
        self.assertIn('target="_blank" rel="noopener"', out)

    def test_raw_html_is_escaped(self):
        out = build.md_to_html("<script>alert(1)</script>")
        self.assertNotIn("<script>", out)
        self.assertIn("&lt;script&gt;", out)


class ConverterBlockTests(unittest.TestCase):
    def test_nested_bullets(self):
        md = "- one\n  - a\n  - b\n- two\n"
        out = build.md_to_html(md)
        self.assertIn("<ul>", out)
        self.assertIn("<ul>\n<li>a</li>\n<li>b</li>\n</ul>", out)
        self.assertIn("<li>one\n", out)

    def test_numbered_steps(self):
        out = build.md_to_html("1. Sign in\n2. Choose codes\n")
        self.assertIn("<ol>", out)
        self.assertIn("<li>Sign in</li>", out)

    def test_task_checkbox(self):
        out = build.md_to_html("- [x] done thing\n- [ ] open thing")
        self.assertIn('<input type="checkbox" checked>', out)
        self.assertIn('<input type="checkbox">', out)

    def test_table(self):
        md = "| A | B |\n| --- | --- |\n| 1 | 2 |\n"
        out = build.md_to_html(md)
        self.assertIn("<table>", out)
        self.assertIn("<th>A</th>", out)
        self.assertIn("<td>2</td>", out)

    def test_blockquote(self):
        out = build.md_to_html("> calm quote")
        self.assertIn("<blockquote>", out)
        self.assertIn("calm quote", out)

    def test_code_fence_escapes(self):
        out = build.md_to_html("```\n<b>&raw\n```")
        self.assertIn("<pre><code>", out)
        self.assertIn("&lt;b&gt;&amp;raw", out)

    def test_hr(self):
        self.assertEqual(build.md_to_html("---\n"), "<hr>")


class ContentLinkTests(unittest.TestCase):
    """Every .md link inside docs/ must point at a file that exists."""

    def test_all_internal_md_links_resolve(self):
        docs = sorted((ROOT / "docs").glob("*.md"))
        self.assertTrue(docs, "docs should not be empty")
        names = {p.name for p in docs}
        for path in docs:
            text = path.read_text(encoding="utf-8")
            for m in re.finditer(r"\]\(([^)#\s]+\.md)(#[^\)]*)?\)", text):
                target = m.group(1)
                self.assertIn(
                    target, names, f"{path.name} links to missing docs/{target}"
                )


class SiteBuildTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._tmp = tempfile.TemporaryDirectory()
        out = Path(cls._tmp.name) / "site"
        cls.written = build.build(out)
        cls.pages = {p: (out / p).read_text(encoding="utf-8") for p in cls.written if p.endswith(".html")}
        cls.out_dir = out

    @classmethod
    def tearDownClass(cls):
        cls._tmp.cleanup()

    def test_expected_pages_exist(self):
        expected = {
            "index.html", "01-choosing-a-password-manager.html",
            "02-strong-memorable-passphrases.html", "03-two-step-codes.html",
            "04-backup-codes.html", "05-passkeys-plain-english.html",
            "06-after-a-breach-alert.html", "07-sharing-access-with-a-trusted-person.html",
            "08-one-evening-account-tidy.html", "09-setup-worksheets.html",
            "10-faq.html", "11-glossary.html",
        }
        self.assertLessEqual(expected, set(self.pages))

    def test_assets_copied(self):
        self.assertIn("style.css", self.written)
        self.assertIn("favicon.svg", self.written)

    def test_nav_links_resolve_to_real_pages(self):
        for name, text in self.pages.items():
            for m in re.finditer(r'href="([A-Za-z0-9._/-]+\.html)(#[A-Za-z0-9-]*)?"', text):
                self.assertIn(
                    m.group(1), self.pages, f"{name} nav-links to missing {m.group(1)}"
                )

    def test_each_page_has_hash_anchors_for_every_internal_anchor_jump(self):
        for name, text in self.pages.items():
            for m in re.finditer(r'href="([A-Za-z0-9._/-]+\.html)#([A-Za-z0-9-]+)"', text):
                page = self.pages.get(m.group(1), "")
                self.assertIn(
                    f'id="{m.group(2)}"', page,
                    f"{name} anchors to #{m.group(2)} but {m.group(1)} lacks it",
                )

    def test_every_page_carries_attribution(self):
        for name, text in self.pages.items():
            self.assertIn("Asdale Dynamics, LLC", text)
            self.assertIn(build.COPYRIGHT, text)

    def test_index_is_start_here(self):
        self.assertIn("Start here", self.pages["index.html"])
        self.assertIn("aria-current", self.pages["index.html"])

    def test_print_button_on_worksheets_and_tidy(self):
        for slug in ("09-setup-worksheets", "08-one-evening-account-tidy"):
            self.assertIn("print-button", self.pages[f"{slug}.html"])
        for slug in ("10-faq", "index"):
            self.assertNotIn("print-button", self.pages[f"{slug}.html"])

    def test_no_secret_shaped_strings(self):
        secret_patterns = [
            r"(?i)(api[_-]?key\s*[:=])",
            r"(?i)(secret\s*[:=])",
            r"(?i)(access[_-]?token\s*[:=])",
            r"sk-[A-Za-z0-9]{10,}",
            r"ghp_[A-Za-z0-9]{10,}",
            r"AKIA[0-9A-Z]{8,}",
        ]
        for name, text in self.pages.items():
            for pat in secret_patterns:
                self.assertIsNone(
                    re.search(pat, text), f"secret-shaped string in {name}: {pat}"
                )

    def test_build_refuses_unsafe_out(self):
        with self.assertRaises(ValueError):
            build.build(Path("/"))

    def test_index_first_next_is_chapter_one(self):
        self.assertIn('class="next"', self.pages["index.html"])
        self.assertIn("01-choosing-a-password-manager.html", self.pages["index.html"])


if __name__ == "__main__":
    unittest.main()
