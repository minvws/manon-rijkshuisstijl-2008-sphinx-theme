import os
from importlib.metadata import version

from sphinx.application import Sphinx

from sphinx_rijkshuisstijl_2008.translator import CustomHTMLTranslator

__version__ = version("sphinx-rijkshuisstijl-2008-theme")


def setup(app: Sphinx):
    root_path = os.path.abspath(os.path.dirname(__file__))
    theme_path = os.path.join(root_path, "theme/sphinx_rijkshuisstijl_2008")

    app.add_html_theme("sphinx_rijkshuisstijl_2008", theme_path)
    app.set_translator("html", CustomHTMLTranslator)

    return {"parallel_read_safe": True, "parallel_write_safe": True}
