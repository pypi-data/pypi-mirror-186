from setuptools import setup

name = "types-python-jose"
description = "Typing stubs for python-jose"
long_description = '''
## Typing stubs for python-jose

This is a PEP 561 type stub package for the `python-jose` package. It
can be used by type-checking tools like
[mypy](https://github.com/python/mypy/),
[pyright](https://github.com/microsoft/pyright),
[pytype](https://github.com/google/pytype/),
PyCharm, etc. to check code that uses
`python-jose`. The source for this package can be found at
https://github.com/python/typeshed/tree/main/stubs/python-jose. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/main/README.md for more details.
This package was generated from typeshed commit `4fea314594fc21fe03af54c08d071c3621f3720e`.
'''.lstrip()

setup(name=name,
      version="3.3.4.2",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/python-jose.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=['types-pyasn1'],
      packages=['jose-stubs'],
      package_data={'jose-stubs': ['__init__.pyi', 'backends/__init__.pyi', 'backends/_asn1.pyi', 'backends/base.pyi', 'backends/cryptography_backend.pyi', 'backends/ecdsa_backend.pyi', 'backends/native.pyi', 'backends/rsa_backend.pyi', 'constants.pyi', 'exceptions.pyi', 'jwe.pyi', 'jwk.pyi', 'jws.pyi', 'jwt.pyi', 'utils.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
