import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "simple-ckan-macnetic",
    version = "0.0.2",
    author = "Magnus Oksbøl Therkelsen",
    author_email = "magnus@thrklsn.dk",
    description = "A wrapper for CKAN APIs, written in Python",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/macnetic/simple-ckan",
    packages = setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires = ">=3.6"
)