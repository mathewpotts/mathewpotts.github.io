# Maintaining the site

The site is deployed as static HTML, so it works on GitHub Pages without PHP.

Shared navigation and document structure live in `templates/header.html` and
`templates/footer.html`. Page-specific content remains in the HTML files under
the repository root and `pages/`.

After changing a template, rebuild the static pages from the repository root:

```text
python build.py
```

The included GitHub Actions workflow also runs this build automatically before
deploying to GitHub Pages. In the repository settings, set Pages to use
**GitHub Actions** as its source.

The script preserves each page's content between its existing `<main>` tags and
regenerates the shared shell around it. Update the page metadata in `build.py`
when adding a new page so its title, navigation state, and asset paths are
correct.

## Add a project

Add another dictionary to `PROJECTS` in `build.py`:

```python
{
	"title": "Project title",
	"url": "project-page.html",
	"dates": "2026 - Present",
	"description": "A short description.",
},
```

The project card markup comes from `templates/project.html`.

## Add a photo

Add a dictionary to `PHOTOS` in `build.py` with the image path, accessible alt
text, and caption. The photo page markup comes from `templates/gallery.html`.