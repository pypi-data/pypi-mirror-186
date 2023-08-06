from setuptools import setup

name = "types-console-menu"
description = "Typing stubs for console-menu"
long_description = '''
## Typing stubs for console-menu

This is a PEP 561 type stub package for the `console-menu` package. It
can be used by type-checking tools like
[mypy](https://github.com/python/mypy/),
[pyright](https://github.com/microsoft/pyright),
[pytype](https://github.com/google/pytype/),
PyCharm, etc. to check code that uses
`console-menu`. The source for this package can be found at
https://github.com/python/typeshed/tree/main/stubs/console-menu. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/main/README.md for more details.
This package was generated from typeshed commit `af2ce282d57cb33857eaa8bfbee947081aa84671`.
'''.lstrip()

setup(name=name,
      version="0.7.0.2",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/console-menu.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=[],
      packages=['consolemenu-stubs'],
      package_data={'consolemenu-stubs': ['__init__.pyi', 'console_menu.pyi', 'format/__init__.pyi', 'format/menu_borders.pyi', 'format/menu_margins.pyi', 'format/menu_padding.pyi', 'format/menu_style.pyi', 'items/__init__.pyi', 'items/command_item.pyi', 'items/external_item.pyi', 'items/function_item.pyi', 'items/selection_item.pyi', 'items/submenu_item.pyi', 'menu_component.pyi', 'menu_formatter.pyi', 'multiselect_menu.pyi', 'prompt_utils.pyi', 'screen.pyi', 'selection_menu.pyi', 'validators/__init__.pyi', 'validators/base.pyi', 'validators/regex.pyi', 'validators/url.pyi', 'version.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
