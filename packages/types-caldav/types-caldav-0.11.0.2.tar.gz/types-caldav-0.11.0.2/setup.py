from setuptools import setup

name = "types-caldav"
description = "Typing stubs for caldav"
long_description = '''
## Typing stubs for caldav

This is a PEP 561 type stub package for the `caldav` package. It
can be used by type-checking tools like
[mypy](https://github.com/python/mypy/),
[pyright](https://github.com/microsoft/pyright),
[pytype](https://github.com/google/pytype/),
PyCharm, etc. to check code that uses
`caldav`. The source for this package can be found at
https://github.com/python/typeshed/tree/main/stubs/caldav. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/main/README.md for more details.
This package was generated from typeshed commit `af2ce282d57cb33857eaa8bfbee947081aa84671`.
'''.lstrip()

setup(name=name,
      version="0.11.0.2",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/caldav.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=['types-requests', 'types-vobject'],
      packages=['caldav-stubs'],
      package_data={'caldav-stubs': ['__init__.pyi', 'davclient.pyi', 'elements/__init__.pyi', 'elements/base.pyi', 'elements/cdav.pyi', 'elements/dav.pyi', 'elements/ical.pyi', 'lib/__init__.pyi', 'lib/error.pyi', 'lib/namespace.pyi', 'lib/url.pyi', 'lib/vcal.pyi', 'objects.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
