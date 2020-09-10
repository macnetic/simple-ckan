# simple-ckan
![License badge](https://img.shields.io/github/license/macnetic/simple-ckan?style=flat)

A wrapper for CKAN APIs written in Python, with Requests.

[CKAN](https://ckan.org/) is a tool for making open data websites. It is used by national and local governments, research institutions, and other organizations who collect a lot of data.

The core API is documented [here](https://docs.ckan.org/en/latest/api/index.html)

## Installation

**Install via pip:**

```shell
$pip install simple-ckan
```

## Usage

**Connect to a CKAN API:**

```python
from simple_ckan import CKANInstance

demo = CKANInstance("https://demo.ckan.org")
demo.action.get.site_read() # Returns True if request is succesful
demo.action.get.package_list(limit=10, offset=0) # List packages
```
