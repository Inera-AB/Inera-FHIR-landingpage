# Inera FHIR Landing Page

Source for the [Inera FHIR specifications landing page](https://inera-ab.github.io/Inera-FHIR-landingpage/), built with [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

## Local development

**Prerequisites:** Python 3.x

```bash
# Install dependencies
pip install -r requirements.txt

# Serve locally with live reload
mkdocs serve
```

The site will be available at `http://127.0.0.1:8000`.

## Publishing

The site is automatically deployed to GitHub Pages when changes are merged to `main`.
The GitHub Actions workflow (`.github/workflows/deploy.yml`) runs `mkdocs gh-deploy`, which pushes the built site to the `gh-pages` branch.

Make sure GitHub Pages is configured to serve from the `gh-pages` branch:
`Settings → Pages → Source → Deploy from branch → gh-pages / (root)`

## Contributing

Edit the Markdown files under `docs/`. The main landing page is `docs/index.md`.
