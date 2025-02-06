import os
import sys
sys.path.insert(0, os.path.abspath('.'))
extensions = ['sphinx.ext.autodoc', 'myst_parser']
html_theme = "basic"
html_static_path = ["_static"]
