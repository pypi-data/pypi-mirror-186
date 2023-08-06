import setuptools
from authsrv import __version__, __url__, __author__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='authsrv',
    version=__version__,
    description='wrapper for authsrv utilities',
    license='MIT',
    packages=setuptools.find_packages(),
    author=__author__,
    author_email='nneul@neulinger.org',
    keywords=['authsrv'],
    url=__url__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
