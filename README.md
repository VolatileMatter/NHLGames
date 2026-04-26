# 720pier NHL Filter

A lightweight, static GitHub Pages tool for filtering saved [720pier.ru](https://720pier.ru) forum pages by NHL team. No backend required — everything runs in the browser.

---

## How It Works

1. You save raw HTML from a 720pier forum page into the `/html/` folder.
2. You run `generate_html_list.py` to update `html_list.json`.
3. When you open the page, it automatically fetches every file listed in `html_list.json`, parses all topic links out of them, deduplicates by topic ID, and loads them into memory.
4. Use the team dropdown or the custom filter box to find the posts you want.

Because the page loads all files on startup, you can accumulate days of forum pages and search across all of them at once.

---

## Setup

### Prerequisites

- A GitHub account with a repository set to serve GitHub Pages from the repo root (or `/docs`).
- Python 3 (for running the list generator locally — it does not run on GitHub Pages).

### First-time setup

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
```

### Adding new forum pages

1. Go to [720pier.ru](https://720pier.ru) and navigate to the forum section you want (e.g. *NHL Playoffs 2026*).
2. Open the page source (`Ctrl+U` / `Cmd+U`), select all, and copy.
3. Paste into a new file inside the `/html/` folder. Name it something descriptive, e.g.:
   ```
   html/nhl_playoffs_2026_page1.html
   html/nhl_playoffs_2026_page2.html
   ```
4. From the repo root, run:
   ```bash
   python generate_html_list.py
   ```
   This scans `/html/` and rewrites `html_list.json`.
5. Commit and push:
   ```bash
   git add html/ html_list.json
   git commit -m "Add forum pages YYYY-MM-DD"
   git push
   ```

### Running locally

Because the page uses `fetch()`, you need a local web server — you **cannot** open `index.html` directly via `file://`.

```bash
# Python 3 (simplest option)
python -m http.server 8000
# Then open http://localhost:8000 in your browser
```

---

## File Structure

```
├── index.html              # Main filter app (no build step required)
├── html_list.json          # Auto-generated list of saved HTML files
├── generate_html_list.py   # Run locally to regenerate html_list.json
├── html/                   # Your saved 720pier forum page HTML files
│   └── *.html
└── README.md
```

---

## Features

- **Auto-loads all saved pages** — no manual paste required after initial setup.
- **Deduplication** — the same topic appearing in multiple saved pages is shown only once, matched by topic ID.
- **Team filter dropdown** — all 32 NHL teams pre-loaded, with accent-variant aliases (e.g. *Montréal / Montreal*).
- **Custom filter box** — type any string (team name, round, quality like `4k`, broadcast like `TNT`) to narrow results.
- **Condensed games toggle** — show or hide "Condensed Games" compilation posts.
- **Sorted newest first** — results are ordered by the date embedded in each post title.
- **No dependencies** — pure HTML/CSS/JS, no npm, no build tools.

---

## Copyright & Legal Disclaimer

This tool is a **personal-use filtering interface**. It does not host, store, reproduce, stream, or distribute any copyrighted content.

- All NHL game footage, broadcast recordings, and related media are the intellectual property of the **National Hockey League (NHL)**, its member clubs, and their respective broadcast partners (ESPN, TNT, Sportsnet, TVA Sports, etc.).
- [720pier.ru](https://720pier.ru) is an independent third-party forum. This project has no affiliation with, endorsement from, or relationship to 720pier.ru.
- This tool only parses and displays **links to existing public forum threads**. It functions similarly to a search engine or bookmarking tool applied to content you have already accessed.
- You are solely responsible for ensuring your use of any linked content complies with the laws and terms of service applicable in your jurisdiction.

The author of this tool makes no representations regarding the legality of any content found on third-party sites. Use responsibly.

---

## License

This project's source code (HTML/CSS/JS/Python) is released under the [MIT License](https://opensource.org/licenses/MIT). The linked content on 720pier.ru is subject to its own terms and the rights of the respective copyright holders.