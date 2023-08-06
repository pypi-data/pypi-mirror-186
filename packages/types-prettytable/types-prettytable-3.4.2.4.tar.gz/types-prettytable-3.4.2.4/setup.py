from setuptools import setup

name = "types-prettytable"
description = "Typing stubs for prettytable"
long_description = '''
## Typing stubs for prettytable

This is a PEP 561 type stub package for the `prettytable` package. It
can be used by type-checking tools like
[mypy](https://github.com/python/mypy/),
[pyright](https://github.com/microsoft/pyright),
[pytype](https://github.com/google/pytype/),
PyCharm, etc. to check code that uses
`prettytable`. The source for this package can be found at
https://github.com/python/typeshed/tree/main/stubs/prettytable. All fixes for
types and metadata should be contributed there.

*Note:* The `prettytable` package includes type annotations or type stubs
since version 3.5.0. Please uninstall the `types-prettytable`
package if you use this or a newer version.


See https://github.com/python/typeshed/blob/main/README.md for more details.
This package was generated from typeshed commit `4fea314594fc21fe03af54c08d071c3621f3720e`.
'''.lstrip()

setup(name=name,
      version="3.4.2.4",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/prettytable.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=[],
      packages=['prettytable-stubs'],
      package_data={'prettytable-stubs': ['__init__.pyi', 'colortable.pyi', 'prettytable.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
