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


## Edit the research page

Add a research position to `RESEARCH_EXPERIENCE` in `build.py`:

```python
{
	"title": "Research position",
	"dates": "2026 - Present",
	"logo": "../assets/images/lab-logo.png",
	"alt": "Research laboratory logo",
	"details": "Laboratory name<br>Location<br>Manager: Name",
	"bullets": ["First responsibility.", "Second responsibility."],
},
```

Add publication text to `PUBLICATIONS` and talk text to `TALKS`. Both lists
support HTML links such as `<a href="...">paper title</a>` for documents and
presentations. The entry markup is defined in
`templates/research-experience.html` and `templates/research-list-item.html`.
## Edit the introduction carousel

The introduction page has its own carousel. Add, remove, or reorder entries in
`HOME_PHOTOS` in `build.py`:

```python
{
	"src": "assets/images/example.jpg",
	"alt": "A useful description of the image",
	"caption": "The caption shown below the image.",
},
```

The carousel markup comes from `templates/home-gallery.html` and
`templates/home-gallery-item.html`. The first item in `HOME_PHOTOS` is shown
first automatically.

## Edit About Me

Edit the paragraphs in `ABOUT_ME_PARAGRAPHS` in `build.py`. Each list item
becomes one paragraph on the introduction page. The surrounding markup comes
from `templates/about-me.html`.

## Add a photo to the Photos tab

Add a dictionary to `PHOTOS` in `build.py` with the image path, accessible alt
text, and caption. The full gallery markup comes from `templates/gallery.html`.