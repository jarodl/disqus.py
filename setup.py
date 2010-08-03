from setuptools import setup, find_packages
import sys, os

version = '0.0.1'

install_requires = [
    # -*- Extra requirements: -*-
    "python-dateutil>=1.1",
    ]

def _py26OrGreater():
    return sys.hexversion > 0x20600f0

if not _py26OrGreater():
    install_requires.append("simplejson>=1.7.1")


setup(name='disqus',
      version=version,
      description="An API wrapper for Disqus",
      long_description=open("./README.md", "r").read(),
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Environment :: Console",
          "Intended Audience :: End Users",
          "Natural Language :: English",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries",
          "Topic :: Utilities",
          "License :: OSI Approved :: MIT License",
          ],
      keywords='disqus', 'API', 'commenting',
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
      [console_scripts]
      disqus=disqus.cmdline:main
      """,
      )
