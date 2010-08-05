from setuptools import setup, find_packages
import sys, os

version = '0.0.3'

install_requires = [
    # -*- Extra requirements: -*-
    ]

def _usingPy26():
    return sys.hexversion > 0x20600f0

if not _usingPy26():
    install_requires.append("simplejson>=1.7.1")

setup(name='disqus',
      version=version,
      description="An API wrapper for Disqus (disqus.com)",
      long_description="""The Disqus API enables developers to interact with the
      Disqus data in their programs. This package conveniently wraps that API for
      easy use with python.""",
      classifiers=[
          "Development Status :: 3 - Alpha",
          "Environment :: Console",
          "Intended Audience :: Developers",
          "Natural Language :: English",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries",
          "Topic :: Utilities",
          "License :: OSI Approved :: MIT License",
          ],
      keywords=['disqus', 'API', 'commenting', 'community'],
      author='Jarod Luebbert',
      author_email='jarod@disqus.com',
      url='http://jarodl.com',
      license='MIT License',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=install_requires,
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
