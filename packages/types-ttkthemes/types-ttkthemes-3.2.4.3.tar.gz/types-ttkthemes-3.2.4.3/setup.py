from setuptools import setup

name = "types-ttkthemes"
description = "Typing stubs for ttkthemes"
long_description = '''
## Typing stubs for ttkthemes

This is a PEP 561 type stub package for the `ttkthemes` package. It
can be used by type-checking tools like
[mypy](https://github.com/python/mypy/),
[pyright](https://github.com/microsoft/pyright),
[pytype](https://github.com/google/pytype/),
PyCharm, etc. to check code that uses
`ttkthemes`. The source for this package can be found at
https://github.com/python/typeshed/tree/main/stubs/ttkthemes. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/main/README.md for more details.
This package was generated from typeshed commit `4fea314594fc21fe03af54c08d071c3621f3720e`.
'''.lstrip()

setup(name=name,
      version="3.2.4.3",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/ttkthemes.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=[],
      packages=['ttkthemes-stubs'],
      package_data={'ttkthemes-stubs': ['__init__.pyi', '_imgops.pyi', '_utils.pyi', '_widget.pyi', 'themed_style.pyi', 'themed_tk.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
