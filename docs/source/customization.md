# Customization

The Manon Sphinx theme behavior & style can be customized in multiple ways:

- Various template-level or nontrivial-style settings can be configured via your
  `conf.py` in `html_theme_options`; see :ref:`theme-options`.
- You can provide your own CSS stylesheet overrides via a
  :ref:`custom stylesheet <custom-stylesheet>`. This is suitable for changes
  that only need minor CSS modifications.

```
_custom-stylesheet:
```

## Custom stylesheet

If you need to modify the Manon Sphinx theme's default CSS styles in a way not
covered by the theme options from the next section, you may provide a custom CSS
stylesheet as follows:

- Create a file named `custom.css` anywhere you prefer (typically `_static/`,
  but this is solely convention) containing your desired overrides to the CSS
  found in the Manon Sphinx theme's `static/css/manon_theme.css`.
- Set the core Sphinx option `html_static_path`
  [html_static_path](https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-html_static_path)
  to either that file's path, or the directory it lives within.

```
_theme-options:
```

## Theme options

The Manon Sphinx theme's primary configuration route is the `html_theme_options`
variable, set in `conf.py` alongside the rest, e.g.:

```python
html_theme_options = {
    "description": "Manon Sphinx theme",
    "show_copyright_privacy_block_footer": True,
    "copyright_url": "/copyright.html",
    "privacy_url": "/privacy.html",
}
```

### Basics

Settings related to text display, logo, etc.

- `description`: Text blurb about your project, to appear under the logo.
- `logo`: Relative path (from `$PROJECT/_static/`) to a logo image, which will
  appear in the upper left corner above the name of the project.

### Footer

Settings related to the copyright and privacy information in the footer.

- `show_copyright_privacy_block_footer`: Set this to `true` to show the
  copyright and privacy information block in the footer.
- `copyright_url`: Set this to the URL for the copyright page. Defaults to
  `/copyright.html`.
- `privacy_url`: Set this to the URL for the privacy page. Defaults to
  `/privacy.html`.

