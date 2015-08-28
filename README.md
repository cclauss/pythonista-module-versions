pythonista-module-versions
==========================

Compare the version numbers of extra modules in Pythonista with PyPI.  A run on Pythonista beta v1.6 build 160033:

* `ctypes` local version is _higher than_ the PyPI version!
* `dateutil` is probably the correct version for Python 2.7.
* flask, jedi, mechanize, Pillow (PIL), and xhtml2pdf (pisa) are current.


```
| module        | local    | PyPI       | 
| name          | version  | version    | 
| ------------- | -------- | ---------- | 
| bottle        | 0.12.5   | 0.12.8     | Upgrade?
| bs4           | 4.3.2    | 4.4.0      | Upgrade?
| Crypto        | 2.6      | 2.6.1      | Upgrade?
| dateutil      | 1.5-mpl  | 2.2        | Upgrade?
| dropbox       | ?????    | 3.22       | ?????
| ecdsa         | 0.11     | 0.13       | Upgrade?
| evernote      | ?????    | 1.25.1     | ?????
| faker         | ?????    | 0.0.4      | ?????
| feedparser    | 5.1.3    | 5.2.1      | Upgrade?
| flask         | 0.10.1   | 0.10.1     | 
| html2text     | 2014.4.5 | 2015.6.21  | Upgrade?
| html5lib      | 0.999    | 0.999999   | Upgrade?
| httplib2      | 0.8      | 0.9.1      | Upgrade?
| itsdangerous  | ?????    | 0.24       | ?????
| jedi          | 0.9.0    | 0.9.0      | 
| jinja2        | 2.7      | 2.8        | Upgrade?
### hasattr(markdown, 'version')
| markdown      | 2.2.0    | 2.6.2      | Upgrade?
| markdown2     | 2.2.1    | 2.3.0      | Upgrade?
| matplotlib    | 1.3.1    | 1.4.3      | Upgrade?
| mechanize     | 0.2.5    | 0.2.5      | 
| midiutil      | ?????    | Found      | ?????
| mpmath        | 0.18     | 0.19       | Upgrade?
| numpy         | 1.8.0    | 1.9.2      | Upgrade?
| oauth2        | 1.5.211  | 1.9rc1     | Upgrade?
| paramiko      | 1.13.0   | 1.15.2     | Upgrade?
| parsedatetime | 1.3      | 1.5        | Upgrade?
### hasattr(PIL, 'PILLOW_VERSION')
| PIL           | 2.9.0    | 2.9.0      | 
| pycparser     | 2.10     | 2.14       | Upgrade?
| pyflakes      | 0.7.3    | 0.9.2      | Upgrade?
| pygments      | 1.6      | 2.0.2      | Upgrade?
| pyparsing     | 2.0.1    | 2.0.3      | Upgrade?
| PyPDF2        | 1.22     | 1.25.1     | Upgrade?
| pytz          | 2013b    | 2015.4     | Upgrade?
| qrcode        | ?????    | 5.1        | ?????
| reportlab     |  $Id$    | 3.2.0      |  $Id$ 
| requests      | 2.5.1    | 2.7.0      | Upgrade?
| simpy         | 3.0.2    | 3.0.8      | Upgrade?
| six           | 1.6.1    | 1.9.0      | Upgrade?
| sqlalchemy    | 0.9.7    | 1.0.8      | Upgrade?
### hasattr(sqlite3, 'version')
| sqlite3       | 2.6.0    | 2.8.1      | Upgrade?
| sympy         | 0.7.4.1  | 0.7.6      | Upgrade?
| thrift        | ?????    | 0.9.2      | ?????
| werkzeug      | 0.9.4    | 0.10.4     | Upgrade?
| wsgiref       | ?????    | 0.1.2      | ?????
| xhtml2pdf     | 3.0.33   | 3.0.33     | 
| xmltodict     | 0.8.7    | 0.9.2      | Upgrade?
| yaml          | 3.09     | 3.11       | Upgrade?
| ------------- | -------- | ---------- | 
```
