# The WMO Sphinx Theme

A [Sphinx](https://python-sphinx.org) theme for documenting WMO projects.

## Installation and usage

The theme is available on [PyPI](https://pypi.org/project/wmo-sphinx-theme), and can
be installed as follows:

```bash
pip3 install wmo-sphinx-theme
```

Enavbling the theme from within your project's `conf.py`:

```python
import wmo_sphinx_theme

html_theme = 'wmo_sphinx_theme'
html_theme_path = wmo_sphinx_theme.get_html_theme_path()

html_css_files = ['wmo.css']
```

## Releasing

```bash
rm -fr build dist *.egg-info
python3 setup.py sdist bdist_wheel --universal
twine upload dist/*
```

### Code Conventions

* [PEP8](https://www.python.org/dev/peps/pep-0008)

### Bugs and Issues

All bugs, enhancements and issues are managed on [GitHub](https://github.com/wmo-im/wmo-sphinx-theme/issues).

## Contact

* [Maaike Limper](https://github.com/maaikelimper)
