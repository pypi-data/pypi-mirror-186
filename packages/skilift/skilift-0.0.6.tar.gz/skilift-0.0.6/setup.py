import setuptools

from distutils.core import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="skilift",
    version="0.0.6",
    author="Bernard Czenkusz",
    author_email="bernie@skipole.co.uk",
    description="Development facility for the skipole WSGI Application generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bernie-skipole.github.io/skipole/",
    packages=['skilift', 'skilift.skiadmin', 'skilift.skiadmin.skiadminpackages', 'skilift.skiadmin.skiadminpackages.editcss',
              'skilift.skiadmin.skiadminpackages.editfiles',
              'skilift.skiadmin.skiadminpackages.editfolders', 'skilift.skiadmin.skiadminpackages.editpages', 'skilift.skiadmin.skiadminpackages.editparts',
              'skilift.skiadmin.skiadminpackages.editresponders', 'skilift.skiadmin.skiadminpackages.editsectionplaces', 'skilift.skiadmin.skiadminpackages.editsections',
              'skilift.skiadmin.skiadminpackages.editspecialpages', 'skilift.skiadmin.skiadminpackages.edittext', 'skilift.skiadmin.skiadminpackages.edittextblocks',
              'skilift.skiadmin.skiadminpackages.editvalidators', 'skilift.skiadmin.skiadminpackages.editwidgets'],
    include_package_data=True,
    keywords='wsgi application web framework',
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application"
    ],
)
