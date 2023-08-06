from setuptools import setup

name = "types-humanfriendly"
description = "Typing stubs for humanfriendly"
long_description = '''
## Typing stubs for humanfriendly

This is a PEP 561 type stub package for the `humanfriendly` package. It
can be used by type-checking tools like
[mypy](https://github.com/python/mypy/),
[pyright](https://github.com/microsoft/pyright),
[pytype](https://github.com/google/pytype/),
PyCharm, etc. to check code that uses
`humanfriendly`. The source for this package can be found at
https://github.com/python/typeshed/tree/main/stubs/humanfriendly. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/main/README.md for more details.
This package was generated from typeshed commit `4fea314594fc21fe03af54c08d071c3621f3720e`.
'''.lstrip()

setup(name=name,
      version="10.0.1.4",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/humanfriendly.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=[],
      packages=['humanfriendly-stubs'],
      package_data={'humanfriendly-stubs': ['__init__.pyi', 'case.pyi', 'cli.pyi', 'compat.pyi', 'decorators.pyi', 'deprecation.pyi', 'prompts.pyi', 'sphinx.pyi', 'tables.pyi', 'terminal/__init__.pyi', 'terminal/html.pyi', 'terminal/spinners.pyi', 'testing.pyi', 'text.pyi', 'usage.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
